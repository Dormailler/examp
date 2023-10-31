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
        appBar: AppBar(),
        body: Container(
          height: 150,
          padding: EdgeInsets.all(10),
          child: Row(
            children: [
              Image.asset('android.jpg',width: 150,),
              Container(

                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('팝니다', style: TextStyle(fontWeight: FontWeight.bold)),
                    Text('금호동 3가'),
                    Text('7000원'),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        Icon(Icons.favorite),
                        Text('5'),
                      ],
                    ),

                  ],
                ),
              )
            ],
          ),
        ),
        // body: Row(
        //   children: [
        //     Expanded(child: Container(color: Colors.blue,), flex: 3,),
        //     Container(width: 100,color: Colors.green,)
        //     // Flexible(child: Container(color: Colors.blue,), flex: 3,),
        //     // Flexible(child: Container(color: Colors.red,), flex: 3,),
        //     // Flexible(child: Container(color: Colors.black,), flex: 3,),
        //   ],
        // ),
        // appBar: AppBar(leading: Icon(Icons.star),actions: [Icon(Icons.star)],), //style : TextStyle() -> Color.fromRGBO Color(0xffff0000) fontWeight: FontWeight.w700
        // body: SizedBox(
        //   child: ElevatedButton(
        //     child: Text('글자'),
        //     onPressed: (){},
        //
        //   ),
        // ),

        // body: Align(
        //   alignment: Alignment.bottomLeft,
        //   child: Container(
        //     width: double.infinity, height: 50, margin: EdgeInsets.fromLTRB(0, 30, 0, 0),
        //     decoration:
        //       BoxDecoration( //decoration 쓰면 앞에서 컬러못씀
        //           border: Border.all(color: Colors.black),
        //           color: Colors.blue,
        //
        //       )
        //   ),
        // ),
        // bottomNavigationBar: BottomAppBar(
        //   height: 80,
        //   child:Row(
        //       mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        //       children: [Icon(Icons.phone),Icon(Icons.message),Icon(Icons.contact_mail)]
        //   )
        // ),
        ),
      );//Image.asset('android.jpg')//Icon(Icons.shop)

  }
}
