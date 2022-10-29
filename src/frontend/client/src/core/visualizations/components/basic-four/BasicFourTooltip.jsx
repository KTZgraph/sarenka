/*
BUG - rozwiazanie tooltipów
https://www.youtube.com/watch?v=sp4HMJdfnPU&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=20
*/

import { select, axisBottom, scaleLinear, axisRight, scaleBand } from "d3";
import { useRef, useEffect, useState } from "react";

const BasicFourTooltip = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20, 65, 75]);
  const svgRef = useRef();

  useEffect(() => {
    const svg = select(svgRef.current);

    const xScale = scaleBand()
      .domain(data.map((value, index) => index))
      .range([0, 300])
      .padding(0.5);

    const yScale = scaleLinear().domain([0, 150]).range([150, 0]);

    const colorScale = scaleLinear()
      .domain([75, 100, 150])
      .range(["green", "orange", "red"])
      .clamp(true);

    const xAxis = axisBottom(xScale).ticks(data.length);

    svg.select(".x-axis").style("transform", "translateY(150px)").call(xAxis);

    const yAxis = axisRight(yScale);
    svg.select(".y-axis").style("transform", "translateX(300px)").call(yAxis);

    svg
      .selectAll(".bar")
      .data(data)
      .join("rect")
      .attr("class", "bar")
      .attr("x", (value, idx) => xScale(idx))
      .attr("width", xScale.bandwidth())
      .style("transform", "scale(1, -1)")

      .attr("y", -150)

      // BUG rozwiazanie https://www.youtube.com/watch?v=sp4HMJdfnPU&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=20
      .on("mouseenter", (event, value) => {
        // BUG  sposób - poprzez pobranie nodów
        // wybierz wszystkie elementy o takiej klasie, i zwróć mi index z okbietu który jest w evencie bo na niego najechałam
        // pórwnuje DOM lement ze wszystkimi elementami DOM, które mają className="bar"
        const indexBar = svg.selectAll(".bar").nodes().indexOf(event.target);

        svg
          .selectAll(".tooltip")
          .data([value])

          .join((enter) => enter.append("text").attr("y", yScale(value) - 4))
          .attr("class", "tooltip")
          .text(value)
          .attr("text-anchor", "middle")
          // .attr("x", event.target.getBoundingClientRect().x)
          // .style("transform", "translate(-180px)")
          // BUG  sposób - poprzez pobranie nodów - wyśrodkowanie napisu z wartością nad słupkiem
          .attr("x", xScale(indexBar) + xScale.bandwidth() / 2)

          .transition()
          .attr("opacity", 1)
          .attr("y", yScale(value) - 7);

        console.log(event.target.getBoundingClientRect().x);
      })
      .on("mouseleave", () => svg.select(".tooltip").remove())
      .transition()

      .attr("height", (value) => 150 - yScale(value))
      .attr("fill", colorScale);
  }, [data]);

  return (
    <>
      <h2>tu są tooltipy</h2>

      <svg ref={svgRef} style={{ overflow: "visible" }}>
        <g className="x-axis" />
        <g className="y-axis" />
      </svg>
      <br />
      <button onClick={() => setData(data.map((value) => value + 5))}>
        Update data
      </button>
      <button onClick={() => setData(data.filter((value) => value < 35))}>
        Filter data
      </button>
      <button
        onClick={() => setData([...data, Math.floor(Math.random() * 140)])}
      >
        Add data
      </button>
    </>
  );
};

export default BasicFourTooltip;
