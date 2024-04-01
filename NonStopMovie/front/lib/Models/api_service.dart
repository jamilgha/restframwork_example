// import 'dart:developer';
//
// import 'package:http/http.dart' as http;
// import 'package:flutter_application_1/constants.dart';
// import 'package:flutter_application_1/Models/model.dart';
//
// class ApiService {
//   Future<List<MovieList>?> getUsers() async {
//     try {
//       var url = Uri.parse(ApiConstants.baseUrl);
//       var response = await http.get(url);
//       if (response.statusCode == 200) {
//         List<MovieList> _model = movieListFromJson(response.body);
//         return _model;
//       }
//     } catch (e) {
//       log(e.toString());
//     }
//   }
// }