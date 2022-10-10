import { useEffect, useRef } from 'react';
import { select } from 'd3';
import useResizeObserver from '../../../../hooks/useResizeObserver';

/*
Component that renders a map of Germany
*/

const GeoChart = ({ data, property }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // will be called initially and on every data change
  useEffect(() => {
    const svg = select(svgRef.current);

    // use resized dimensions
    // but fall back to getBoundingClientReact, if no dimension yet
    const { widt, height } =
      dimensions || wrapperRef.current.getBoundingClientReact();
  }, [data, dimensions, property]);

  return (
    <div ref={wrapperRef} style={{ marginBottom: '2rem' }}>
      <svg ref={svgRef}></svg>
    </div>
  );
};

export default GeoChart;
