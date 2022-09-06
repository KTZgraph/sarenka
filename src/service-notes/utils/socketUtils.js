const mongoose = require("mongoose");
require("dotenv").config();

// pobranie schema Notatki
const Note = require("../models/NoteModel");

// connect to db
mongoose.connect(process.env.MONGO_URI);

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
    socket.on("get-note", async (noteId) => {
      // ------------ ŁADOWANIE DOKUMENTU
      // pobieranie danych z bazy
      const note = await findOrCreateNote(noteId); //findOrCreateNote asynchroniczna
      // WARNING sockte joins room for this note
      // jak w chatach żeby mogli wszsytcy pisac w jednym pokoju/chacie
      socket.join(noteId);

      // "load-note" - moje zdarzenie; wysyałnie danych z dokuemntu do klienta
      // zwracam pole data z notatki
      socket.emit("load-note", note.data);

      // "send-changes" zdarzenie z biblioteki quill- kopia gogle docs
      socket.on("send-changes", (delta) => {
        // console.log("delta: ", delta);
        // wysyła do wszystkich tylko nie do nas zmiany
        // "receive-changes" - moja nazwa zdarzenia
        // socket.broadcast.emit("receive-changes", delta); //broadcastowo YOLO do wszystkich
        // to - wysłąnei zmian do specyficznego kanału
        socket.broadcast.to(noteId).emit("receive-changes", delta);
      });

      // ZAPISYWANIE DOKUMENTU, "save-note" - moje zdarzenie
      socket.on("save-note", async (data) => {
        // znajdź notatatkę po id i zaktualizuj, ale tylko data bo id zostaje przecież to samo
        await Note.findByIdAndUpdate(noteId, { data });
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

// funckje do zapisu
const defaultValue = "";

// funckja do pobierani dokumnetu z bazy lub tworzenia nowej notatki
async function findOrCreateNote(noteId) {
  // jak jakiś dziwny url bez idka notatki
  if (noteId == null) return;

  const note = await Note.findById(noteId); //trzeba użyć async function
  // jak notatki w bazie to  go zwróć
  if (note) return note;
  // jak notatki nie ma w bazie to nowy dokument
  return await Note.create({ _id: noteId, data: defaultValue });
}
