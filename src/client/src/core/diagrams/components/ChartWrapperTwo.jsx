import { useRef, useEffect, useState } from 'react';

import D3ChartTwo from './D3ChartTwo';

import './ChartWrapperTwo.scss';

const ChartWrapperTwo = ({ data }) => {
  const chartAreaTwo = useRef(null);
  const [chartTwo, setChartTwo] = useState(null);

  useEffect(() => {
    // FIXME - dodaje dwa svg komponenty
    // Similar to componentDidMount and componentDidUpdate:

    if (!chartTwo) {
      // chart hasn't been set - create the chart
      setChartTwo(new D3ChartTwo(chartAreaTwo.current));
    } else {
      // after chart has been set - update the chart
      //   chart.update();
      //   chart.update(data);
    }
  }, [chartTwo, data]);

  return <div className="chart-area-two" ref={chartAreaTwo}></div>;
};

export default ChartWrapperTwo;
