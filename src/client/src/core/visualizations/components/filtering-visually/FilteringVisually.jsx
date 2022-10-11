/*
https://www.youtube.com/watch?v=bPNkdoEqfVY&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=16

bruch w d3.js to jest ten szary prostokąt na wykresie który można przesuwać
pozwala na wybranie podzzbioru (subportion of my chart) I can then extract and display values widoczne po dywkresem
będzie responsywne
można dodać nowe dane i wybrac za pomocą bruch nowe dane

`brushX` funckja z d3.js

*/

import {
  select,
  scaleLinear,
  max,
  line,
  curveCardinal,
  axisBottom,
  axisLeft,
  brushX,
} from "d3";
import { useRef, useEffect, useState } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

import "./FilteringVisually.scss";

const FilteringVisually = ({ data }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  //   wybrana pozycja brusha
  // WARNING defaultowo brush JAKO INDEX wartości, NIE PIKSELE - default index selection
  const [selection, seteSelection] = useState([0, 1.5]);

  //   will be called initially and on every dta change
  useEffect(() => {
    const svg = select(svgRef.current);

    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   scales + line generator
    const xScale = scaleLinear()
      .domain([0, data.length - 1])
      .range([height, 0]);

    // do  mapowanie wartości na osi OY
    const yScale = scaleLinear()
      .domain([0, max(data)])
      .range([height, 0]);

    //   line funckja z d3.js
    const lineGenerator = line()
      .x((d, idx) => xScale(idx))
      .y((d) => yScale(d))
      //   zakryzwienie, żeby nie była taka ostra
      .curve(curveCardinal);

    //   render the line
    svg
      .selectAll(".myLine")
      .data([data])
      .join("path")
      .attr("class", "myLine")
      .attr("stroke", "black")
      .attr("fill", "none")
      .attr("d", lineGenerator);

    //   kólko dla każdej wartości
    svg
      .selectAll(".myDot")
      .data(data)
      .join("circle")
      .attr("class", "myDot")
      .attr("stroke", "black")
      .attr("r", 2)
      .attr("cx", (value, idx) => xScale(idx))
      .attr("cy", yScale);

    //   axes
    const xAxis = axisBottom(xScale);
    // do elem,entu html dodaję os OX i ją transofrmuję żeby była na dole obrazka (tam gdzie wysokosc, bo rośnie w dół całość)
    svg
      .select(".x-axis")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);

    const yAxis = axisLeft(yScale);

    // do elem,entu html dodaję os OY
    svg.select(".y-axis").call(yAxis);

    // WARNING - brush logic
    // initializacaj brusha
    // extent pozwala na poruszanie się brush - pole od lewego gónego wierzchołka, do prawgo dolnego
    // BUG extent przyjmuje listę zagnieżdżoną jako argument [!]
    const brush = brushX()
      .extent([
        [0, 0],
        [width, height],
      ])
      // eventy na który reaguje brush
      // start od początku
      // move kiedy się rusza
      // end kiedy przestaje się ruszać bruch
      .on("start brush end", (event) => {
        // jak brush jest nullem np odkilkaliśmy z boku to event nie ma takiego atrybutu i rzuca błedem
        if (!event.selection) return;

        // skal xScale jest w stanie z pikseli odwórić wartosc na index
        const indexSelection = event.selection.map(xScale.invert);
        // trę wartosc chcę zapisać w useState żeby potem użyć w .call(brush.move, [0,100])
        // bez tego za każdym razem jak wykres się zrerenderuje (np po zmianie rozmiaru okna przeglądartki) to brush jest na początku 0, 100 pikseli
        // dodatkowo jajk moje kółka sa zaznaczone brushem to chce żeby wyglądały te zaznaczone inaczej
        console.log(indexSelection);
      });

    // renderowanie brusha w svg
    // svg.select(".brush").call(brush);

    svg
      .select(".brush")
      .call(brush)
      // brush.move, [0, 100] wprowadza zakres brush na samym początku od zera o 100
      .call(brush.move, [0, 100]);

    // koniec useEffect
  }, [data, dimensions]);

  return (
    <div ref={wrapperRef} className="filtering-visually-chart">
      <svg ref={svgRef}>
        {/* WARNING grupy są ważne, bo brush też będzie renderowany jako element HTML */}
        <g className="x-axis" />
        <g className="y-axis" />
        <g className="brush" />
      </svg>
    </div>
  );
};

export default FilteringVisually;
