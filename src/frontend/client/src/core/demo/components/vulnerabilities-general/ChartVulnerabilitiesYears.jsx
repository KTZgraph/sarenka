import { useEffect, useRef, useState } from "react";
import {
  vulnerabitilitesYearsDummy,
  vulnerabitilitesYearsCategoryDummy,
} from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";
// BUG trzeba w CSS ustawić wysokosć
import useResizeObserver from "../../../../hooks/useResizeObserver";

import D3ChartVulnerabilitiesYears from "./D3ChartVulnerabilitiesYears";

const currentYear = new Date().getFullYear().toString();

const yearOptions = Object.keys(vulnerabitilitesYearsDummy).map((k) => ({
  label: k.toString(),
  value: k,
}));

const ChartVulnerabilitiesYears = () => {
  const [yearSelected, setYearSelected] = useState(currentYear);
  const [data, setData] = useState([]);
  //   dane do wykresów liniowych
  const [dataCategory, setDataCategory] = useState([]);

  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);

  const dimensions = useResizeObserver(chartRef);

  useEffect(() => {
    // ustawianie danych
    setData(vulnerabitilitesYearsDummy[parseInt(yearSelected)]);
    setDataCategory(vulnerabitilitesYearsCategoryDummy[parseInt(yearSelected)]);

    const { width, height } =
      dimensions || chartRef.current.getBoundingClientRect();

    if (!chartState) {
      setChartState(
        new D3ChartVulnerabilitiesYears(
          chartRef.current,
          data,
          yearSelected,
          width,
          height,
          dataCategory
        )
      );
    } else {
      chartState.update(data, yearSelected, width, height, dataCategory);
    }
  }, [data, yearSelected, chartState, dataCategory]);

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
