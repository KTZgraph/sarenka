import { useState } from 'react';
import GeoChart from './GeoChart';
// WARNING ważny format jsona, który d3.js używa do renderowania krajów i ich kształtów
//geojson-maps.ash.ms/
// każdy kraj jest zdefuniowany jako feature
import data from './GeoChart.world.geo.json';

import './WorldMapApp.scss';
const WorldMapApp = () => {
  const [property, setProperty] = useState('pop_est');

  return (
    <div className='world-map-app'>
      <h2>World Map with d3-geo</h2>
      <GeoChart data={data} property={property} />
      <h2>Select property to highlight</h2>
      <select
        value={property}
        onChange={(event) => setProperty(event.target.value)}
      >
        <option value="pop_est">Population</option>
        <option value="name_len">Name length</option>
        <option value="gdp_md_est">GDP</option>
      </select>
    </div>
  );
};

export default WorldMapApp;
