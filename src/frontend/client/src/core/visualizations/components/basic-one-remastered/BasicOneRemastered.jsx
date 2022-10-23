import { select } from 'd3';
import { useRef, useEffect, useState } from 'react';

const BasicOneRemastered = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20]);
  const svgRef = useRef();
  console.log(svgRef);

  useEffect(() => {
    console.log(svgRef);
    const svg = select(svgRef.current);
    // każe znaleźc wszystkie circles (tutja ich nie ma) i je zsynchronizować z danymi
    svg
      .selectAll('circle')
      .data(data)
      //   WARNING pierwsza wersja mocno versbose - trzeba się powtarzać z atrybutami
      /*.join(
        // ccallbacki dla każdego typu enter, update, exit
        // enter utowrzy te elementy w DOM
        (enter) =>
          enter
            .append("circle")
            .attr("r", (value) => value)
            .attr("cx", (value) => value * 2)
            .attr("cy", (value) => value * 2)
            .attr("stroke", "red"),
        // zakutlizuje kółk aktóre już  są w moim svg
        (update) =>
          update
            .attr("class", "updated")
            .attr("r", (value) => value)
            .attr("cx", (value) => value * 1.1)
            .attr("cy", (value) => value * 1.1)
            .attr("stroke", "blue")
            .attr("fill", "gray"),
        // hanfdle exitings circles - te elementy których już nie potrzebuję
        (exit) => exit.remove()
      );*/
      //   WARNING druga wersja skrócona - atrybuty po metodzie .join() będą do obu przypadków dopisywane
      //   WARNING to dlatego że mota .join() zwraca obiekt selection (jak d3.select(svgRef.current)) -> umożliwia zmianę atrybutów obu ewntering and updaintg elements
      //   WARNING teraz nie trzeba się powtarzać
      /*.join(
        // ccallbacki dla każdego typu enter, update, exit
        // enter utowrzy te elementy w DOM
        (enter) => enter.append("circle"),
        // zakutlizuje kółk aktóre już  są w moim svg
        (update) => update.attr("class", "updated"),
        // hanfdle exitings circles - te elementy których już nie potrzebuję
        // WARNING defaultowy callback - ALE jak chcę animowac, robić transistion czy coś, to muszę ten callback zrobić
        (exit) => exit.remove() //to jest defaultowy callback dla D3 - z automatu usuwa kółka, które nie sa już potrzebne, nawet bez tego callbacka
      )
      //   dodanie atrybutów po join - dodaje je do elementów enter i update - nie trzba się powtarzać
      .attr("r", (value) => value)
      .attr("cx", (value) => value * 1.1)
      .attr("cy", (value) => value * 1.1)
      .attr("stroke", "blue")
      .attr("fill", "gray")*/
      //   WARNING trzecia wersja gdzie używam defaultowych dla metody .join callbacków - MOŻNA jeszcze skrócić
      // .join("circle")  od razu stowrzy elementy circle dla mnie
      .join('circle')
      //   dodanie atrybutów po join - dodaje je do elementów enter i update - nie trzba się powtarzać
      .attr('r', (value) => value)
      .attr('cx', (value) => value * 1.1)
      .attr('cy', (value) => value * 1.1)
      .attr('stroke', 'blue')
      .attr('fill', 'gray');
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

export default BasicOneRemastered;
