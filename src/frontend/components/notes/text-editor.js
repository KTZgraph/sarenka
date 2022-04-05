import React, { useCallback, useEffect, useState } from "react";
import Quill from "quill";
import "quill/dist/quill.snow.css";
import { io } from "socket.io-client";

// import { useParams } from "react-router-dom"; // do wyciągania ID dokumentu
import { useRouter } from 'next/router'


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

const SAVE_INTERVAL_MS = 2000;

export default function TextEditor() {
  // const {id: documentId} = useParams()

  // const router = useRouter()
  // const { id: documentId } = router.query
  const documentId = 1; // TODO:

  const [socket, setSocket] = useState();
  const [quill, setQuill] = useState();

  // połaczenie z serwerem
  useEffect(() => {
    // połączenie z serwerem
    const s = io("http://localhost:8000");
    setSocket(s);

    // disconnect jak już nie potrzebujemy socketa
    return () => {
      // wyjdź z pokoju zanim się rozłączysz
      s.emit('leave', documentId)
      s.disconnect();
    };
  }, []);


// aktualizacja dokumentu - zapisywanie zmian co kilka sekund
useEffect(()=>{
  if(socket == null | quill == null) return

  const interval = setInterval(()=>{
    //  quill.getContents() wszystkie informacje jakie mam zapisac w bazie danych
    socket.emit('save_document', {'documentId': documentId ,'data': quill.getContents()})

  }, SAVE_INTERVAL_MS)

  // czysszczeni eintervala
  return() => {
    clearInterval(interval)
  }

}, [socket, quill])


// zmiany po dokuemntId
useEffect(() => {
  if(socket == null | quill == null) return

// próbuję się dostać do pokoju z dokumentem id


  // nasłuchiwanie zdarzenia z pythona tylko raz socket.once
  // 'load_document' zdarzenie z pythona
  socket.once('load_document', document => {
    // dokuemnt musi zostać zwrócony z serwera

    console.log('document: ', document)
    quill.setContents(document)
    // bo wcześniej blokuję edytor jeśli dokuemnt jest niezaładowany
    quill.enable()
  })

  // 'get_document' zdarzenie z pythona
  socket.emit('get_document', documentId)

}, [socket, quill, documentId])


  // obieranie danych z serwera
  useEffect(() => {
    if (socket == null || quill == null) return;

    // delta dane z serwera
    const handler = (delta) => {
      // aktualizacja danych w edytorze
      quill.updateContents(delta);
      // quill.getContents(delta); // podobno to jest do bazy
    };

    // tu zmiana do odbierania danych z serwera quill.on("text-change", handler);
    // 'receive-changes' zdarzenie z pythona emitowane
    // socket.on("receive-changes", handler);
    socket.on("receive-changes", handler);

    return () => {
      // tu zmiana do odbierania danych z serwera quill.off("text-change", handler);
      // 'receive-changes' zdarzenie z pythona emitowane
      // socket.off("receive-changes", handler);
      socket.off("receive-changes", handler);
    };
  }, [socket, quill]);


  // detekecja zmian z Quill
  useEffect(() => {
    // na początku uruchomienia są nullami
    if (socket == null || quill == null) return;

    const handler = (delta, oldDelta, source) => {
      // source - czy user zrobil zmiany, czy quill library
      if (source !== "user") return; //gdy zmiany NIE przez usera
      // wysyłanie zmian do serwera - wysyłanie wiadomosci z klienta do serwerra
      // 'send_changes' zdarzenie z pythona
      const data = {
        'delta': delta,
        'documentId': documentId
      }
      socket.emit("send_changes", data);
    };

    // 'text-change' zdarzenie z dokumentacji
    quill.on("text-change", handler);

    // usuwanie event listenera jeśli go już dłużej nie potrzebujemy
    return () => {
      // 'text-change'zdarzenie z bilioteki
      quill.off("text-change", handler);
    };
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
    // q.disable()
    q.setText('Loading...')
    setQuill(q);
  }, []);
  return <div className="container" ref={wrapperRef}></div>;
}
