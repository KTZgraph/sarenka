import { useEffect, useRef } from "react";

/*
https://youtu.be/bPNkdoEqfVY?t=806
Hook, that return the last used value

za pomocą tego mozna przechowywać downolną wartośc i przy koljenym rerenderowaniu komponentu 
and with that you can basically store any vairable and in the next render of a component you can check if that variable has changed since the last render
that is something you can easily do with class components but you cannot do that with functional components that easily
and that is wgy you have to use this usePrevious hook and 
*/

function usePrevious(value) {
  const ref = useRef();

  useEffect(() => {
    ref.current = value;
  });

  return ref.current;
}

export default usePrevious;
