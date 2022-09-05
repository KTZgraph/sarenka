import Quill from "quill";
import "quill/dist/quill.snow.css";
import { useEffect } from "react";

// npm i quill
const NewNote = () => {
  useEffect(() => {
    new Quill("#container", { theme: "snow" });
  }, []);
  return <div id="container"></div>;
};

export default NewNote;
