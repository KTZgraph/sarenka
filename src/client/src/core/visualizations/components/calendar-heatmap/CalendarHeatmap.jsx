import { useEffect, useRef, useState } from 'react';

import useResizeObserver from '../../../../hooks/useResizeObserver';

import D3CalendarHeatmap from './D3CalendarHeatmap';
import './CalendarHeatmap.scss';

const randomNumbers = () => {
  return Array.from(
    { length: 12 },
    () => Math.floor(Math.random() * 100) + 1
  );
};

const DUMMY_DATA = [
  {
    Day: 'Mon',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Tue',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Wed',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Thu',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Fri',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Sat',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
  {
    Day: 'Sun',
    Frequency: { AM: randomNumbers(), PM: randomNumbers() },
  },
];

const CalendarHeatmap = () => {
  const wrapperRef = useRef(null);
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);
  const [data, setData] = useState(DUMMY_DATA);
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    console.log('----- CalendarHeatmap ----- ');
    console.log('----- CalendarHeatmap dimensions----- ');
    console.log('dimensions: ', dimensions);

    // jak nie ma rozmiaru dimensions to nic nie robię
    if (!dimensions) return;

    if (!chartState) {
      setChartState(
        new D3CalendarHeatmap(chartRef.current, data, dimensions)
      );
    } else {
      chartState.update(data, dimensions);
    }
  }, [chartState, data, dimensions]);

  return (
    <div
      className="visualizations__calendar-heatmap"
      ref={wrapperRef}
    >
      <svg
        className="calendar-heatmap-svg"
        id="calendar-heatmap-id"
        ref={chartRef}
      ></svg>
    </div>
  );
};

export default CalendarHeatmap;
