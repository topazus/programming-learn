#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2012, Google Inc.
# Author: Dave Crossland (dcrossland a google com)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
# 		 http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# A script for generating a HTML file containing copyright notices
# for all fonts found in a directory tree, using fontTools


def usage():
    print >> sys.stderr, "copyrightnotices.py /directory/tree/of/fonts/ html_file_to_output_notices_to.html "


# Pseudo Code:
#
# for each font file found in the tree:
#   check space exists, if not, create it with width 1000
#   check nbsp exists, if not, create it
#   check nbsp has same advanceWidth as space, if not, set it
#   write the new font

import os, sys, codecs, json
from datetime import date
from fontTools import ttLib


def openFont(filename):
    return ttLib.TTFont(filename)


def getGlyph(font, uchar):
    for table in font["cmap"].tables:
        if not (table.platformID == 3 and table.platEncID in [1, 10]):
            continue
        if uchar in table.cmap:
            return table.cmap[uchar]
    return None


def addGlyph(font, uchar, glyphName):

    # Add to glyph list
    glyphOrder = font.getGlyphOrder()
    assert glyphName not in glyphOrder
    glyphOrder.append(glyphName)
    font.setGlyphOrder(glyphOrder)

    # Add horizontal metrics (to zero)
    font["hmtx"][glyphName] = [0, 0]

    # Add to cmap
    for table in font["cmap"].tables:
        if not (table.platformID == 3 and table.platEncID in [1, 10]):
            continue
        if not table.cmap:  # Skip UVS cmaps
            continue
        assert uchar not in table.cmap
        table.cmap[uchar] = glyphName

    # Add empty glyph outline
    font["glyf"].glyphs[glyphName] = ttLib.getTableModule("glyf").Glyph()
    return glyphName


def getWidth(font, glyphname):
    return font["hmtx"][glyphname][0]


def setWidth(font, glyphname, width):
    font["hmtx"][glyphname] = (width, font["hmtx"][glyphname][1])


def writeFont(font, filename):
    # check the os.path.exists works
    while os.path.exists(filename):
        filename = filename + "-nbsp"
    font.save(filename)
    print("Wrote font to", filename)


def checkAndFix(filename):
    # open
    font = openFont(filename)
    # check
    space = getGlyph(font, 0x0020)
    nbsp = getGlyph(font, 0x00A0)
    if not nbsp:
        nbsp = addGlyph(font, 0x00A0, "nbsp")
    spaceWidth = getWidth(font, space)
    nbspWidth = getWidth(font, nbsp)
    if spaceWidth != nbspWidth:
        setWidth(font, nbsp, spaceWidth)
    writeFont(font, filename)
    return


def run(filename):
    checkAndFix(filename)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 2:
        usage()
        return 1
    run(argv[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
