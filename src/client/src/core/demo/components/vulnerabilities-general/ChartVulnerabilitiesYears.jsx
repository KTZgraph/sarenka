import { select, scaleLinear, scaleBand, axisBottom, max, axisLeft } from "d3";

import { useEffect, useRef, useState } from "react";
import { vulnerabitilitesYearsDummy } from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";
// z tym hookiem jakieś problemy
import useResizeObserver from "../../../../hooks/useResizeObserver";

import D3ChartVulnerabilitiesYears from "./D3ChartVulnerabilitiesYears";
import { drawChart } from "./D3ChartVulnerabilitiesYears";

const DUMMY_DATA = {
  2022: [
    { month: 1, critical: 32, high: 129, medium: 228, low: 304 },
    { month: 2, critical: 74, high: 163, medium: 259, low: 192 },
    { month: 3, critical: 29, high: 197, medium: 170, low: 395 },
    { month: 4, critical: 100, high: 107, medium: 273, low: 316 },
    { month: 5, critical: 22, high: 100, medium: 273, low: 485 },
    { month: 6, critical: 53, high: 118, medium: 183, low: 485 },
    { month: 7, critical: 53, high: 178, medium: 274, low: 269 },
    { month: 8, critical: 50, high: 193, medium: 192, low: 252 },
    { month: 9, critical: 89, high: 116, medium: 244, low: 199 },
  ],
  2021: [
    { month: 1, critical: 32, high: 129, medium: 228, low: 304 },
    { month: 2, critical: 74, high: 163, medium: 259, low: 192 },
    { month: 3, critical: 29, high: 197, medium: 170, low: 395 },
    { month: 4, critical: 100, high: 107, medium: 273, low: 316 },
    { month: 5, critical: 22, high: 100, medium: 273, low: 485 },
    { month: 6, critical: 53, high: 118, medium: 183, low: 485 },
    { month: 7, critical: 53, high: 178, medium: 274, low: 269 },
    { month: 8, critical: 50, high: 193, medium: 192, low: 252 },
    { month: 9, critical: 89, high: 116, medium: 244, low: 199 },
    { month: 10, critical: 80, high: 125, medium: 190, low: 393 },
    { month: 11, critical: 46, high: 115, medium: 122, low: 309 },
    { month: 12, critical: 28, high: 149, medium: 246, low: 484 },
  ],
  2020: [
    { month: 1, critical: 32, high: 129, medium: 228, low: 304 },
    { month: 2, critical: 74, high: 163, medium: 259, low: 192 },
    { month: 3, critical: 29, high: 197, medium: 170, low: 395 },
    { month: 4, critical: 100, high: 107, medium: 273, low: 316 },
    { month: 5, critical: 22, high: 100, medium: 273, low: 485 },
    { month: 6, critical: 53, high: 118, medium: 183, low: 485 },
    { month: 7, critical: 53, high: 178, medium: 274, low: 269 },
    { month: 8, critical: 50, high: 193, medium: 192, low: 252 },
    { month: 9, critical: 89, high: 116, medium: 244, low: 199 },
    { month: 10, critical: 80, high: 125, medium: 190, low: 393 },
    { month: 11, critical: 46, high: 115, medium: 122, low: 309 },
    { month: 12, critical: 28, high: 149, medium: 246, low: 484 },
  ],
  2019: [
    { month: 1, critical: 32, high: 129, medium: 228, low: 304 },
    { month: 2, critical: 74, high: 163, medium: 259, low: 192 },
    { month: 3, critical: 29, high: 197, medium: 170, low: 395 },
    { month: 4, critical: 100, high: 107, medium: 273, low: 316 },
    { month: 5, critical: 22, high: 100, medium: 273, low: 485 },
    { month: 6, critical: 53, high: 118, medium: 183, low: 485 },
    { month: 7, critical: 53, high: 178, medium: 274, low: 269 },
    { month: 8, critical: 50, high: 193, medium: 192, low: 252 },
    { month: 9, critical: 89, high: 116, medium: 244, low: 199 },
    { month: 10, critical: 80, high: 125, medium: 190, low: 393 },
    { month: 11, critical: 46, high: 115, medium: 122, low: 309 },
    { month: 12, critical: 28, high: 149, medium: 246, low: 484 },
  ],
};

const currentYear = new Date().getFullYear().toString();

// const yearOptions = Object.keys(vulnerabitilitesYearsDummy).map((k) => ({
const yearOptions = Object.keys(DUMMY_DATA).map((k) => ({
  label: k.toString(),
  value: k,
}));

const ChartVulnerabilitiesYears = () => {
  const wrapperRef = useRef();
  const svgRef = useRef();
  //   BUG z dimension - uwaga na CSS
  const dimensions = useResizeObserver(wrapperRef);
  const [chartState, setChartState] = useState(null);

  //   domyślnie aktulany rok
  const [yearSelected, setYearSelected] = useState(currentYear);
  const [data, setData] = useState([]);

  useEffect(() => {
    // *------------------------------------------------
    if (!dimensions) return;
    console.log("dimensions: ", dimensions);
    const { width, height } = dimensions;

    // const svg = select(svgRef.current)
    //   .attr("width", width)
    //   .attr("height", height);

    drawChart(svgRef.current, data, yearSelected, width, height);

    // *------------------------------------------------
  }, [data, yearSelected, chartState, dimensions]);

  return (
    <>
      <div className="svg-wrapper" ref={wrapperRef}>
        <Dropdown
          className="chart__dropdown"
          label="Select Year"
          options={yearOptions}
          value={yearSelected}
          onChange={(e) =>
            setData(vulnerabitilitesYearsDummy[parseInt(e.target.value)])
          }
        />
        <svg
          ref={svgRef}
          className="svg-chart"
          id="vulnerabilities-year-chart-id"
        ></svg>
      </div>
    </>
  );
};

export default ChartVulnerabilitiesYears;
