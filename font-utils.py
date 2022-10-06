from contextlib import redirect_stderr
import contextlib
import pprint
import sys
import fontTools.ttLib
import fontTools.cffLib.width
import fontforge

FONT_SPECIFIER_NAME_ID = 4
FONT_SPECIFIER_FAMILY_ID = 1


def shortName(font):
    """Get the short name from the font's names table"""
    font = fontTools.ttLib.TTFont(font, ignoreDecompileErrors=True)
    with contextlib.redirect_stderr(None):
        names = font["name"].names
    name = ""
    family = ""
    for record in font["name"].names:
        if b"\x00" in record.string:
            name_str = record.string.decode("utf-16-be")
        else:
            name_str = record.string.decode("latin-1")
        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            name = name_str
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            family = name_str
        if name and family:
            break
    return name, family


def font_name(font_path):
    font = fontTools.ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    with contextlib.redirect_stderr(None):
        names = font["name"].names

    details = {}
    for x in names:
        if x.langID == 0 or x.langID == 1033:
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors="ignore")

    pprint.pprint(details)

    return details[4], details[1], details[2]


def is_monospace(font_path):
    font = fontTools.ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    with contextlib.redirect_stderr(None):
        hmtx = font["hmtx"].metrics
    widths = [x[0] for x in hmtx.values()]
    return len(set(widths)) == 1


def check_monospace(font_path):
    font = fontTools.ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    I_cp = ord("I")
    M_cp = ord("M")
    I_glyphid = None
    M_glyphid = None
    for table in font["cmap"].tables:
        for codepoint, glyphid in table.cmap.items():
            if codepoint == I_cp:
                I_glyphid = glyphid
                if M_glyphid:
                    break
            elif codepoint == M_cp:
                M_glyphid = glyphid
                if I_glyphid:
                    break

    if (not I_glyphid) or (not M_glyphid):
        sys.stderr.write("Non-alphabetic font %s, giving up!\n" % sys.argv[1])
        sys.exit(3)

    glyphs = font.getGlyphSet()
    i = glyphs[I_glyphid]
    M = glyphs[M_glyphid]
    return i.width == M.width


def is_monospace2(font_path):
    f = fontforge.open(font_path)
    i = f["i"]
    m = f["m"]
    return i.width == m.width


print(font_name("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf"))
print(is_monospace("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf"))
print(check_monospace("/home/ruby/.local/share/fonts/LXGWWenKai/LXGWWenKai-Bold.ttf"))
print(is_monospace("/home/ruby/.local/share/fonts/LXGWWenKai/LXGWWenKai-Bold.ttf"))
print(is_monospace2("/home/ruby/.local/share/fonts/LXGWWenKai/LXGWWenKai-Bold.ttf"))
print(is_monospace("LXGWWenKaiMono-Regular2.ttf"))
print(check_monospace("LXGWWenKaiMono-Regular2.ttf"))
print(is_monospace2("LXGWWenKaiMono-Regular2.ttf"))
