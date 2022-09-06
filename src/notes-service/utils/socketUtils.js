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

    // "get-note" - moje zdarzenie - pobieranie dokumentu
    socket.on("get-note", (noteId) => {
      const data = "";
      // WARNING sockte joins room for this note
      // jak w chatach żeby mogli wszsytcy pisac w jednym pokoju/chacie
      socket.join(noteId);

      // "load-note" - moje zdarzenie; wysyałnie danych z dokuemntu do klienta
      socket.emit("load-note", data);

      // "send-changes" zdarzenie z biblioteki quill- kopia gogle docs
      socket.on("send-changes", (delta) => {
        console.log("delta: ", delta);
        // wysyła do wszystkich tylko nie do nas zmiany
        // "receive-changes" - moja nazwa zdarzenia
        // socket.broadcast.emit("receive-changes", delta); //broadcastowo YOLO do wszystkich
        // to - wysłąnei zmian do specyficznego kanału
        socket.broadcast.to(noteId).emit("receive-changes", delta);
      });
    });

    socket.on("message", (message) => {
      console.log(`message from ${socket.id} : ${message}`);
    });

    socket.on("disconnect", () => {
      console.log(`socket ${socket.id} disconnect`);
    });
  });
};
