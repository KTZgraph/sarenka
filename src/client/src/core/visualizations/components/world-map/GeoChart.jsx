/*
https://www.youtube.com/watch?v=gGORNzKIXL4&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=13
kule ziemi trzeba zamienić na piskelowe wartości mapy
https://github.com/d3/d3-geo#azimuthal-projections

geoPath z d3.js - zwraca funkcję która otrzymuje jakiś geo.json data or features in a GEO JSON file or countires in our case as an input
and transform them into "d" atributes of a <path> element in ans SVG
- co chcemy zrobić to wyrenderować <path> element dla każdego kraju w świecie i połaczyć te atrybuty  "d" żeby zdefiniowac ich kształt

*/

import { useEffect, useRef, useState } from 'react';
import {
  select,
  geoPath,
  geoMercator,
  min,
  max,
  scaleLinear,
} from 'd3';
import useResizeObserver from '../../../../hooks/useResizeObserver';
import { width } from '@mui/system';

/*
Component that renders a map of Germany
*/

const GeoChart = ({ data, property }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // stan do przechowywania wybranego kraju
  const [selectedCountry, setSelectedCountry] = useState(null);

  // will be called initially and on every data change
  useEffect(() => {
    console.log('wrapperRef.current.getBoundingClientRect()');
    console.log(wrapperRef.current.getBoundingClientRect());
    const svg = select(svgRef.current);

    //   minimla i maksywamlna wartośc po prosty wybranego z selecta
    const minProp = min(
      data.features,
      (feature) => feature.properties[property]
    );
    const maxProp = max(
      data.features,
      (feature) => feature.properties[property]
    );

    //   skala kolorów żeby pokazac natężenie dancyh
    const colorScale = scaleLinear()
      .domain([minProp, maxProp])
      .range(['#ccc', 'red']);

    console.warn(minProp, maxProp);

    // use resized dimensions
    // but fall back to getBoundingClientReact, if no dimension yet
    //   WARNING optymalizacja - bo diemsnions na początku jest nullem
    // if (!dimensions) return;

    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   WARNING projects geo-coordinates on a 2D plane
    // const projection = geoMercator();
    //  WARNING fitSize() tak żeby się mapa zmienśiła do dimensions które musze podać i musze dać referencję
    const projection = geoMercator().fitSize(
      // TODO - poprawocwać nad procentami ekranu
      [width, height],

      //  selectedCountry  to obiet z listy data.features[isdx] //generuje KRAJ- przybliża
      // WARNING jeśli wybraliśmy kraj, to on ma się renderować zamiast całej mapy
      // FIXME - coś po klikaniu źle przybliża
      selectedCountry || data
    );

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
      // po kliknieciu na kraj ustawiam stan/zmienną na wybrany tego kraju
      .on('click', (event, feature) => {
        console.log('setSelectedCountry');
        setSelectedCountry(feature);
      })
      .attr('class', 'country')
      // skla kolorystyczna do wypełnianie krajów
      // wartosc z obiekty jego pola  po kluczu z selecta
      .attr('fill', (feature) =>
        colorScale(feature.properties[property])
      )
      //   definiowanie kształtów krajów - atrybut "d" elementu <path> svg
      //   pathGenerator zwrócić prawidłowy atrybut d = "M100 100" i tak dalej
      .attr('d', (feature) => pathGenerator(feature));
  }, [data, dimensions, property, selectedCountry]);

  return (
    <div
      ref={wrapperRef}
      style={{
        marginBottom: '2rem',
        width: '100%',
        height: '100%',
        overflow: 'visible',
        background: 'green',
        display: 'flex',
        alignItems: 'center',
        // pdding dlatego, że od zero , zero pod sidebar chce być
        padding: '150px',
      }}
    >
      <svg
        ref={svgRef}
        style={{
          width: '100%',
          height: '100%',
          overflow: 'visible',
        }}
      ></svg>
    </div>
  );
};

export default GeoChart;
