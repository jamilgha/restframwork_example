import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_application_1/Models/api_service.dart';
import 'package:flutter_application_1/Models/model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;
class MovieFetch_List extends StatefulWidget {
  const MovieFetch_List({super.key});

  @override
  State<MovieFetch_List> createState() => _MovieFetch_ListState();
}

class _MovieFetch_ListState extends State<MovieFetch_List> {
// List<MovieList> _userModel = [];
//
//   getSliders(){
//
//     if (_userModel.length == 0) {
//       var url = "http://g858h5bxu.pythonanywhere.com/api/movie-list/?format=json";
//       // var url = "http://127.0.0.1:8000/api/movie-list/";
//
//       http.get(Uri.parse(url)).then((response) {
//         print(response.statusCode);
//         print(response.body);
//
//         if (response.statusCode == 200) {
//           List jsonResponse = convert.jsonDecode(response.body);
//
//           for (int i = 0; i < jsonResponse.length; i++) {
//             setState(() {
//               _userModel.add(MovieList(
//                 id: jsonResponse[i]['id'],
//                 movieTitle: jsonResponse[i]['MovieList'],
//                 movieBudget: jsonResponse[i]['movieBudget'],
//                 movieHomepage: jsonResponse[i]['movieHomepage'],
//                 movieOverview: jsonResponse[i]['movieOverview'],
//                 movieVotesAvg: jsonResponse[i]['movieVotesAvg'],
//                 movieVotesCount: jsonResponse[i]['movieVotesCount'],
//                 movieReleaseDate: jsonResponse[i]['movieReleaseDate'],
//                 moviePoster: jsonResponse[i]['moviePoster'],
//                 linkPlay: jsonResponse[i]['linkPlay'],
//                 moviegender: jsonResponse[i]['moviegender'],
//               ));
//             });
//           }
//         }
//       });
//     }
//
//   }
  late Future<List<Movie>> _futureMovies;
String Base_url='http://g858h5bxu.pythonanywhere.com';
  Future<List<Movie>> fetchMovies() async {


final Response=await http.get(Uri.parse('http://g858h5bxu.pythonanywhere.com/api/movie-list/?format=json'));
if (Response.statusCode == 200) {
  List<dynamic> jsonData = json.decode(Response.body);
  return jsonData.map((item) => Movie.fromJson(item)).toList();
} else {
  throw Exception('Failed to load data');
}
  }
@override
  void initState() {
    // TODO: implement initState
    super.initState();
    _futureMovies = fetchMovies();

}
  Future<void> _refreshMovies() async {
    setState(() {
      _futureMovies = fetchMovies();
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Flutter API Example'),
      ),
      body: FutureBuilder<List<Movie>>(
        future: _futureMovies,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(
              child: CircularProgressIndicator(),
            );
          } else if (snapshot.hasError) {
            return Center(
              child: Text('Error: ${snapshot.error}'),
            );
          } else {
            List<Movie>? movies = snapshot.data;
            return RefreshIndicator(
              onRefresh:_refreshMovies,

              child: ListView.builder(
                scrollDirection: Axis.vertical,
                itemCount: movies!.length,
                itemBuilder: (context, index) {
                  return Container(
                    height: 240,
                    width: 160,
                    margin: EdgeInsets.all(8),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(

                          height: 200,
                          width: 150,
                          // width: 200,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(15),
                            image: DecorationImage(

                                fit: BoxFit.cover,
                                image: NetworkImage(Base_url+movies[index].moviePoster)),
                          ),
                          // child: Image.network(Base_url+movies[index].moviePoster)
                        ),
                        Text(movies[index].movieTitle,style: TextStyle(fontWeight: FontWeight.bold,fontSize: 10),),
                      ],
                    ),
                  );
                },
              ),
            );
          }
        },
      ),
    );
  }
}
