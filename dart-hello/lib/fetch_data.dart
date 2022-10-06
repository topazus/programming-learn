import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:requests/requests.dart';
// use http package to fetch data from the internet
Future<http.Response> fetchAlbum() {
  return http.get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));
}

void fetch()async{
  var response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/todos/1'));
  print(response.body);
}
void fetch2()async{
  var data = {'title': 'My first post'};
  var resp = await http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    headers: {'Content-Type': 'application/json; charset=UTF-8'},
    body: json.encode(data),
  );
  print(resp.body);
}
// use requests package to fetch data from the internet

void request_data()async{
  var r = await Requests.post(
  'https://reqres.in/api/users',
  body: {
    'userId': 10,
    'id': 91,
    'title': 'aut amet sed',
  },
  bodyEncoding: RequestBodyEncoding.FormURLEncoded);

r.raiseForStatus();
dynamic json = r.json();
print(json!['id']);
}
