// https://youtu.be/DGmX1FDdLZE?t=157
// w folderze sarenka\src\frontend>
// npm install --save express
// npm install --save path

// node index.js

// bo clinet ma folder produkcyjny build i portrzebujemy serwrera expressa do serwisowania wlaśnie tego produkcyjnego folderu

const express = require("express");
// moduł żeby łatwiej zarządzac ścieżkami - ja os.join w pythonie
const path = require("path");

const app = express();

// raoute do serwisowania tego folderu build
app.get("*", (req, res) => {
  // sarenka\src\frontend\client\build\index.html, żeby nie wspisywać ściezki bezwzglednej
  const myPath = path.resolve(__dirname, "client", "build", "index.html");
  //WARNING   __dirname specjalna zmeinna Node.js do aktualnego folderu
  console.log("__dirname", __dirname);
  console.log("my path ", myPath);
  return res.sendFile(myPath);
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
