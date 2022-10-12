import { useEffect, useRef, useState } from "react";
import { vulnerabitilitesYearsDummy } from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";
// z tym hookiem jakieś problemy
import useResizeObserver from "../../../../hooks/useResizeObserver";

import D3ChartVulnerabilitiesYears from "./D3ChartVulnerabilitiesYears";

const currentYear = new Date().getFullYear().toString();

const yearOptions = Object.keys(vulnerabitilitesYearsDummy).map((k) => ({
  label: k.toString(),
  value: k,
}));

const getDataByYear = (selectedYear) => {
  const year = parseInt(selectedYear);
  return vulnerabitilitesYearsDummy[year];
};

const ChartVulnerabilitiesYears = () => {
  const [data, setData] = useState([]);
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  const [yearSelected, setYearSelected] = useState(currentYear);

  const dimensions = useResizeObserver(chartRef);

  useEffect(() => {
    const { width, height } =
      dimensions || chartRef.current.getBoundingClientRect();

    if (!chartState) {
      setData(getDataByYear(yearSelected));
      setChartState(
        new D3ChartVulnerabilitiesYears(
          chartRef.current,
          data,
          yearSelected,
          width,
          height
        )
      );
    } else {
      setData(getDataByYear(yearSelected));
      chartState.update(data, yearSelected, width, height);
    }
  }, [data, yearSelected, chartState]);

  return (
    <>
      <div
        className="svg-wrapper"
        id="dashboard__trends-chart-id"
        ref={chartRef}
      >
        <Dropdown
          className="chart__dropdown"
          label="Select Year"
          options={yearOptions}
          value={yearSelected}
          onChange={(e) => setYearSelected(e.target.value)}
        />
      </div>
    </>
  );
};

export default ChartVulnerabilitiesYears;
