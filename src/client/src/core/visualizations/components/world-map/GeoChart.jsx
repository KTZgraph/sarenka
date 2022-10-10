/*
https://www.youtube.com/watch?v=gGORNzKIXL4&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=13
kule ziemi trzeba zamienić na piskelowe wartości mapy
https://github.com/d3/d3-geo#azimuthal-projections

geoPath z d3.js - zwraca funkcję która otrzymuje jakiś geo.json data or features in a GEO JSON file or countires in our case as an input
and transform them into "d" atributes of a <path> element in ans SVG
- co chcemy zrobić to wyrenderować <path> element dla każdego kraju w świecie i połaczyć te atrybuty  "d" żeby zdefiniowac ich kształt

*/

import { useEffect, useRef } from 'react';
import { select, geoPath, geoMercator } from 'd3';
import useResizeObserver from '../../../../hooks/useResizeObserver';

/*
Component that renders a map of Germany
*/

const GeoChart = ({ data, property }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // will be called initially and on every data change
  useEffect(() => {
    const svg = select(svgRef.current);

    // use resized dimensions
    // but fall back to getBoundingClientReact, if no dimension yet
    //   WARNING optymalizacja - bo diemsnions na początku jest nullem
    const { widt, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   WARNING projects geo-coordinates on a 2D plane
    const projection = geoMercator();

    //WARNING   takes geojson data
    //WARNING   transform that into the d attribute of a path element
    //   pathGenerator tę funckje zwrca geoPath, funckaj użyta później do zamaiany jsona na kształty
    const pathGenerator = geoPath().projection(projection);

    //   WARNING general update pattern żeby wygenerować kształy krajów
    //    data.features z pliku jsona wszsytkie kraje ze światra
    svg
      .selectAll('.country')
      .data(data.features)
      //   na podstawie danych ma towrzyc elementy <path> svg
      .join('path')
      .attr('class', 'country')
      //   definiowanie kształtów krajów - atrybut "d" elementu <path> svg
      //   pathGenerator zwrócić prawidłowy atrybut d = "M100 100" i tak dalej
      .attr('d', (feature) => pathGenerator(feature));
  }, [data, dimensions, property]);

  return (
    <div ref={wrapperRef} style={{ marginBottom: '2rem' }}>
      <svg ref={svgRef}></svg>
    </div>
  );
};

export default GeoChart;
