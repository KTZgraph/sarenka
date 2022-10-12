/*
https://codepen.io/Samih/pen/nRXaOG
https://www.youtube.com/watch?v=hOzKr8H_438

line chart
https://www.youtube.com/watch?v=SnkpNCxHSkc&t=723s
*/
import {
  axisBottom,
  axisLeft,
  scaleBand,
  scaleLinear,
  select,
  line,
  curveCardinal,
} from "d3";
import { useEffect, useState, useRef } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const SimpleBarLineGraph = () => {
  const [data, setData] = useState([200, 250, 60, 150, 100, 175]);
  const [dataLine, setDataLine] = useState([100, 125, 30, 75, 50, 87]);
  const wrapperRef = useRef();

  const svgRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    // const width = 500;
    // const height = 300;
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //1) setting up svg container
    const svg = select(svgRef.current)
      .attr("width", width)
      .attr("height", height)
      .style("overflow", "visible");
    //   .style("margin-top", "75px");

    //2) setting the scaling
    const xScale = scaleBand()
      .domain(data.map((d, idx) => idx))
      .range([0, width])
      .padding(0.5);

    //   skala na odwrót
    const yScale = scaleLinear().domain([0, height]).range([height, 0]);

    //3) setting the axes
    const yAxis = axisLeft(yScale).ticks(5);
    svg.append("g").call(yAxis);

    const xAxis = axisBottom(xScale).ticks(data.length);
    svg.append("g").call(xAxis).attr("transform", `translate(0, ${height})`);

    //4) setting the svg data
    svg
      .selectAll(".bar")
      .data(data)
      .join("rect")
      .attr("x", (d, idx) => xScale(idx))
      .attr("y", yScale)
      .attr("width", xScale.bandwidth())
      .attr("height", (d) => height - yScale(d));

    //   WARNING - kombinowanie
    // WARNING https://www.youtube.com/watch?v=SnkpNCxHSkc&t=723s
    // kombinowanie
    const xScaleLine = scaleLinear()
      .domain([0, data.length - 1])
      .range([0, width]);

    const yScaleLine = scaleLinear().domain([0, height]).range([height, 0]);

    const generateScaledLine = line()
      .x((d, idx) => xScaleLine(idx))
      .y(yScaleLine)
      .curve(curveCardinal);

    svg
      .selectAll(".line")
      //   BUG trzeba listę z list yzrobić, żeby był jedne elemnt do path
      //   .data([data])
      .data([dataLine])
      .join("path")
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "red");

    //   konie useEffect
  }, [data, dimensions]);

  return (
    <div
      ref={wrapperRef}
      style={{
        marginBottom: "2rem",
        overflow: "visible",
        width: "300px",
        height: "500px",
        // padding: "40px",
        // minHeight: "500px",
      }}
    >
      <svg
        ref={svgRef}
        style={{ overflow: "visible", width: "100%", height: "100%" }}
      ></svg>
    </div>
  );
};

export default SimpleBarLineGraph;
