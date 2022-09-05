// https://www.youtube.com/watch?v=iRaelG7v0OU
import { useCallback } from "react";
import Quill from "quill";
import "quill/dist/quill.snow.css";

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
  const wrapperRef = useCallback((wrapper) => {
    if (wrapper == null) return;

    wrapper.innerHTML = "";

    const editor = document.createElement("div");
    wrapper.append(editor);

    new Quill(editor, { theme: "snow", modules: { toolbar: TOOLBAR_OPTIONS } });
  }, []);

  return (
    <div className="new-note">
      <div ref={wrapperRef} className="new-note__container"></div>
    </div>
  );
};

export default NewNote;
