// http://bl.ocks.org/tmcw/3931800/972696d92e86c4f541ec0c89b5657771b40e99fa
// Line Chart

import { useEffect, useRef, useState } from 'react';
// import useWindowSize from "../../../../hooks/useWindowSize";

import {
  trendsChartData2022,
  trendsChartData2021,
  trendsChartData2020,
  trendsChartData2019,
  trendsChartData2018,
  trendsChartData2017,
  trendsChartData2016,
  trendsChartData2015,
} from './trends-chart';
import D3ChartTrends from './D3ChartTrends';
import Dropdown from '../../../../UI/Dropdown';

import './TrendsChart.scss';

const yearOptions = [
  { label: '2022', value: 2022 },
  { label: '2021', value: 2021 },
  { label: '2020', value: 2020 },
  { label: '2019', value: 2019 },
  { label: '2018', value: 2018 },
  { label: '2017', value: 2017 },
  { label: '2016', value: 2016 },
  { label: '2015', value: 2015 },
];

const getDataByYear = (year) => {
  console.log('year', year);
  console.log('year', typeof year);
  let data = [];

  switch (Number(year)) {
    case 2022:
      console.log(' case 2022:');
      data = trendsChartData2022;
      break;

    case 2021:
      console.log(' case 2021:');
      data = trendsChartData2021;
      break;

    case 2020:
      console.log(' case 2020:');
      data = trendsChartData2020;
      break;

    case 2019:
      data = trendsChartData2019;
      break;

    case 2018:
      data = trendsChartData2018;
      break;

    case 2017:
      data = trendsChartData2017;
      break;

    case 2016:
      data = trendsChartData2016;
      break;

    case 2015:
      data = trendsChartData2015;
      break;

    default:
      console.log(' case default:');
      data = trendsChartData2022;
      break;
  }

  return data;
};

const TrendsChart = () => {
  const [data, setData] = useState([]);
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  // const [windowHeight, windowWidth] = useWindowSize();
  // domyślnie wybór to katualny rok
  const [yearSelected, setYearSelected] = useState(
    new Date().getFullYear().toString()
  );

  useEffect(() => {
    console.log('----- TrendsChart ----- ');
    // setData(trendsChartData2021);
    // setData(trendsChartData2022);

    if (!chartState) {
      setData(getDataByYear(yearSelected));
      setChartState(
        new D3ChartTrends(chartRef.current, data, yearSelected)
      );
    } else {
      setData(getDataByYear(yearSelected));
      chartState.update(data, yearSelected);
    }
  }, [data, yearSelected, chartState]);

  return (
    <>
      <div
        className="dashboard__trends-chart"
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

export default TrendsChart;
