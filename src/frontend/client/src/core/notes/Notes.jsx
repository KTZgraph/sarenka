import { useEffect, useRef } from 'react';
import { io } from 'socket.io-client';

const Notes = () => {
  const socket = useRef();

  useEffect(() => {
    //   FIXME CORSES
    socket.current = io('ws://localhost:3001');
    socket.current.on('connection', () => {
      console.log('connecte to server');
    });
  }, []);

  const handleClick = () => {
    console.log('click');
    try {
      socket.current.emit('message', new Date().getTime());
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div>
      <h1>Notes socketio</h1>
      <button type="button" onClick={handleClick}>
        Emit a time message
      </button>
    </div>
  );
};

export default Notes;
