import { useRef, useEffect, useState } from 'react';
import D3ChartOne from './D3ChartOne';

import './ChartWrapperOne.scss';

const ChartWrapperOne = ({ data }) => {
  // Integrating with third-party DOM libraries.  https://reactjs.org/docs/refs-and-the-dom.html
  const chartAreaOne = useRef(null);
  const [chartOne, setChartOne] = useState(null);

  useEffect(() => {
    // FIXME - dodaje dwa svg komponenty
    // Similar to componentDidMount and componentDidUpdate:

    if (!chartOne) {
      // chart hasn't been set - create the chart
      setChartOne(new D3ChartOne(chartAreaOne.current));
    } else {
      // after chart has been set - update the chart
      //   chart.update();
      //   chart.update(data);
    }
    // DEPENDENCY ARRAY
    // This isn't strictly necessary in our example,
    // but it's best practice with the useEffect hook to include any variables inside inside of our function as a dependency,
    //  and ESLint will yell at us if we leave this out
    //   }, [chart]);
  }, [chartOne, data]);

  return <div className="chart-area-one" ref={chartAreaOne}></div>;
};

export default ChartWrapperOne;
