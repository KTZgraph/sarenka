import {useState, useEffect} from "react";

const useFetch = url => {
  const [data, setData] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    //AbortController - do cleanup
    const abortCont = new AbortController();

    fetch(url, {signal: abortCont.signal})
      .then(res => {
        if(!res.ok){
          //jak status nie okejka
          throw Error(`could not fetch data from url:${url}`);
        }
        return res.json();
      })
      .then(data => {
        setData(data);
        setIsPending(false);
        setError(null);
      })
      .catch(err => {
        if(err.name === 'AbortError') {
          //ja zastopowane przez abortCont.abort()
          console.log('fetch aborted')
        }
        setIsPending(false); // żeby loading.. przy bnłedzie się nie pokazywało
        setError(err.message)
      })

    //cleanup function
    return () => abortCont.abort();
  }, [url]); //jak się tylko url zmieni to wywoła tego useEffect hooka

  // zwracanie wartości, lepiej jako obiekt niż lista; bo kolejność nie ma znaczenia
  return {data, isPending, error};
};

export default useFetch;
