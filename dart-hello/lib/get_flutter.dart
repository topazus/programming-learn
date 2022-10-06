import 'dart:convert';
import 'dart:io';

void current_flutter_url() async {
  var current_stable_url;
  var current_beta_url;
  var file = await File('releases_linux.json').readAsString();

  var jsonData = jsonDecode(file);
  var base_url = jsonData['base_url'];
  var current_stable_hash = jsonData['current_release']['stable'];
  var current_beta_hash = jsonData['current_release']['beta'];

  var releases = jsonData['releases'];
  for (final x in releases) {
    if (x['hash'] == current_stable_hash) {
      current_stable_url = '${base_url}/${x['archive']}';
    }
    if (x['hash'] == current_beta_hash) {
      current_beta_url = '${base_url}/${x['archive']}';
    }
  }
  print('$current_stable_url, $current_beta_url');
}
