import 'package:requests/requests.dart';
import 'package:http/http.dart' as http;
void get_github_api_data()async{
  // get commits in a github repo

var commits_data=await http.get(Uri('https://api.github.com/repos/flutter/flutter/commits'));
}
