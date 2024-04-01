// // To parse this JSON data, do
// //
// //     final movieList = movieListFromJson(jsonString);
//
// import 'dart:convert';
//
// List<MovieList> movieListFromJson(String str) => List<MovieList>.from(json.decode(str).map((x) => MovieList.fromJson(x)));
//
// String movieListToJson(List<MovieList> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));
//
// class MovieList {
//   int id;
//   String movieTitle;
//   int movieBudget;
//   String movieHomepage;
//   String movieOverview;
//   String movieVotesAvg;
//   int movieVotesCount;
//   DateTime movieReleaseDate;
//   String moviePoster;
//   String linkPlay;
//   int moviegender;
//
//   MovieList({
//     required this.id,
//     required this.movieTitle,
//     required this.movieBudget,
//     required this.movieHomepage,
//     required this.movieOverview,
//     required this.movieVotesAvg,
//     required this.movieVotesCount,
//     required this.movieReleaseDate,
//     required this.moviePoster,
//     required this.linkPlay,
//     required this.moviegender,
//   });
//
//   factory MovieList.fromJson(Map<String, dynamic> json) => MovieList(
//     id: json["id"],
//     movieTitle: json["movie_title"],
//     movieBudget: json["movie_budget"],
//     movieHomepage: json["movie_homepage"],
//     movieOverview: json["movie_overview"],
//     movieVotesAvg: json["movie_votes_avg"],
//     movieVotesCount: json["movie_votes_count"],
//     movieReleaseDate: DateTime.parse(json["movie_release_date"]),
//     moviePoster: json["movie_poster"],
//     linkPlay: json["Link_play"],
//     moviegender: json["moviegender"],
//   );
//
//   Map<String, dynamic> toJson() => {
//     "id": id,
//     "movie_title": movieTitle,
//     "movie_budget": movieBudget,
//     "movie_homepage": movieHomepage,
//     "movie_overview": movieOverview,
//     "movie_votes_avg": movieVotesAvg,
//     "movie_votes_count": movieVotesCount,
//     "movie_release_date": movieReleaseDate.toIso8601String(),
//     "movie_poster": moviePoster,
//     "Link_play": linkPlay,
//     "moviegender": moviegender,
//   };
// }

class Movie {
  final int id;
  final String movieTitle;
  final int movieBudget;
  final String movieHomepage;
  final String movieOverview;
  final double movieVotesAvg;
  final int movieVotesCount;
  final DateTime movieReleaseDate;
  final String moviePoster;
  final String linkPlay;
  final int movieGender;

  Movie({
    required this.id,
    required this.movieTitle,
    required this.movieBudget,
    required this.movieHomepage,
    required this.movieOverview,
    required this.movieVotesAvg,
    required this.movieVotesCount,
    required this.movieReleaseDate,
    required this.moviePoster,
    required this.linkPlay,
    required this.movieGender,
  });

  factory Movie.fromJson(Map<String, dynamic> json) {
    return Movie(
      id: json['id'],
      movieTitle: json['movie_title'],
      movieBudget: json['movie_budget'],
      movieHomepage: json['movie_homepage'],
      movieOverview: json['movie_overview'],
      movieVotesAvg: double.parse(json['movie_votes_avg']),
      movieVotesCount: json['movie_votes_count'],
      movieReleaseDate: DateTime.parse(json['movie_release_date']),
      moviePoster: json['movie_poster'],
      linkPlay: json['Link_play'],
      movieGender: json['moviegender'],
    );
  }
}