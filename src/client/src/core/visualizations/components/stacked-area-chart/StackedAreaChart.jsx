import {
  select,
  scaleBand,
  axisBottom,
  stack,
  max,
  scaleLinear,
  axisLeft,
  stackOrderAscending,
} from "d3";
import { useEffect, useRef } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const StackedAreaChart = ({ data, keys, colors }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();
    const stackGenerator = stack().keys(keys).order(stackOrderAscending);
    const layers = stackGenerator(data);
    const extent = [
      0,
      max(layers, (layer) => max(layer, (sequence) => sequence[1])),
    ];

    const xScale = scaleBand()
      .domain(data.map((d) => d.year))
      .range([0, width])
      .padding(0.25);

    const yScale = scaleLinear().domain(extent).range([height, 0]);

    const yAxis = axisLeft(yScale);
    svg.select(".y-axis").call(yAxis);

    svg
      .selectAll(".layer")
      .data(layers)
      .join("g")
      .attr("class", "layer")
      .attr("fill", (layer) => {
        console.log("layer", layer);
        return colors[layer.key];
      })
      .selectAll("rect")
      .data((layer) => layer)
      .join("rect")
      .attr("x", (sequence) => {
        console.log("sequence: ", sequence);
        return xScale(sequence.data.year);
      })
      .attr("width", xScale.bandwidth())
      .attr("y", (sequence) => yScale(sequence[1]))
      .attr("height", (sequence) => yScale(sequence[0]) - yScale(sequence[1]));

    const xAxis = axisBottom(xScale);
    svg
      .select(".x-axis")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);
  }, [colors, data, dimensions, keys]);

  return (
    <>
      <div
        ref={wrapperRef}
        style={{
          marginBottom: "2rem",
          overflow: "visible",
          width: "80%",
          height: "300px",
          padding: "20px",
        }}
      >
        <svg
          ref={svgRef}
          style={{ overflow: "visible", width: "100%", height: "100%" }}
        >
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default StackedAreaChart;
