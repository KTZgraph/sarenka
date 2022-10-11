/*
https://www.youtube.com/watch?v=bPNkdoEqfVY&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=16

bruch w d3.js to jest ten szary prostokąt na wykresie który można przesuwać
pozwala na wybranie podzzbioru (subportion of my chart) I can then extract and display values widoczne po dywkresem
będzie responsywne
można dodać nowe dane i wybrac za pomocą bruch nowe dane

*/

import {
  select,
  scaleLinear,
  max,
  line,
  curveCardinal,
  axisBottom,
  axisLeft,
} from "d3";
import { useRef, useEffect } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

import "./FilteringVisually.scss";

const FilteringVisually = ({ data }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

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
  }, [data, dimensions]);

  return (
    <div ref={wrapperRef} className="filtering-visually-chart">
      <svg ref={svgRef}>
        <g className="x-axis" />
        <g className="y-axis" />
      </svg>
    </div>
  );
};

export default FilteringVisually;
