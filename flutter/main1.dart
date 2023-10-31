import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    return MaterialApp( //단위 LP
      home: Scaffold(
        appBar: AppBar( title: Text("앱임")),
        body: Align(
          alignment: Alignment.bottomLeft,
          child: Container(
            width: double.infinity, height: 50, margin: EdgeInsets.fromLTRB(0, 30, 0, 0),
            decoration:
              BoxDecoration( //decoration 쓰면 앞에서 컬러못씀
                  border: Border.all(color: Colors.black),
                  color: Colors.blue,

              )
          ),
        ),
        bottomNavigationBar: BottomAppBar(
          height: 80,
          child:Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [Icon(Icons.phone),Icon(Icons.message),Icon(Icons.contact_mail)]
          )
        ),
        ),
      );//Image.asset('android.jpg')//Icon(Icons.shop)

  }
}
