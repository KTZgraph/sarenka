import { useState } from 'react';
import RacingBarChart from './RacingBarChart';
import useInterval from './useInterval';

const getRandomIndex = (array) => {
  return Math.floor(array.length * Math.random());
};

const RacingBarChartApp = () => {
  const [iteration, setIteration] = useState(0);
  const [start, setStart] = useState(false);
  const [data, setData] = useState([
    {
      name: 'alpha',
      value: 10,
      color: '#f4efd3',
    },
    {
      name: 'beta',
      value: 15,
      color: '#cccccc',
    },
    {
      name: 'charlie',
      value: 20,
      color: '#c2b0c9',
    },
    {
      name: 'delta',
      value: 25,
      color: '#9656a1',
    },
    {
      name: 'echo',
      value: 30,
      color: '#fa697c',
    },
    {
      name: 'foxtrot',
      value: 35,
      color: '#fcc169',
    },
  ]);

  useInterval(() => {
    // co 500 ms iterują po danych i wybieram jeden z obiektów/koni i zwiększam tego obiektu wartości
    if (start) {
      const randomIndex = getRandomIndex(data);
      setData(
        data.map((entry, index) =>
          index === randomIndex
            ? {
                ...entry,
                value: entry.value + 10,
              }
            : entry
        )
      );
      setIteration(iteration + 1);
    }
  }, 500);

  return (
    <>
      {/* wypisanie listy obiektów które bieżemy pod uwagę -  mapowanie wartosci */}
      {data.map((entry) => (
        <span key={entry.name}>{entry.name}</span>
      ))}

      <h1>Racing Bar Chart</h1>
      {/* potem te dane przekazuję do komponentu */}
      <RacingBarChart data={data} />
      <button onClick={() => setStart(!start)}>
        {start ? 'Stop the race' : 'Start the race!'}
      </button>
      <p>Iteration: {iteration}</p>
    </>
  );
};

export default RacingBarChartApp;
