import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_application_1/Widget.dart';
import 'package:flutter_application_1/home.dart';
import 'package:flutter_application_1/movieFetch.dart';
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(

        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MovieFetch_List(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});




  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {

    return SafeArea(
      child: Scaffold(
        // appBar: AppBar(

        //   backgroundColor: Theme.of(context).colorScheme.inversePrimary,

        //   title: Text('Cash Jeans'),
        // ),
        body: Center(

          child: Column(

            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              sliderhome(),
              headerText(),
              slidernewproduct(context),
              headerText(),
              slidercategories()

            ],
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed:() {

          },
          tooltip: 'Increment',
          child: const Icon(Icons.add),
        ), // This trailing comma makes auto-formatting nicer for build methods.
      ),
    );
  }


}
