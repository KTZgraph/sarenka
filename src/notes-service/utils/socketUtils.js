const socketIO = require("socket.io");

exports.sio = (server) => {
  return socketIO(server, {
    // oba działają
    transport: ["polling"],
    // transport: ['websocket'],
    cors: {
      // FIXME CORS
      // origin: '*',
      origin: "http://localhost:3000",
      methods: ["GET", "POST"],
    },
  });
};

exports.connection = (io) => {
  io.on("connection", (socket) => {
    console.log("A user is connected");

    // "send-changes" zdarzenie z biblioteki quill- kopia gogle docs
    socket.on("send-changes", (delta) => {
      console.log("delta: ", delta);
    });

    socket.on("message", (message) => {
      console.log(`message from ${socket.id} : ${message}`);
    });

    socket.on("disconnect", () => {
      console.log(`socket ${socket.id} disconnect`);
    });
  });
};
