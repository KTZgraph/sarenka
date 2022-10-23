import { useRef, useEffect, useState } from 'react';
import D3ChartThree from './D3ChartThree';

import Dropdown from '../../../UI/Dropdown';
import './ChartWrapperThree.scss';

const genderOptions = [
  { label: 'Men', value: 'men' },
  { label: 'Women', value: 'women' },
];

const ChartWrapperThree = ({ data }) => {
  const chartAreaThree = useRef(null);
  const [chartThree, setChartThree] = useState(null);
  const [genderSelected, setGenderSelected] = useState('men');
  useEffect(() => {
    // FIXME - dodaje dwa svg komponenty
    // Similar to componentDidMount and componentDidUpdate:

    if (!chartThree) {
      // chart hasn't been set - create the chart
      //   WARNING - nie działa odświeżanie na zmianę stanu genderSelected - trzeba dwa useEffect z innymi dependency wywołać
      setChartThree(
        new D3ChartThree(chartAreaThree.current, genderSelected)
      );
    } else {
      // after chart has been set - update the chart
      //   chart.update();
      //   chart.update(data);
    }
  }, [chartThree, data, genderSelected]);

  useEffect(() => {
    setChartThree(
      new D3ChartThree(chartAreaThree.current, genderSelected)
    );
  }, [genderSelected]);

  return (
    <div className="chart-area-three-container">
      {/* dropdown do wyboru wykresu */}
      <div className="chart-area-three__row">
        <div className="chart-area-three__col">
          <Dropdown
            label="Please select gender"
            options={genderOptions}
            value={genderSelected}
            onChange={(e) => {
              setGenderSelected(e.target.value);
              console.log('e.target.value: ', e.target.value);
            }}
          />
        </div>
      </div>
      <div className="chart-area-three__row">
        <div className="chart-area-three__col"></div>
      </div>
      <div className="chart-area-three" ref={chartAreaThree}></div>
    </div>
  );
};

export default ChartWrapperThree;
