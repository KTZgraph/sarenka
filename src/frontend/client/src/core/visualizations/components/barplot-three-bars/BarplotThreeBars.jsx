import { useEffect, useRef, useState } from 'react';
import { csv } from 'd3';
import D3BarplotThreeBars from './D3BarplotThreeBars';

const URL_TMP =
  'https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/data_stacked.csv';

const BarplotThreeBars = () => {
  const chartRef = useRef(null);
  const [chartState, setChartState] = useState(null);

  useEffect(() => {
    console.log('----- BarplotThreeBars ----- ');
    if (!chartState) {
      csv(URL_TMP).then((dataArray) => {
        if (dataArray.length === 0) return;
        setChartState(
          new D3BarplotThreeBars(chartRef.current, dataArray)
        );
      });
    } else {
      csv(URL_TMP).then((dataArray) => {
        if (dataArray.length === 0) return;
        chartState.update(dataArray);
      });
    }
  }, [chartState]);

  return (
    <div
      className="dashboard__barplot-three-bars"
      id="dashboard__barplot-three-bars-id"
      ref={chartRef}
    ></div>
  );
};

export default BarplotThreeBars;
