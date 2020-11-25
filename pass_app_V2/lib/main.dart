import 'package:flutter/material.dart';
import 'Screens/MainScreen.dart';

void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
          canvasColor: Colors.grey[900],
          visualDensity: VisualDensity.adaptivePlatformDensity),
      home: MyHomePage(),
    ),
  );
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _obscureText = true;

  void update(callback) {
    this.setState(() {
      callback();
    });
  }

  void unlock() {
    _obscureText = !_obscureText;
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      child: Scaffold(
        body: Center(
          child: Column(
            children: [
              Container(
                padding: EdgeInsets.only(top: 90),
                child: Text(
                  'Iniciar Sessão',
                  style: TextStyle(
                    color: Colors.grey[300],
                    fontSize: 25,
                  ),
                ),
              ),
              Container(
                padding: EdgeInsets.only(top: 50, right: 20, left: 20),
                child: TextField(
                  cursorColor: Colors.blueGrey,
                  style: TextStyle(color: Colors.cyan[200]),
                  decoration: InputDecoration(
                    labelText: 'Nome de Utilizador',
                    labelStyle: TextStyle(
                      color: Colors.blueGrey,
                      fontSize: 16,
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.blueGrey),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.cyan[200]),
                    ),
                  ),
                ),
              ),
              Container(
                padding: EdgeInsets.only(
                  top: 30,
                  right: 20,
                  left: 20,
                ),
                child: TextField(
                  cursorColor: Colors.blueGrey,
                  style: TextStyle(color: Colors.cyan[200]),
                  decoration: InputDecoration(
                    labelText: 'Palavra Passe',
                    labelStyle: TextStyle(
                      color: Colors.blueGrey,
                      fontSize: 16,
                    ),
                    suffixIcon: IconButton(
                      icon: (_obscureText
                          ? Icon(Icons.lock)
                          : Icon(Icons.lock_open)),
                      color: Colors.blueGrey,
                      onPressed: () => update(unlock),
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.blueGrey),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.blueGrey),
                    ),
                  ),
                  obscureText: _obscureText,
                ),
              ),
              Container(
                margin: EdgeInsets.only(top: 5),
                child: Row(
                  children: [
                    Expanded(
                      child: Container(
                        margin: EdgeInsets.fromLTRB(10, 25, 10, 20),
                        child: Divider(
                          thickness: 5,
                          color: Colors.grey[500],
                        ),
                      ),
                    ),
                    Text(
                      "OU",
                      style: TextStyle(
                        fontSize: 15,
                        color: Colors.grey[500],
                      ),
                    ),
                    Expanded(
                      child: Container(
                        margin: EdgeInsets.fromLTRB(10, 25, 10, 20),
                        child: Divider(
                          thickness: 5,
                          color: Colors.grey[500],
                        ),
                      ),
                    )
                  ],
                ),
              ),
              Container(
                margin: EdgeInsets.only(
                  top: 10,
                  right: 10,
                  left: 10,
                ),
                child: RaisedButton(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(45),
                  ),
                  splashColor: Colors.grey,
                  color: Colors.grey[700],
                  child: Padding(
                    padding: EdgeInsets.only(
                      top: 10,
                      bottom: 10,
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Image(
                          image: AssetImage('assets/google_logo.png'),
                          height: 35,
                        ),
                        Padding(
                          padding: EdgeInsets.only(left: 10),
                          child: Text(
                            'Iniciar sessão com Google',
                            style: TextStyle(
                              color: Colors.grey[900],
                              fontSize: 23,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => MainScreen()),
                    );
                  },
                ),
              ),
              Container(
                color: Colors.transparent,
                padding: EdgeInsets.only(top: 40),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Expanded(
                      child: Container(
                        height: 40,
                        padding: EdgeInsets.only(
                          left: 20,
                          right: 20,
                        ),
                        child: RaisedButton(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(15)),
                          splashColor: Colors.grey[800],
                          color: Colors.black,
                          child: Text(
                            'Registar-se',
                            style: TextStyle(
                              color: Colors.grey,
                              fontSize: 16,
                            ),
                          ),
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => MainScreen()),
                            );
                          },
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
      onTap: () {
        FocusScope.of(context).requestFocus(new FocusNode());
      },
    );
  }
}
