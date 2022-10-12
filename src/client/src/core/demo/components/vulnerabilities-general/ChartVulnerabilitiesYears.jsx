import { select, scaleLinear, scaleBand, axisBottom, max, axisLeft } from "d3";

import { useEffect, useRef, useState } from "react";
import { vulnerabitilitesYearsDummy } from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";
import useResizeObserver from "../../../../hooks/useResizeObserver";

import D3ChartVulnerabilitiesYears from "./D3ChartVulnerabilitiesYears";

const currentYear = new Date().getFullYear().toString();

const yearOptions = Object.keys(vulnerabitilitesYearsDummy).map((k) => ({
  label: k.toString(),
  value: k,
}));

const ChartVulnerabilitiesYears = () => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);
  const [chartState, setChartState] = useState(null);

  //   domyślnie aktulany rok
  const [yearSelected, setYearSelected] = useState(currentYear);
  const [data, setData] = useState([]);

  useEffect(() => {
    // *------------------------------------------------
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    console.log("dimensions: ", dimensions);
    console.log("width: ", width);
    console.log("height: ", height);

    if (!chartState) {
      setData(vulnerabitilitesYearsDummy[parseInt(yearSelected)]);
      setChartState(
        new D3ChartVulnerabilitiesYears(
          svgRef.current,
          data,
          yearSelected,
          width,
          height
        )
      );
    } else {
      setData(vulnerabitilitesYearsDummy[parseInt(yearSelected)]);
      chartState.update(data, yearSelected, width, height);
    }

    // *------------------------------------------------
  }, [data, yearSelected, dimensions]);

  return (
    <>
      <div className="svg-wrapper" ref={wrapperRef}>
        <Dropdown
          className="chart__dropdown"
          label="Select Year"
          options={yearOptions}
          value={yearSelected}
          onChange={(e) => setYearSelected(e.target.value)}
        />
        <svg ref={svgRef} className="svg-chart">
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default ChartVulnerabilitiesYears;
