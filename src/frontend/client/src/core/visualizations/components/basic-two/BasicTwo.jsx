// connected lines
// path z svg jest bardziej powerdful niż line z svg

import { select, line, curveCardinal } from 'd3';
// line z d3.js pozwala na pomoc z atrybuted d z <path> z svg
import { useRef, useEffect, useState } from 'react';

const BasicTwo = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20, 65, 75]);
  const svgRef = useRef();

  useEffect(() => {
    const svg = select(svgRef.current);
    // myLine jest własciwie funckją, która wygeneruje atrybut d naszego path element bazujac na danych które dostaje
    const myLine = line()
      .x((value, idx) => idx * 50)
      //   .y((value) => value)
      // zmiana y żeby wykres zaczynał się od dołu
      .y((value) => 150 - value)
      //   robię sobie krzywe
      .curve(curveCardinal);

    // svg
    //   .selectAll("circle")
    //   .data(data)
    //   .join("circle")
    //   .attr("r", (value) => value)
    //   .attr("cx", (value) => value * 1.1)
    //   .attr("cy", (value) => value * 1.1)
    //   .attr("stroke", "blue")
    //   .attr("fill", "gray");

    // WARNING ubieram dane w array, bo nie  chcę, żeby wygenerowało nowe path dla każdego elementu/liczy z stanu data
    // chcę jeden path dla mojej całej data array
    svg
      .selectAll('path')
      .data([data])
      // twqoryz nowe dane entering dla każdego fragmentu danych
      .join('path')
      // chcę żeby dodało dla każdego elementu atrybut d
      // tutaj callback z value ,, value to cała lista
      //   funckja myLine zwróci koordynaty, a potem .attr("d", callback ) doczemi je do atrybutu d
      .attr('d', (value) => myLine(value))
      // bez fill none zakolorwuje całą płaszczyznę, a teraz none to nawet linia się nie pojawia
      .attr('fill', 'none')
      //   trzeba dać stroke inaczej nic nie jest widoczne
      .attr('stroke', 'blue');
  }, [data]);

  return (
    <>
      <svg ref={svgRef}></svg>
      <br />
      <button onClick={() => setData(data.map((value) => value + 5))}>
        Update data
      </button>
      <button
        onClick={() => setData(data.filter((value) => value < 35))}
      >
        Filter data
      </button>
    </>
  );
};

export default BasicTwo;
