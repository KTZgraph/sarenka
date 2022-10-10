import { useState } from 'react';
import AnimatedTreeChart from './AnimatedTreeChart';

const initialData = {
  name: 'frameworks',
  children: [
    {
      name: 'joomla',
      children: [
        {
          name: 'joomla-plugin-1',
        },
        {
          name: 'joomla-plugin-2',
        },
        {
          name: 'joomla-plugin-3',
        },
      ],
    },
    {
      name: 'wordpress',
    },
  ],
};

const AnimatedTreeChartApp = () => {
  const [data, setData] = useState(initialData);

  return (
    <div
      style={{
        marginBottom: '2rem',
        width: '100%',
        height: '100%',
        overflow: 'visible',
      }}
    >
      <h1>Animated Tree Chart</h1>
      <AnimatedTreeChart data={data} />
      <button onClick={() => setData(initialData.children[0])}>
        Update data
      </button>
    </div>
  );
};

export default AnimatedTreeChartApp;
