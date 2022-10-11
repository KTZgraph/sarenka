/*
https://www.youtube.com/watch?v=dxUyI2wfYSI&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=18

ten zoom ma zastosowanie do każdego liniowego wykresu, cyz też wykresu któy używa linear or continuous scales
na podstawie plkiu client\src\core\visualizations\components\filtering-visually\FilteringVisuallyChild.jsx

*/

import { height } from "@mui/system";
import {
  select,
  scaleLinear,
  max,
  line,
  curveCardinal,
  axisBottom,
  axisLeft,
  //   zoom z d3.js do powiększania wykresów
  zoom,
} from "d3";
import { useRef, useEffect } from "react";

import useResizeObserver from "../../../../hooks/useResizeObserver";

import "./ZoomableLineChart.scss";

const ZoomableLineChart = ({ data, clipPathId = "myZoomableLineChart-id" }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    const svgContent = svg.select(".content");

    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();
    // scales + line generator
    const xScale = scaleLinear()
      .domain([0, data.length - 1])
      .range([10, width - 10]);

    const yScale = scaleLinear()
      .domain([0, max(data)])
      .range([height - 10, 10]);

    const lineGenerator = line()
      .x((d, index) => xScale(index))
      .y((d) => yScale(d))
      .curve(curveCardinal);

    // render the line
    svgContent
      .selectAll(".myLine")
      .data([data])
      .join("path")
      .attr("class", "myLine")
      .attr("stroke", "black")
      .attr("fill", "none")
      .attr("d", lineGenerator);

    // teraz kropki renderuję w grupie content
    svgContent
      .selectAll(".myDot")
      .data(data)
      .join("circle")
      .attr("class", "myDot")
      .attr("stroke", "black")
      .attr("r", 4)
      .attr("fill", "orange")
      .attr("cx", (value, index) => xScale(index))
      .attr("cy", yScale);

    // axes
    const xAxis = axisBottom(xScale);
    svg
      .select(".x-axis")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);

    const yAxis = axisLeft(yScale);
    svg.select(".y-axis").call(yAxis);

    // zoom behaviour
    // funckaj zoom zwraca funckję, trzeba zdefiniować trzy różne rzeczy
    // 1) scaleExtend - jak daleko mozemy zoom in and zoom out w svg - zmiejnszyć 2 razy (max zoom out), maskzymalnie powiekszyć 5 razy (max zoom in) w naszym środku svg
    // 2) translateExtent basically limits our zoom behaviour when we click and hold the mouse to drag or navigate inside of our line chart
    //  -> od punkut ).) góra lewo do prawo dów szerokosc,wyokość
    // 3) .on("zoom",  -  zoomhandler - the place where we want to handle what actually happens when a zoom event is triggered
    const zoomBehaviour = zoom()
      .scaleExtent([0.5, 5])
      .translateExtent([
        [0, 0],
        [width, height],
      ])
      .on("zoom", () => {
        console.log("zoomed!");
      });

    //   połączenie zooma z svg, zoomBehaviour to funckja któa przyjmuje selekcje
    svg.call(zoomBehaviour);
    // zoomBehaviour(svg); //alternatywnie
  }, [data, dimensions]);

  return (
    <>
      <div
        ref={wrapperRef}
        style={{ marginBottom: "2rem" }}
        className="zoomable-line-chart"
      >
        <svg ref={svgRef} style={{ height: "100%" }}>
          <defs>
            <clipPath id={clipPathId}>
              <rect x="0" y="0" width="100%" height="100%" />
            </clipPath>
          </defs>

          <g className="x-axis" />
          <g className="y-axis" />
          <g
            className="content"
            clipPath={`url(#${clipPathId})`}
            style={{ zIndex: 999 }}
          ></g>
        </svg>
      </div>
    </>
  );
};

export default ZoomableLineChart;
