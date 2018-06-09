var express = require("express");
var mysql = require('mysql');
var bodyParser = require("body-parser");
var HashMap = require('hashmap');
var conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'my_db'
});
var app = express();
const PORT = 3000;
var map = new HashMap();

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

conn.connect(function(err) {
  if (!err) {
    console.log("Database is connect");
  } else {
    console.log("Error");
  }
});

app.post("/fuel", function(req, res) {
  console.log(req.body.name, req.body.cate, req.body.place, req.body.date, req.body.price);
  conn.query("INSERT INTO inform VALUES (?,?,?,?,?)", [req.body.name, req.body.cate, req.body.place, req.body.date, req.body.price], function(err, result) {
    if (err)
      console.log("Insert error");
    else {
      console.log("Insert success");
    }
  });
});

app.post("/addGroup", function(req, res) {
  console.log("I " + req.body.col);
  conn.query("SELECT * FROM groups WHERE name = ? ", [req.body.col], function(err, rows, fields) {
    if (err)
      console.log("Gruop col ERROR");
    else {
      if (rows.length == 0) {
        conn.query("INSERT INTO groups VALUES (?)", [req.body.col], function(err, result) {
          if (err)
            console.log("add col ERORR");
        });
        var query = 'ALTER TABLE car add ' + [req.body.col] + ' int not null default 0';
        conn.query(query, function(err, result) {
          if (err)
            console.log("add col ERORR");
        });
      }
    }
  });
});

app.post("/delGroup", function(req, res) {
  console.log("D " + req.body.col);
  conn.query("DELETE FROM groups WHERE name = ? ", [req.body.col], function(err, result) {
    if (err)
      console.log("Delete col ERROR");
  });
  var query = 'ALTER TABLE car drop ' + [req.body.col];
  conn.query(query, function(err, result) {
    if (err)
      console.log("Delete col ERROR");
  });
});

app.post("/upGroup", function(req, res) {
  console.log(req.body.map);
  var map = req.body.map;
  var query = 'UPDATE car SET ' + [req.body.name] + ' = ? WHERE name = ?';
  for (var i in map) {
    if (map.hasOwnProperty(i)) {
      conn.query(query, [map[i], i], function(err, result) {
        if (err)
          console.log("Update ERROR");
      });
    }
  }
});

app.get("/car/:gname", function(req, res) {
  var query = "SELECT name, " + [req.params.gname] + " FROM car";
  conn.query(query, function(err, rows, fields) {
    if (err)
      console.log("Select car ERORR");
    else {
      res.send(rows);
      console.log(rows);
    }
  });
});

app.get("/info/:car/:cate", function(req, res) {
  console.log(req.params.car + " " + req.params.cate);
  var str = req.params.cate;
  if (str.length < 3) {
    conn.query("SELECT * FROM inform WHERE name = ? ORDER BY date DESC ", [req.params.car], function(err, rows, fields) {
      if (err)
        console.log("select ERORR");
      else {
        res.send(rows);
        console.log(rows);
      }
    });
  }
  else{
    conn.query("SELECT * FROM inform WHERE name = ? AND cate = ? ORDER BY date DESC LIMIT 2", [req.params.car, req.params.cate], function(err, rows, fields) {
      if (err)
        console.log("select ERORR");
      else {
        res.send(rows);
        console.log(rows);
      }
    });
  }
});

app.get("/grp", function(req, res) {
  conn.query("SELECT name FROM groups", function(err, rows, fields) {
    if (err)
      console.log("group ERROR");
    else {
      res.send(rows);
      console.log(rows);
    }
  });
});

var server = app.listen(PORT, function() {
  console.log("Server is runnung on port 3000");
});
