import { useEffect, useRef, useState } from 'react';

import D3PieChartInteractive from './D3PieChartInteractive';

// create 2 data_set
const data1 = { a: 9, b: 20, c: 30, d: 8, e: 12 };
const data2 = { a: 6, b: 16, c: 20, d: 14, e: 19, f: 12 };

const PieChartInteractive = () => {
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  // WARNING  muszą być jakies wstępne dane do tego wykresu
  const [data, setData] = useState(data1);

  useEffect(() => {
    console.log('----- GroupedBarplot ----- ');
    if (!chartState) {
      setChartState(
        new D3PieChartInteractive(chartRef.current, data)
      );
    } else {
      chartState.update(data);
    }
  }, [chartState, data]);

  return (
    <div
      className="visualizations__pie-chart-interactive"
      ref={chartRef}
    >
      <button onClick={() => setData(data1)}>Data 1</button>
      <button onClick={() => setData(data2)}>Data 2</button>
    </div>
  );
};

export default PieChartInteractive;
