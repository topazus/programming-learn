import 'dart:convert';
import 'package:version/version.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:dart_hello/flutter_download.dart' as parse_flutter;
import 'package:deep_pick/deep_pick.dart';
import 'package:dart_hello/t1.dart' as t1;

void main(List<String> arguments) async {
  print(parse_flutter.storageUrl);
  final env = Platform.environment;
  // print(env);
  print(env['PATH']);
  print(parse_flutter.getGoogleReleaseUrl());

  var url = Uri.https('example.com', 'whatsit/create');
  var response =
      await http.post(url, body: {'name': 'doodle', 'color': 'blue'});
  print('Response status: ${response.statusCode}');
  print('Response body: ${response.body}');

  print(await http.read(Uri.https('google.com')));
  fetch2();
}

void fetch2() async {
  var data = {'title': 'My first post'};
  var resp = await http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    headers: {'Content-Type': 'application/json; charset=UTF-8'},
    body: json.encode(data),
  );
  print(resp.body);
}
