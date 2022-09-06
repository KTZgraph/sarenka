// https://www.youtube.com/watch?v=iRaelG7v0OU
import { useCallback, useEffect, useState } from "react";
import Quill from "quill";
import "quill/dist/quill.snow.css";

// socket.io-client connection
import { io } from "socket.io-client";

import "./NewNote.scss";

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

  const wrapperRef = useCallback((wrapper) => {
    if (wrapper == null) return;

    wrapper.innerHTML = "";

    const editor = document.createElement("div");
    wrapper.append(editor);

    const q = new Quill(editor, {
      theme: "snow",
      modules: { toolbar: TOOLBAR_OPTIONS },
    });

    setQuill(q);
  }, []);

  return (
    <div className="new-note">
      <div ref={wrapperRef} className="new-note__container"></div>
    </div>
  );
};

export default NewNote;
