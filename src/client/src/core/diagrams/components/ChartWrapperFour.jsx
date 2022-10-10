// tylko jedna funckja importowana
import { json } from 'd3';
import { useEffect, useRef, useState } from 'react';

import D3ChartFour from './D3ChartFour';
import Input from '../../../UI/Input';
import './ChartWrapperFour.scss';

const AddNewDataChartWrapperFour = ({
  data,
  setData,
  activeName,
}) => {
  const [name, setName] = useState('');
  const [height, setHeight] = useState('');
  const [age, setAge] = useState('');

  const handleRemove = (deleteName) => {
    const newData = data.filter((d) => {
      return d.name !== deleteName;
    });

    setData(newData);
  };

  const handleAdd = () => {
    setData((prevState) => [...prevState, { name, height, age }]);
    setName('');
    setAge('');
    setHeight('');
  };

  return (
    <div className="add-new-data">
      {data.map((student, idx) => (
        <div
          className={`row ${
            activeName === student.name ? 'row--active' : ''
          }`}
          key={idx}
        >
          <div className="col">{student.name}</div>
          <div className="col">{student.height}</div>
          <div className="col">{student.age}</div>
          <div className="col">
            <button
              onClick={() => handleRemove(student.name)}
              style={{ backgroundColor: 'orange' }}
            >
              delete
            </button>
          </div>
        </div>
      ))}
      <div className="row">
        <div className="col">
          <Input
            htmlFor="name"
            type="text"
            name="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="col">
          <Input
            htmlFor="height"
            type="text"
            name="height"
            value={height}
            onChange={(e) => setHeight(e.target.value)}
          />
        </div>
        <div className="col">
          <Input
            htmlFor="age"
            type="text"
            name="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
        </div>
        <div className="col">
          <button onClick={handleAdd}>Add</button>
        </div>
      </div>
    </div>
  );
};

const ChartWrapperFour = () => {
  const url = 'https://udemy-react-d3.firebaseio.com/children.json';
  const chartAreaFour = useRef(null);
  const [chartFour, setChartFour] = useState(null);
  const [data, setData] = useState([]);
  // rozwiazanie wielokrotnego ładowania https://stackoverflow.com/questions/70676777/useeffect-rendering-multiple-times-even-when-data-is-not-changing
  const [isLoading, setIsLoading] = useState(true);

  // do labelek gdy się kliknie na kółeczko - przekazane do D3js
  const [activeName, setActiveName] = useState('');

  useEffect(() => {
    // Similar to componentDidMount and componentDidUpdate:
    console.log(
      '------------------- ChartWrapperFour - useEffect -------------------'
    );

    if (!chartFour) {
      // pobieranie danych
      json(url)
        .then((dataArray) => {
          if (dataArray.length !== 0) {
            setIsLoading(true);
            setData(dataArray);
            setChartFour(
              new D3ChartFour(
                chartAreaFour.current,
                dataArray,
                setActiveName
              )
            );
            setIsLoading(false);
          }
        })
        .catch((error) => console.log(error));
    } else {
      chartFour.update(data, setActiveName);
    }
  }, [data, chartFour]);

  if (isLoading) return null;

  return (
    <div className="chart-wrapper-four">
      <div className="chart-wrapper-four__row">
        <div className="chart-wrapper-four__col">
          {/* wykres */}
          <div className="chart-area-four" ref={chartAreaFour}></div>;
        </div>
        <div className="chart-wrapper-four__col">
          {/* tabelka */}
          <AddNewDataChartWrapperFour
            data={data}
            setData={setData}
            activeName={activeName}
          />
        </div>
      </div>
    </div>
  );
};

export default ChartWrapperFour;
