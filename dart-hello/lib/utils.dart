import 'dart:io' show File, Directory;

// list files in dir
void list_files() async {
  var dir = Directory('/usr/local/bin');
  var entries = await Directory('/opt/flutter')
      .list(recursive: true, followLinks: true)
      .toList();
  print('all files and directories in $dir: ${entries.length}');

  var files_in_entries = entries.whereType<File>().toList();
  print('files in dir: $dir: ${files_in_entries.length}');
}
