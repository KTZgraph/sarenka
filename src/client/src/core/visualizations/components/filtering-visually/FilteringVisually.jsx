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
//BUG custom hook usePrevious żeby w nieskońcozść nie renderowało się tutaj w useEffect po zmianie pozycji selection brusha
import usePrevious from "../../../../hooks/usePrevious";

import "./FilteringVisually.scss";

// props children do renderowania dzieci komponentu
const FilteringVisually = ({ data, children }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  //   wybrana pozycja brusha
  // WARNING defaultowo brush JAKO INDEX wartości, NIE PIKSELE - default index selection
  const [selection, setSelection] = useState([0, 1.5]);

  // BUG  usePrevious - custom hook
  const previousSelection = usePrevious(selection);

  //   will be called initially and on every dta change
  useEffect(() => {
    const svg = select(svgRef.current);

    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   scales + line generator
    const xScale = scaleLinear()
      //   .domain([0, data.length - 1])
      //   FIX - bo bez tego są wartości ujemny pod pod osią Y
      .domain([0, data.length])
      .range([0, width]);

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
      //   .attr("r", 2)
      // WARNING - zmiana styli kółek jeśli sa w polu brush - selection to  lista dwóch współrzednych na osi X
      //   jeśli jest w polu to promień kółka to 4
      .attr("r", (value, idx) =>
        idx >= selection[0] && idx <= selection[1] ? 4 : 2
      )
      //   tak samo zmiana koloru wypęłnienia jeśli kólka są w polu brush
      .attr("fill", (value, idx) =>
        idx >= selection[0] && idx <= selection[1] ? "orange" : "black"
      )
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
        // BUG - jeśli tak zostawimy to ten callback się wykonuje w nieskońcozsć i rerenderujemy nieskończenie w useEffect
        // BUG - trzeba upeniwć się, że  svg.select(".brush")... jest wywoływane tylko gdy setSelection sie nie zmienia
        setSelection(indexSelection);
      });

    // renderowanie brusha w svg
    // svg.select(".brush").call(brush);

    // BUG to zawsze zmienia pozycję na początkujacą - trzeba użyć kolejnego cutomowego hooka usePrevious
    /*svg
      .select(".brush")
      .call(brush)
      // brush.move, [0, 100] wprowadza zakres brush na samym początku od zera o 100
      //   .call(brush.move, [0, 100]);
      //   WARNING defaultowa pozycja brusha - z index value mapuję na piksele
      //   brush.move wymaga wartości pikselowej jako arumentu
      //   .call(brush.move, selection.map(xScale));
      .call(brush.move, selection);*/
    //   BUG - rozwiązanie svg.select(".brush").call(brush)...
    if (previousSelection === selection) {
      svg.select(".brush").call(brush).call(brush.move, selection.map(xScale));
    }

    // koniec useEffect
  }, [data, dimensions, selection]);

  return (
    <>
      <div ref={wrapperRef} className="filtering-visually-chart">
        <svg ref={svgRef}>
          {/* WARNING grupy są ważne, bo brush też będzie renderowany jako element HTML */}
          <g className="x-axis" />
          <g className="y-axis" />
          <g className="brush" />
        </svg>
      </div>
      {/* tag small fo infgormacji o zakresie wybranych przez brush danych */}
      <small style={{ marginBottom: "1rem", marginRight: "50px" }}>
        Selected values: [
        {data
          // fitltrowqanie wartości które są w zakresie brusha
          .filter((value, idx) => idx >= selection[0] && idx <= selection[1])
          .join(", ")}
        ]
      </small>

      {/* dzieci tego komponentu - zamiana na funckję żeby przekazać aktualną wartosc selection z brusha*/}
      {children(selection)}
    </>
  );
};

export default FilteringVisually;
