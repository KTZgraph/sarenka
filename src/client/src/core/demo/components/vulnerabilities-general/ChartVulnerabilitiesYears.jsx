import { useEffect, useRef, useState } from "react";
import { vulnerabitilitesYearsDummy } from "./vulnerabilities-years-dummy";
import Dropdown from "../../../../UI/Dropdown";

const yearOptions = [
  { label: "2022", value: 2022 },
  { label: "2021", value: 2021 },
  { label: "2020", value: 2020 },
  { label: "2019", value: 2019 },
  { label: "2018", value: 2018 },
  { label: "2017", value: 2017 },
  { label: "2016", value: 2016 },
  { label: "2015", value: 2015 },
];

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
