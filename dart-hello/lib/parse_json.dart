import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:version/version.dart';
import 'dart:io' show File;

class Person {
  late final String name;
  late final int age;
  Person(this.name, this.age);
  Person.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    age = json['age'] as int;
  }
  Person.fromJsonString(String jsonString) {
    Map<String, dynamic> jsonMap = jsonDecode(jsonString);
    name = jsonMap['name'];
    age = jsonMap['age'] as int;
  }
}

void t1() {
  var jsonString = r'{"name": "ruby","age":19}';
  Map<String, dynamic> jsonMap = json.decode(jsonString);
  var p = Person.fromJson(jsonMap);
  print('${p.name}, ${p.age}');
  p = Person.fromJsonString(jsonString);
  print('${p.name}, ${p.age}');
}

class Album {
  final int userId;
  final int id;
  final String title;

  const Album({
    required this.userId,
    required this.id,
    required this.title,
  });

  factory Album.fromJson(Map<String, dynamic> json) {
    return Album(
      userId: json['userId'],
      id: json['id'],
      title: json['title'],
    );
  }
}

class Restaurant {
  Restaurant({required this.name, required this.cuisine, this.yearOpened});
  final String name; // non-nullable
  final String cuisine; // non-nullable
  final int? yearOpened; // nullable

  factory Restaurant.fromJson(Map<String, dynamic> data) {
    final name = data['name'] as String; // cast as non-nullable String
    final cuisine = data['cuisine'] as String; // cast as non-nullable String
    final yearOpened = data['year_opened'] as int?; // cast as nullable int
    return Restaurant(name: name, cuisine: cuisine, yearOpened: yearOpened);
  }
}

Future<void> parse_json_from_url() async {
  var url = Uri.parse(
      'https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json');
  var resp = await http.get(url);
  var json_data = json.decode(resp.body);
}

void parse_json3() {
  var file_str = File('releases_linux.json').readAsStringSync();
  var json_data = json.decode(file_str);
  final currentRelease = json_data['current_release'];
  final releases = json_data['releases'];
  print(releases[0]);
  print(currentRelease);
}

void parse_json() {
  print('------');
  var file_str = File('releases_linux.json').readAsStringSync();
  var json_data = json.decode(file_str);
  final currentRelease = json_data['current_release'] as Map<String, dynamic>;
  final releases = json_data['releases'];

  var base_url =
      'https://storage.googleapis.com/flutter_infra_release/releases';
  var latest_beta_url;
  var latest_stable_url;
  var latest_stable_version = '0.0.0';
  var latest_beta_version = '0.0.0';
  for (final release in releases) {
    var archive = release['archive'];
    var channel = release['channel'];
    var version;
    try {
      version = Version.parse(release['version']);
    } catch (e) {
      continue;
    }
    if (channel == 'beta' && version > Version.parse(latest_beta_version)) {
      latest_beta_version = release['version'];
      latest_beta_url = '${base_url}/${archive}';
    } else if (channel == 'stable' &&
        version > Version.parse(latest_stable_version)) {
      latest_stable_version = release['version'];
      latest_stable_url = '${base_url}/${archive}';
    }
  }

  print(latest_stable_url);
  print(latest_beta_url);
}

void parse_json2() {
  var file_str = File('releases_linux.json').readAsStringSync();
  var json_data = json.decode(file_str);
  final currentRelease = json_data['current_release'] as Map<String, dynamic>;
  final releases = json_data['releases'] as List<dynamic>;
  var base_url =
      'https://storage.googleapis.com/flutter_infra_release/releases';
  var latest_beta_url;
  var latest_stable_url;
  List<String> arr = [];
  print(releases.length);
  for (var i = 0; i < releases.length; i++) {
    var archive = releases[0]['archive'];
    var channel = releases[0]['channel'];
    if (channel == 'beta') {
      latest_beta_url = '${base_url}/${archive}';
      arr.add('$i beta');
    }
    if (channel == 'stable') {
      latest_stable_url = '${base_url}/${archive}';
      arr.add('$i stable');
    }
  }
  print(latest_stable_url);
  print(latest_beta_url);
  print(arr);
  print(arr.takeWhile((x) => x.contains('stable')));
}
