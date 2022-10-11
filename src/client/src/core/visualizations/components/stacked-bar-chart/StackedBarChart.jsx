import { select, scaleBand, axisBottom } from "d3";
import { useEffect, useRef } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const StackedBarChart = ({ data, keys, colors }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   sklaa X jest potrzebna do xAxis
    const xScale = scaleBand()
      // domain input to lata, map zwraca listę
      .domain(data.map((d) => d.year))
      .range([0, width]);

    // renderuje oś X
    const xAxis = axisBottom(xScale);
    // teraz dodać do svg
    svg.select(".x-axis").call(xAxis);
  }, [colors, data, dimensions, keys]);

  return (
    <>
      <div
        ref={wrapperRef}
        style={{ marginBottom: "2rem", overflow: "visible" }}
      >
        <svg ref={svgRef} style={{ overflow: "visible" }}>
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default StackedBarChart;
