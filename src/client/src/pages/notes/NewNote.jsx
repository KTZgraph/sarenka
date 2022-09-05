import Quill from "quill";
import "quill/dist/quill.snow.css";
import { useEffect, useRef } from "react";

// npm i quill
const NewNote = () => {
  const wrapperRef = useRef();

  useEffect(() => {
    const editor = document.createElement("div");
    wrapperRef.current.append(editor);
    new Quill(editor, { theme: "snow" });
  }, []);
  return <div id="container" ref={wrapperRef}></div>;
};

export default NewNote;
