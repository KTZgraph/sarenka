import { useEffect, useRef, useState } from 'react';
import D3BasicAreaChart from './D3BasicAreaChart';

const DUMMY_DATA = [
  { year: '2011', count: 260 },
  { year: '2012', count: 60 },
  { year: '2014', count: 120 },
  { year: '2015', count: 197 },
  { year: '2016', count: 52 },
  { year: '2017', count: 52 },
  { year: '2018', count: 60 },
  { year: '2019', count: 120 },
  { year: '2020', count: 97 },
  { year: '2021', count: 115 },
  { year: '2022', count: 200 },
];

const BasicAreaChart = () => {
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  // WARNING  muszą być jakies wstępne dane do tego wykresu
  const [data, setData] = useState(DUMMY_DATA);

  useEffect(() => {
    console.log('----- D3BasicAreaChart ----- ');
    if (!chartState) {
      setChartState(new D3BasicAreaChart(chartRef.current, data));
    } else {
      chartState.update(data);
    }
  }, [chartState, data]);

  return (
    <div
      className="dashboard__basic-are-chart"
      style={{ width: 'inherit', height: 'inherit' }}
      ref={chartRef}
    >
      <h2>BasicAreaChart</h2>
    </div>
  );
};

export default BasicAreaChart;
