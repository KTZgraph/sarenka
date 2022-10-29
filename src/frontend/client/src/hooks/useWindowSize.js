import { useEffect, useState } from 'react';

export default function useWindowSize() {
  // https://www.youtube.com/watch?v=OHvJqOjToes
  const [size, setSize] = useState([
    window.innerHeight,
    window.innerWidth,
  ]);

  // useEffect do nasłuchiwania resize windows
  useEffect(() => {
    const handleResize = () => {
      setSize([window.innerHeight, window.innerWidth]);
    };

    window.addEventListener('resize', handleResize);

    // cleanup
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return size;
}
