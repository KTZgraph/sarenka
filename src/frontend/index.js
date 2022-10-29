// https://youtu.be/DGmX1FDdLZE?t=157
/*
Dlaczego seriwsujemy apkę Reacta z serverem Node.js express
- it's because we want to store our access and refresh tokens inside of the HTTP only cookies
so with the cookies you're gonna have your React Client and the you're gonna have your bakckend api which in this case is gonna be express that's serving the app and 
then we're gonna have cookies 
Now the cookies, the behaviour of then is on your request they get sent into requests automatically but the domains have to be the exact same unsless you 
do some differeny changes to the options of the cookies like let's say set the same site property or the same site option rather to sopmething like None and then do some
other things inside of your fetch requests so you can sort get around that but for the most part of the default behaviour is that browser will not send along the cookies if 
the domain is different at the desctination 
-> So that we have the express server serving the React Client and then that way the cookies can go back and forth and then the express server it;s going to be able to parse the
values of those cookies
The browser won't be able to because we're gonna have the HTTP only flag set to true - meaning that javascript can't read the value on the browser
--> but of course on the server on our express server it will be able to we'll be able to parse those cvalues and then send any authorized requests that we need to because we're 
using JSON WEB TOKEN AUTHENTICATION the way that we make authorized requests is we use the authorization header where then we pass in the auth header type do  things like
BEARER and the your access token
So that's how we do the authorized requests which is something that we saw in the last video  https://www.youtube.com/watch?v=rxRYEXBmM88&t=8s

So that is kinf of how we manage these values and how we keep them nice and secure
*/

// w folderze sarenka\src\frontend>
// npm install --save express
// npm install --save path
// node index.js

// żeby dynamicznie widac było zmiany
// npm install --save nodemon
// zmodyfikowac plik sarenka\src\frontend\package.json
// npm start

// bo clinet ma folder produkcyjny build i portrzebujemy serwrera expressa do serwisowania wlaśnie tego produkcyjnego folderu

// npm i --save dotenv # do zmiennych środowiskowych

const express = require("express");

// npm install --save cookie-parser do łądneijszego parsowanie cookie
const cookieParser = require("cookie-parser");

// moduł żeby łatwiej zarządzac ścieżkami - ja os.join w pythonie
const path = require("path");

// dodanie biblioteki, zeby zmiene srodkowiskowe działały
require("dotenv").config();

// pobieram swoje routery, po imporcie dotenv żeby mieć pewnosć, że nie ma problemu z pobieaniem wartości zmiennych środkowiskowcyh
const registerRoute = require("./routes/auth/register");
const loginRoute = require("./routes/auth/login");
const meRoute = require("./routes/auth/me");
const logoutRoute = require("./routes/auth/logout");

const app = express();

// dodanie tego middlewara pozwala na działanie  router.post("/api/users/register" z sarenka\src\frontend\routes\auth\register.js
app.use(express.json());
// npm install --save cookie-parser
app.use(cookieParser());

// include rejestracja moich routes
app.use(registerRoute);
app.use(loginRoute);
app.use(meRoute);
app.use(logoutRoute);

// dodanie plików statycznych
app.use(express.static("client/build"));

// raoute do serwisowania tego folderu build
app.get("*", (req, res) => {
  // sarenka\src\frontend\client\build\index.html, żeby nie wspisywać ściezki bezwzglednej
  const myPath = path.resolve(__dirname, "client", "build", "index.html");
  //WARNING   __dirname specjalna zmeinna Node.js do aktualnego folderu
  //   console.log("__dirname", __dirname);
  //   console.log("my path ", myPath);
  return res.sendFile(myPath);
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
