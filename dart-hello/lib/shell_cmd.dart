import 'dart:io';

import 'package:deep_pick/deep_pick.dart';

void run_cmd() async {
  var uname = Process.runSync('uname', ['-m']).stdout;
  var trim_uname = pick(uname).asStringOrThrow().trim();
  print(trim_uname);
  var gcc_version = (await Process.run('gcc', ['--version'])).stdout;
  print(gcc_version);
}
