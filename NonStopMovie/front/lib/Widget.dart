  import 'package:flutter/material.dart';
  
  
  Widget sliderhome() {
    return Container(
              height: 200,
              child: PageView.builder(reverse: true,itemCount: 3,itemBuilder: (context, index) {
                return Container(
                  decoration: BoxDecoration( color: Colors.black, borderRadius: BorderRadius.circular(10),),
                  margin: EdgeInsets.all(8),
                  height: 200,
                  
                );
              },),
            );
  }
  
  Widget slidernewproduct(context) {
    return Container(
              height: 200,
              width:MediaQuery.of(context).size.width,
              child: PageView.builder(scrollDirection: Axis.horizontal,reverse: true,itemCount: 10,itemBuilder: (context, index) {
                return Container(
                  decoration: BoxDecoration( color: Colors.black, borderRadius: BorderRadius.circular(10),),
                  margin: EdgeInsets.all(8),
                  height: 200,
width:50,
                  
                );
              },),
            );
  }
  Widget slidercategories() {
    return Container(
              height: 200,
              child: PageView.builder(scrollDirection: Axis.horizontal,reverse: true,itemCount: 10,itemBuilder: (context, index) {
                return Container(
                  decoration: BoxDecoration( color: Colors.black, borderRadius: BorderRadius.circular(10),),
                  margin: EdgeInsets.all(8),
                  height: 200,
                  width: MediaQuery.of(context). size.width / 0.8,
                  
                );
              },),
            );
  }

class headerText extends StatelessWidget {
  const headerText({
    super.key,
   
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Padding(
          padding: const EdgeInsets.only(left: 8),
          child: const Text( 'New Products',style: TextStyle(fontSize: 15,fontWeight: FontWeight.bold),),
        ),
         Padding(
          padding: const EdgeInsets.only(right: 8),
          child: const Text('More',style: TextStyle(fontSize: 15,fontWeight: FontWeight.bold),),
        ),
      ],
    );
  }}