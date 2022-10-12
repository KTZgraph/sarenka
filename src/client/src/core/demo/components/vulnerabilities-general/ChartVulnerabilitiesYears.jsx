import { useEffect, useRef, useState } from "react";
import { vulnerabitilitesYearsDummy } from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";

const yearOptions = Object.keys(vulnerabitilitesYearsDummy).map((k) => ({
  label: k.toString(),
  value: k,
}));

const ChartVulnerabilitiesYears = () => {
  const svgRef = useRef(null);
  const wrapperRef = useRef(null);
  //   domyślnie aktulany rok
  const [yearSelected, setYearSelected] = useState(
    new Date().getFullYear().toString()
  );
  const [data, setData] = useState(
    vulnerabitilitesYearsDummy[parseInt(yearSelected)]
  );

  useEffect(() => {
    console.log("data", data);
    console.log(yearSelected);
    setData(vulnerabitilitesYearsDummy[parseInt(yearSelected)]);
  }, [data, yearSelected]);

  return (
    <>
      <div
        className="chart-vulnerabilities-years"
        id="dashboard__trends-chart-id"
        ref={wrapperRef}
      >
        <Dropdown
          className="chart__dropdown"
          label="Select Year"
          options={yearOptions}
          value={yearSelected}
          onChange={(e) => setYearSelected(e.target.value)}
        />
        <svg ref={svgRef}></svg>
      </div>
    </>
  );
};

export default ChartVulnerabilitiesYears;
