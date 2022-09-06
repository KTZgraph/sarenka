// https://www.youtube.com/watch?v=iRaelG7v0OU
import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Quill from "quill";
import "quill/dist/quill.snow.css";

// socket.io-client connection
import { io } from "socket.io-client";

import "./NewNote.scss";

const SAVE_INTERVAL_MS = 2000;
const TOOLBAR_OPTIONS = [
  [{ header: [1, 2, 3, 4, 5, 6, false] }],
  [{ font: [] }],
  [{ list: "ordered" }, { list: "bullet" }],
  ["bold", "italic", "underline"],
  [{ color: [] }, { background: [] }],
  [{ script: "sub" }, { script: "super" }],
  [{ align: [] }],
  ["image", "blockquote", "code-block"],
  ["clean"],
];

// npm i quill
const NewNote = () => {
  const { noteId } = useParams();
  const [socket, setSocket] = useState();
  const [quill, setQuill] = useState();

  useEffect(() => {
    const s = io("http://localhost:3001");
    setSocket(s);

    return () => {
      // NIe socket z useState
      s.disconnect();
    };
  }, []);

  // ---------- ustawienie userów w pokoju o id dokumentu, zeby nie modyfikowac wszsytkich dokumentów o rożnych idkach
  useEffect(() => {
    if (socket == null || quill == null) return;

    // tylko raz nasłuchujemy na zdarzenie dlatego socket.once
    socket.once("load-note", (note) => {
      // serwer raz wysyła wartośc z bazy notatki - quill aktualizuje edytor
      quill.setContents(note);
      // żeby mozna było edytować notatkę w edytorze
      quill.enable();
    });

    // "get-note" - nazwa mojego zdarzenia, id potrzebne do podłaczenia go do pokoju
    socket.emit("get-note", noteId);
  }, [socket, quill, noteId]);

  // ----------- zapisywanie dokumentu do bazy
  useEffect(() => {
    if (socket == null || quill == null) return;

    // autoamtyczne zapisywanie dokumentu co kilka sekund
    const interval = setInterval(() => {
      // "save-note" - moje zdarzenie z backendu
      socket.emit("save-note", quill.getContents());
    }, SAVE_INTERVAL_MS);

    // na końcu czyścimy interval
    return () => {
      clearInterval(interval);
    };
  }, [socket, quill]);

  //--------------- odbieranie danych broadcastowo z serwera
  useEffect(() => {
    // do detekcji zmian, jeśli kiedykolwiek quill się zmieni

    //socket i qull na początku sa niezdefiniowane
    if (socket == null || quill == null) return;
    // https://quilljs.com/docs/api/#text-change
    // "text-change" zdarzenie z biblioteki
    const handler = (delta) => {
      // aktualizacja dokumentu o to co wysłał serwer
      quill.updateContents(delta);
    };

    // "receive-changes", - moja nazwa zdarzenia z serwera który rozsyła dane
    socket.on("receive-changes", handler);

    return () => {
      // czyszczenie gdy wychodzimy
      socket.off("receive-changes", handler);
    };
    // useEffect tutaj zalezy od socket i quill
  }, [socket, quill]);

  //------------ wysyałnie delty - zmian w dokumencie
  useEffect(() => {
    // do detekcji zmian, jeśli kiedykolwiek quill się zmieni

    //socket i qull na początku sa niezdefiniowane
    if (socket == null || quill == null) return;
    // https://quilljs.com/docs/api/#text-change
    // "text-change" zdarzenie z biblioteki
    const handler = (delta, oldDelta, source) => {
      if (source !== "user") return;
      // delta mała porcja danych która się zmienia
      socket.emit("send-changes", delta);
    };
    quill.on("text-change", handler);

    return () => {
      // czyszczenie gdy wychodzimy
      quill.off("text-change", handler);
    };
    // useEffect tutaj zalezy od socket i quill
  }, [socket, quill]);

  // edytor
  const wrapperRef = useCallback((wrapper) => {
    if (wrapper == null) return;

    wrapper.innerHTML = "";

    const editor = document.createElement("div");
    wrapper.append(editor);

    const q = new Quill(editor, {
      theme: "snow",
      modules: { toolbar: TOOLBAR_OPTIONS },
    });

    // edytor niedostępny dopóki nie ma danych
    q.disable(); // albo q.enable(false)
    q.setText("Loading...");

    setQuill(q);
  }, []);

  return (
    <div className="new-note">
      <div ref={wrapperRef} className="new-note__container"></div>
    </div>
  );
};

export default NewNote;
