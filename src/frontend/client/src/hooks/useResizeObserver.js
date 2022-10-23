/*
https://www.youtube.com/watch?v=a4rstx9Pz2o&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=8
*/

import { useEffect, useState } from 'react';

// custom react hook do obserwowanie elementu DOM
export default function useResizeObserver(divRef) {
  // https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
  //   najbardziej wydajny sposób do sprawdzenia zmiany rozmiaru elementu
  //   sama zmiana rozmiaru window nie koniecznie sprawia, że zmienia się rozmair elementu
  // BUG nie działa z SVG ale z DIV już tak
  const [dimensions, setDimensions] = useState(null);
  // trzeba użyć useEffect hooka, zeby dostać się do elementów DOM które zostały wyrenderowane

  useEffect(() => {
    const observeTarget = divRef.current;
    const resizeObserver = new ResizeObserver((entries) => {
      // callback który ma entries do obserwowania
      console.log('------------- useResizeObserver -------------');
      entries.forEach((entry) => {
        setDimensions(entry.contentRect);
      });
      // set resized dimensions here
    });

    resizeObserver.observe(observeTarget);
    // cleanup dla tego useEffect - to jest wywoływane gdy kompoinent któy używa tego hooka
    // jest usuwany lub unMounted
    return () => {
      resizeObserver.unobserve(observeTarget);
    };
  }, [divRef]);

  return dimensions;
}
