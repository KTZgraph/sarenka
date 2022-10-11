import { select } from "d3";
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
  }, [colors, data, dimensions, keys]);

  return (
    <>
      <div ref={wrapperRef} style={{ marginBottom: "2rem" }}>
        <svg ref={svgRef}>
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default StackedBarChart;
