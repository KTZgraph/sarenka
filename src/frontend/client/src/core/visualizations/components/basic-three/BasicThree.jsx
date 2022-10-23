// dodawanie osi X i osi Y

import {
  select,
  line,
  curveCardinal,
  axisBottom,
  scaleLinear,
  axisRight,
} from 'd3';
import { useRef, useEffect, useState } from 'react';

const BasicThree = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20, 65, 75]);
  const svgRef = useRef();

  useEffect(() => {
    const svg = select(svgRef.current);
    // scala X
    const xScale = scaleLinear()
      // oś X - liczba elementów tutaj 7
      // domain - input values - ttuaj mam 7 liczb więc skaluje od 0 do 6 [0,1,2,3,4,5,6]
      //   .domain([0, 6])
      .domain([0, data.length - 1])
      // range wizualna reprezentacja danych
      .range([0, 300]);

    // sclaa Y - od 0 do 75 gdzie 75 to wiem, ze to moja największa wartość
    const yScale = scaleLinear()
      // domain - inut data - wartości na osi Y
      .domain([0, 75])
      // mapowanie wartości na wizualizację; 150 to dół wykresu bo oś Y rośnie w dół
      .range([150, 0]);

    // WARNING dodanie osi X
    // trudne do wyjasnienia Axis to własnieciwe funckja helper
    // that transform input values to something else wich is usually needed for the visual representation of that value
    // xAxis też wymaga funckji scale
    // axisBottom tak naprawdę w dół pozycjonuije ticks cyferki pod wartości osi X

    // daje bardzo dużo tick na osi X a ja mam tylko 6 wartości
    // const xAxis = axisBottom(xScale);
    // WARNING - zmian aliczby ticks na osi
    // const xAxis = axisBottom(xScale).ticks(7);
    const xAxis = axisBottom(xScale)
      .ticks(data.length)
      //   jeszcze trnasformuję żeby pokazywało od 1 do 7 zamiast od 0 do 6
      .tickFormat((index) => index + 1);

    // mam sobie grupę na oś w HTMl więc teraz chcę żeby d3.js sobie ten element HTMl <g className="x-axis" /> wybrał
    // wyszukuje po klasie i wywołuję funckje xAxis
    // podobne do xAxis(svg.select(".x-axis"))
    // metoda call to po prostu inna składnia, pozwala dodać do wybranego aktualnie elementu oś X
    // WARNIGN bez styli do oś jest na samej górze wykresu
    // svg.select(".x-axis").call(xAxis);
    // odbijam/przenoszę na dół wzgledem osi Y wartości
    svg
      .select('.x-axis')
      .style('transform', 'translateY(150px)')
      .call(xAxis);

    // WARNING - dodanie osi Y
    const yAxis = axisRight(yScale);
    // też robię element g dla osi 0Y - mówie d3.js żeby wybrała html <g className="y-axis" />
    // przesuwam oś pionową OY prawo lewo czyli względem osi X - stad translateX
    svg
      .select('.y-axis')
      .style('transform', 'translateX(300px)')
      .call(yAxis);

    // generates the "d" attribute of path element
    const myLine = line()
      // tu mnoże, przez 50 bo wiem, że moje svg jest rzerokosi 350px
      //   .x((value, idx) => idx * 50)
      // teraz ładnie dynamicznie
      .x((value, idx) => xScale(idx))
      //   .y((value) => 150 - value)
      // ładnei dynamicznie przeskalowane przez funckję yScale
      //   .y((value) => yScale(value))
      // można to szybciej zapisać bez callbacka - wywoął sobie sam funckje z paramtertem value który d3.js daje
      .y(yScale)
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

    svg
      //   .selectAll("path")
      // WARNING - przez to wykres ląduje na dół gdy mamy oś X dodaną, bo oś to też elemnt <path>
      //   lepszy slektor - wybiera elementy które mają klase line - czyli oś X już nie
      .selectAll('.line')
      .data([data])
      .join('path')
      //   .attr("d", (value) => myLine(value))
      // szybszy zapis bez callback - metoda d3.js sama sobie funckje wywoła i przekaże value
      .attr('d', myLine)
      .attr('fill', 'none')
      .attr('stroke', 'blue')
      //   dodanie klasy do nowych albo aktulizowanych lementów path
      .attr('class', 'line');
  }, [data]);

  return (
    <>
      {/* style={{ overflow: "visible" }} fajnie widać, gdzie wykres sie przeniósł */}
      <svg ref={svgRef} style={{ overflow: 'visible' }}>
        {/* fajnie jest sobie przygotowac grupę pod oś X albo oś Y - od razu mozna ddodac kalsę css */}
        <g className="x-axis" />
        <g className="y-axis" />
      </svg>
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

export default BasicThree;
