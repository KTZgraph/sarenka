// scaleTime przydatne do mapowania dat na 2008 do 2014 do sotępnej przestrzeni którą mamy w svg
// pozwoli wypozycjonować każdy epizod na osi OX zależnie od czasu

// axisBottom wygeneruje oś OX z ticks na dole

// <line> w svg ma 4 atrybuty x1 i y1 dla pierwszej kropki linii
// x2 i y2 dla drugiej kropki linii; te dwie koordynaty (x1, y1) i (x2, y2) są połąćzone i jest renderowana linia

// druga oś OY jest po to żeby zaznczyć na wysokości ile minut każda posttaci była w filmie - scaleLinear

import {
  select,
  min,
  max,
  scaleTime,
  scaleLinear,
  axisBottom,
} from 'd3';
import { useRef, useEffect } from 'react';

import useResizeObserver from '../../../../hooks/useResizeObserver';

const getDate = (dateString) => {
  // helper do pasowania dat z dnych
  const date = dateString.split('-');
  return new Date(date[2], date[0] - 1, date[1]);
};

const BreakingBadTimeline = ({ data, highligh }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // will be called initially and over on every data change
  useEffect(() => {
    const svg = select(svgRef.current);
    if (!dimensions) return;

    const minDate = min(data, (episode) => getDate(episode.air_date));
    const maxDate = max(data, (episode) => getDate(episode.air_date));

    console.log('minDate: ', minDate);
    console.log('maxDate:', maxDate);

    const xScale = scaleTime()
      // domain - wartości inputowe
      .domain([minDate, maxDate])
      // mapowanie na dostepne piksele
      .range([0, dimensions.width]);

    // druga skala OY, zeby zaznaczyć minuty ile osoba byla w filmie
    // WARNING oś OY rośnie w dół, więc zakres jest od max (dół wykresu) do zera (góra wykresu)
    const yScale = scaleLinear()
      .domain([
        // max i callback jak te dane mają być porównywane
        max(data, (episode) => episode.characters.length),
        0,
      ])
      // mapowanie na piksele
      .range([0, dimensions.height]);

    // linia dla każdego odcinka; klasa, zeby je potem aktualizować
    // WARNING selectAll a NIE .select !
    svg
      .selectAll('.episode')
      .data(data)
      .join('line')
      .attr('class', 'episode')
      // trzeba dac kolor żeby linia była widoczna
      // .attr("stroke", "black")
      // kolor zależnie od tego czy charakter istnieje
      .attr('stroke', (episode) =>
        episode.characters.includes(highligh) ? 'blue' : 'black'
      )
      // sama pozycja x zależy od samego w sobie epizodu a dokłądniej od jego daty
      .attr('x1', (episode) => xScale(getDate(episode.air_date)))
      .attr('y1', dimensions.height)
      // linia i tak będzie pionowa więc x1 i x2 to ta sama wpsółrzędna x1=x2
      .attr('x2', (episode) => xScale(getDate(episode.air_date)))
      // .attr("y2", 0); //cała wysokosć
      // zmiana, żeby wysokosc słupka odpowiadała ilości minut osoby na ekranie
      .attr('y2', (episode) => yScale(episode.characters.length));

    const xAxis = axisBottom(xScale);
    // dopisuje oś do grupy w środku svg
    svg
      .select('.x-axis')
      .call(xAxis)
      // BUG - pamiętać o px bo inaczej nie odbije względem osi Y wartosci, alebo coś dizwnego się dizeje
      .style('transform', `translateY(${dimensions.height}px)`);

    // draw the gauge
  }, [data, dimensions, highligh]);

  return (
    <div
      ref={wrapperRef}
      style={{
        marginBottom: '2rem',
        width: '100%',
        height: '100%',
        overflow: 'visible',
      }}
    >
      <svg
        ref={svgRef}
        style={{
          width: '100%',
          height: '100%',
          overflow: 'visible',
        }}
      >
        <g className="x-axis" />
      </svg>
    </div>
  );
};

export default BreakingBadTimeline;
