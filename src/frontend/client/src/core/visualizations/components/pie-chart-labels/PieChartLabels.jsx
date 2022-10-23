import { useEffect, useRef, useState } from 'react';

import D3PieChartLabels from './D3PieChartLabels';

import './PieChartLabels.scss';

function randomData() {
  var labels = [
    'Lorem ipsum',
    'dolor sit',
    'amet',
    'consectetur',
    'adipisicing',
    'elit',
    'sed',
    'do',
    'eiusmod',
    'tempor',
    'incididunt',
  ];

  return labels.map(function (label) {
    return { label: label, value: Math.random() };
  });
}

const PieChartLabels = () => {
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  // WARNING  muszą być jakies wstępne dane do tego wykresu
  const [data, setData] = useState(randomData);

  useEffect(() => {
    console.log('----- PieChartLabels ----- ');
    if (!chartState) {
      setChartState(new D3PieChartLabels(chartRef.current, data));
    } else {
      chartState.update(data);
    }
  }, [chartState, data]);

  return (
    <div className="visualizations__pie-chart-labels" ref={chartRef}>
      <button onClick={() => setData(randomData)}>randomize</button>
    </div>
  );
};

export default PieChartLabels;
