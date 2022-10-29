import { useRef, useEffect } from 'react';
import { select, scaleBand, scaleLinear, max } from 'd3';
import useResizeObserver from '../../../../hooks/useResizeObserver';

const RacingBarChart = ({ data }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // will be called initially and on every data change
  useEffect(() => {
    const svg = select(svgRef.current);
    if (!dimensions) return;

    // sorting the data
    data.sort((a, b) => b.value - a.value);

    const yScale = scaleBand()
      // mapowanie, zeby wyszła lista indeksów/cyfr [0,1,2,3,4,5]
      .domain(data.map((value, idx) => idx)) //[0,1,2,3,4,5]
      //   mapowanie na piksele
      .range([0, dimensions.height]) // [0, 200 (example)]
      //   padding w poziomie danych
      .paddingInner(0.1);

    const xScale = scaleLinear()
      // bieże wartosc konia np 0 | nawjyższąw artośc - ostatniego konia
      //   tutaj mapujemy już liniowe wartości inputu na linioowy zakres outputowch/pikseli wartości
      .domain([0, max(data, (entry) => entry.value)]) //[0, 65(example)]
      //   mapowanie na piksele od 0 | mapuje na cała szerokosc svg
      .range([0, dimensions.width]); //[0, 400 (example)]

    // draw the bars
    svg
      .selectAll('.bar')
      //   tutaj nie srotuje protokątów po wartościach
      // .data(data)
      //   dodanie kluczy żeby sortować po prostokątach
      //   .data(data, (entry, idx) => idx) // domyślnie sortuje po indeksach
      //   WARNING - teraz zmienia i animuje kolejnosć prostokątów, A NIE tylko przeskakuje kolor zależnei od długośći
      .data(data, (entry, idx) => entry.name)
      //  BUG  tutaj te prostokąty jakby z góry wlatują - NIE ładna animacja
      //   .join("rect")
      // poprawka żeby od razu prostokąty były na swoim miejscu
      .join((enter) =>
        //   callback enter tylko dla nowych elementów - efekt po odświeżeniu
        //   dodaję atrybut Y bo prostokąy też mają go od razu
        enter.append('rect').attr('y', (entry, idx) => yScale(idx))
      )
      .attr('class', 'bar')
      .attr('x', 0)
      .attr('width', (entry) => xScale(entry.value))
      //   od tego momentu chcę animować zmiany żeby tak "nie skakało"
      .transition()
      .attr('y', (entry, idx) => yScale(idx))
      .attr('height', yScale.bandwidth())
      //   mapowanie kolórw z listy danych
      .attr('fill', (entry) => entry.color);

    // draw the labels - informacje na prostokątach
    // podobne do tworzenia prostokątów, z tym, ze tutaj to jest text
    svg
      .selectAll('.label')
      .data(data, (entry, idx) => entry.name)
      //   pozbycie się bryzdkiej animacji - uzycie callbacka enter w join
      //   .join("text")
      .join((enter) =>
        //   callback enter tylko dla nowych elementów - efekt po odświeżeniu
        enter
          .append('text')
          //   chcę żby od razu miało atrybut Y i nie wjeżdżało dziwnie
          .attr(
            'y',
            (entry, index) =>
              yScale(index) + yScale.bandwidth() / 2 + 5
          )
      )
      .text((entry) => `${entry.name} (${entry.value} meters)`)
      .attr('class', 'label')
      .attr('x', 10)
      .transition()
      .attr(
        'y',
        (entry, index) => yScale(index) + yScale.bandwidth() / 2 + 5
      );

    //   koniec useEffect
  }, [data, dimensions]);

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
      ></svg>
    </div>
  );
};

export default RacingBarChart;
