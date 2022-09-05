// https://www.youtube.com/watch?v=SMubOngCCmw

const http = require('http');
const dotenv = require('dotenv');
const cors = require('cors');

dotenv.config();
const express = require('express');
const app = express();
const socketUtils = require('./utils/socketUtils');

const server = http.createServer(app);
// instancja potrzebnma do sockketu
const io = socketUtils.sio(server);
socketUtils.connection(io);

// middleware
const socketIOMiddleware = (req, res, next) => {
  req.io = io;
  next();
};

//cors middleware
app.use(cors());

// ROUTES
app.use('/api/v1/hello', socketIOMiddleware, (req, res) => {
  req.io.emit('message', `Hello, ${req.originalUrl}`);
  res.send('hello world from io express');
});

//LISTEN the server
const port = process.env.PORT || 8000;
server.listen(port, () => {
  console.log(`App running on port ${port}...`);
});
