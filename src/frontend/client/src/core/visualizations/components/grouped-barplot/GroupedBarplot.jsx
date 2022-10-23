import { useEffect, useRef, useState } from 'react';
import D3GroupedBarplot from './D3GroupedBarplot';

const DUMMY_DATA = [
  { group: 1, critical: 32, high: 129, medium: 228, low: 304 },
  { group: 2, critical: 74, high: 163, medium: 259, low: 192 },
  { group: 3, critical: 29, high: 197, medium: 170, low: 395 },
  { group: 4, critical: 100, high: 107, medium: 273, low: 316 },
  { group: 5, critical: 22, high: 100, medium: 273, low: 485 },
  { group: 6, critical: 53, high: 118, medium: 183, low: 485 },
  { group: 7, critical: 53, high: 178, medium: 274, low: 269 },
  { group: 8, critical: 50, high: 193, medium: 192, low: 252 },
  { group: 9, critical: 89, high: 116, medium: 244, low: 199 },
  { group: 10, critical: 80, high: 125, medium: 190, low: 393 },
  { group: 11, critical: 46, high: 115, medium: 122, low: 309 },
  { group: 12, critical: 28, high: 149, medium: 246, low: 484 },
];

// BUG group musi zostać
const DUMMY_DATA_COLUMNS = [
  'group',
  'critical',
  'high',
  'medium',
  'low',
];

const GroupedBarplot = () => {
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);

  useEffect(() => {
    console.log('----- GroupedBarplot ----- ');
    if (!chartState) {
      setChartState(
        new D3GroupedBarplot(
          chartRef.current,
          DUMMY_DATA,
          DUMMY_DATA_COLUMNS
        )
      );
    } else {
      chartState.update(DUMMY_DATA, DUMMY_DATA_COLUMNS);
    }
  }, [chartState]);

  return (
    <div className="visualizations__grouped-barplot" ref={chartRef}></div>
  );
};

export default GroupedBarplot;
