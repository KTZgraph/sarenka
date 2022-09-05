// https://www.youtube.com/watch?v=iRaelG7v0OU
import { useCallback } from "react";
import Quill from "quill";
import "quill/dist/quill.snow.css";

import "./NewNote.scss";

// npm i quill
const NewNote = () => {
  const wrapperRef = useCallback((wrapper) => {
    if (wrapper == null) return;

    wrapper.innerHTML = "";

    const editor = document.createElement("div");
    wrapper.append(editor);

    new Quill(editor, { theme: "snow" });
  }, []);

  return (
    <div className="new-note">
      <div ref={wrapperRef} className="new-note__container"></div>
    </div>
  );
};

export default NewNote;
