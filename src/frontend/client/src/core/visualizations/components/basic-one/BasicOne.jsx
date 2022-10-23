import { useRef, useEffect, useState } from 'react';
import { select } from 'd3';
import './BasicOne.scss';

const BasicOne = () => {
  // useRef po to, że gdy po raz pierwszy element html zostanie wyrenderowany to mamy do niego dostęp
  const svgRef = useRef();
  const [data, setData] = useState([25, 30, 45, 60, 20]);

  useEffect(() => {
    // uruchomiono po raz pierwszy raz gdy DOM element się wyrenderuje
    // kolejne gdy rzeczy z dependency array się zmienią
    // opakowanie ref do D3
    const svg = select(svgRef.current);

    // renderowanie kółek na podstawie dancyh
    // mówię d3 żeby wybrała wszystkie kółka które znajdujesz w svg i zsynchronizuj je z danymi; ale tutja nie ma żadnych kółek
    // dlatego na początku daję Ci dane przez .data, niie musisz aktualizuzowac żadnych danych, bo ich nie masz w svg
    // i nie musisz usuwać żadnych kółek bo też ich nie masz
    svg
      .selectAll('circle')
      .data(data)
      // coi chcesz zrobić z elementami któe chcmey UPDATE i EXIT
      // dla .join trzeba stworzyć callbacka dla każdego elementu
      // pierwszy callback to enter callback - mówi co chcę zrobić z nowymi piece od data
      //   frugi callback to co chcemy zorbić z zatuaklziowanymi danymi
      //   trzeci callback - coc chcę zrobić z danymi które chcę usunąć

      // WARNING  .join('circle') gdy nie potrzeba callbacków
      .join(
        (enter) =>
          enter
            .append('circle')
            .attr('class', 'new')
            .attr('r', (value) => value)
            .attr('cx', (value) => value * 2)
            .attr('cy', (value) => value * 2)
            .attr('stroke', 'red'),
        (update) => update.attr('class', 'updated'),
        (exit) => exit.remove()
      )
      // po join atrybuty będą mieć wpływa dla obu enering and updating elements
      .attr('r', (value) => value)
      .attr('cx', (value) => value * 2)
      .attr('cy', (value) => value * 2)
      .attr('stroke', 'red');
  }, [data]);

  return (
    <>
      <svg ref={svgRef} className="basic-one__svg"></svg>
      <button onClick={() => setData(data.map((value) => value + 5))}>
        Update data
      </button>

      <button
        onClick={() => setData(data.filter((value) => value < 35))}
      >
        Filter data
      </button>
    </>
  );
};

export default BasicOne;
