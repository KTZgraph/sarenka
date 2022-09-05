const socketIO = require('socket.io');

exports.sio = (server) => {
  return socketIO(server, {
    // oba działają
    transport: ['polling'],
    // transport: ['websocket'],
    cors: {
      // FIXME CORS
      origin: '*',
    },
  });
};

exports.connection = (io) => {
  io.on('connection', (socket) => {
    console.log('EEEEEEEEEEE');
    console.log('A user is connected');

    socket.on('message', (message) => {
      console.log(`message from ${socket.id} : ${message}`);
    });

    socket.on('disconnect', () => {
      console.log(`socket ${socket.id} disconnect`);
    });
  });
};
