/*
 * https://www.youtube.com/watch?v=J81Hghazii8&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=14
 */
import PhysicsBasedForceLayout from './PhysicsBasedForceLayout';

const data = {
  name: 'frameworks',
  children: [
    {
      name: 'joomla',
      // keyword "children" jest ważny dla D3.js
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

const PhysicsBasedForceLayoutApp = () => {
  return <PhysicsBasedForceLayout data={data} />;
};

export default PhysicsBasedForceLayoutApp;
