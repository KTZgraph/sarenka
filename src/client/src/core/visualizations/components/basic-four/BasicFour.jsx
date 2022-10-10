// scaleBand jest fajne do charBar bo pierwszy słuepk powiedzmy szerokości 50px byłby w półowie zeżarty przez oś Y z lewej/ czy zakończenie pola svg z leve
// żeby to rozwiazać trzeba by się nagimnastykować z marginami, matmą i tak dalej

import {
  select,
  axisBottom,
  scaleLinear,
  axisRight,
  scaleBand,
} from 'd3';
import { useRef, useEffect, useState } from 'react';

const BasicFour = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20, 65, 75]);
  const svgRef = useRef();

  useEffect(() => {
    const svg = select(svgRef.current);

    const xScale = scaleBand()
      // scaleBand bieże domain i dzieli tutaj na 5 równych kawałków dlatego się nazywa scaleBand
      //   .domain([0, 15, 26, 37, 48]) też sprawi że mam podziałkę na 5 równych elementów
      //   ale nie są liniowo rozłożonwe bo scaleBand tego nie umie, a scaleLinear już umie sobie ciągłe wartości obliczyć
      //   WARNING scaleBand().domain([el1explicite, el2explicite, el3explicite]) tutaj w .domain trzeba być expilici co mapujemy - dlatego lista konkretnych elementów
      //   wartosci takie jak indeksy danych
      //   .domain([0, 1, 2, 3, 4, 5, 6])
      //   szybszy sposób na wyplucie lementów przez dfunkcje map na Array data
      .domain(data.map((value, index) => index))
      .range([0, 300])
      //   padding, bo inmaczej wszsytkie słupki są sklejone bokami do siebie
      .padding(0.5);

    const yScale = scaleLinear().domain([0, 150]).range([150, 0]);

    // do kolorowanie słupków - liniowa skala kolorów
    // BUG skala liniowa nie jest jakoś super do generowanioa palety kolorów
    const colorScale = scaleLinear()
      // ttuaj żaden słupek nie jest w pełni zielony ani w pełni czerwony ze względu na wartości
      // .domain([0, 150])
      // teraz dopier słupki powyżej 75 będą się "zaczerwieniać"
      //   .domain([75, 150]) jak się tak zostawi a mapuje trzy kolory to czerwony NIE jest nigdy wykosztywywany
      .domain([75, 100, 150]) //teraz 100 będzie pomarańczowe
      //WARNING   jak się tak zostawi samo .domain([75, 150]).range(["green", "red"]) to albo się słupki robią Bardziej Zielone jeśli mogą, albo bardziej zaczerwienieją co NIE jest fajne
      //   .range(["green", "red"]) jak się tak zsotawi to z zielonego rpzechodiz na brzydki braz i dopiero potem czerwony
      .range(['green', 'orange', 'red']) //rozwiazanie brdzydkiego przejsci akolorostycznego przez brzydki brąz
      //  WARNING  clamp(true) upewnia że wartości poniżej 75 dalej zwrócą te wartośc zwrócone przez .range(["green", "red"])
      .clamp(true);

    // nie trzeba już dodawac  + 1 do ticksów osi
    const xAxis = axisBottom(xScale).ticks(data.length);

    svg
      .select('.x-axis')
      .style('transform', 'translateY(150px)')
      .call(xAxis);

    const yAxis = axisRight(yScale);
    svg
      .select('.y-axis')
      .style('transform', 'translateX(300px)')
      .call(yAxis);

    // wybór wszystkich elem,entów z klasą .bar i synchroznizuję je z lista danych któe mam
    // join - tutaj tylko domyslne callbacki używam to się nie bawie w te trzy calbacki dla ENTER, UPDATE ,EXIT
    // BUG  metoda .on na d3.js nie ma indexy, a potrzebuję go do wypozycjonowania napisu nad słupkiem
    // BUG - to nie działa https://stackoverflow.com/questions/64910052/d3-js-v6-2-get-data-index-in-listener-function-selection-onclick-listene

    svg
      .selectAll('.bar')
      .data(data)
      .join('rect')
      // WARNING - WAŻNE po metodzie join():  dla każdego elementu enter, i update dodaję atrybut klasy
      .attr('class', 'bar')
      // wypełnianie odcnieniami kolorów ze skali liniowe od zielonego do czerwonego
      //  WARNING  jak tu się zostawi .attr("fill", colorScale) to kolorwanie nie jest animowae ;/
      //   .attr("fill", colorScale)
      //   scalowanie po osi X słupków - rozmieszczenie na osi X
      .attr('x', (value, idx) => xScale(idx))
      //   chcę żeby słupki miały szerokość jak pasma (podizałkę na równe cześci pionowo)
      .attr('width', xScale.bandwidth())
      //   ładna animacja rośniecia słupków
      //   .transition() są animowane ale jakby od złej strony bo wydają się "podskakiwać"
      //   to dlatego bo origin każdego słupka to jego gora lewo brzeg tak jak w SVG
      //   WARNING - robimy sztuczkę z obracaniem do góry nogami słupkwó, zeby mieć ładną animację
      //   BUG .style("transform", "scale(1, -1)")  teraz znikneły słupki bo D3.js zawsze transformuje względem swojego punku (0,0) czyli góra lewo
      .style('transform', 'scale(1, -1)')
      //   skaluje słupki tak, żeby pasowała wysokosc do WARTOSCI  na osi Y
      //   .attr("y", yScale) To źle działa - słupki wyskauję na druga strone do góry
      //   trzeba prznenieść po odbiciu ich w dół o wysokosć wykresu
      .attr('y', -150)
      // WARNING WAŻNE ZDARZENIE PRZEZ .transition() - interkatywnosc wykresu przed animacją transition
      //   BUG w zdarzeniu pierwszy jest obiekt event nie ma idx
      //   BUG ustawianie lokalnego indexu dla każdego  bo już w D3.js nowej wersji go nie ma

      .on('mouseenter', (event, value) => {
        // callback gdy jest zdarzenie to d3 zsycnchronizuj się proszę z elemtani o klasi tooltip z danymi od pojkedynczej wartosci - z której robię listę
        // będę mieć tylko jeden tooltip w jednym momencie
        // .join utworzy nowy text element dla każdego fragmentu danych
        // teraz każdy element enter i update dostanie atrybut klasy tooltip

        // metoda .on na d3.js nie ma indexy, a potrzebuję go do wypozycjonowania napisu nad słupkiem
        // WARNING WSZEDZIE używamy tego samego elementu tylko zaktualizowanego napisu
        svg
          .selectAll('.tooltip')
          .data([value])
          //   .join("text")
          // zmieniam tak pozycję enter elementu żeby nie leciał z samiutkiej góry wykresu
          .join((enter) =>
            enter.append('text').attr('y', yScale(value) - 4)
          )
          .attr('class', 'tooltip')
          .text(value)
          //   wyśrodkowanie tekstu
          .attr('text-anchor', 'middle')
          //   BUG - rozwiazanie szerokośći - pobranie pozycji X dadego słupka/prostokąta!
          //   .attr("x", xScale(idx))
          // BUG trzeba odjąć szerokość svg
          .attr('x', event.target.getBoundingClientRect().x)
          //   BUG responswywność
          //   WARNING PRZESUNIECIE w lewo o SZEROKOŚĆ wyresu z osią Y
          .style('transform', 'translate(-180px)')

          .transition()
          //   żeby napis był w pełni nasycenia - animacja
          .attr('opacity', 1)
          // WARNING   dodatkowo animuję jakby napis z góy szedł w dół spadał, NIE ŁADNA :< - dlatego zmienian na .join((enter) => enter.append("text").attr("y", yScale(value) - 4))
          //   wysokosć napisue się zgadza dodatkowo -7 żeby był ciut nad słupkiem napis
          .attr('y', yScale(value) - 7);

        console.log(event.target.getBoundingClientRect().x);
      })
      //   usuwanie napisu po odjechaniu myszką ze słupka - żeby znikał
      .on('mouseleave', () => svg.select('.tooltip').remove())
      .transition()
      // WARNING- WYOSOKOŚĆ słupków po transition, bo to właśnie ją chcemy animować - rośniecie
      // WARNING tu dziwne wysokość słupków - oś Y od wysokosci trzeba odjać WARTOSC Y jaką miałby słupek bo całośc rośnie w dół
      .attr('height', (value) => 150 - yScale(value))
      .attr('fill', colorScale);
  }, [data]);

  return (
    <>
      <svg ref={svgRef} style={{ overflow: 'visible' }}>
        <g className="x-axis" />
        <g className="y-axis" />
      </svg>
      <br />
      <button onClick={() => setData(data.map((value) => value + 5))}>
        Update data
      </button>
      <button
        onClick={() => setData(data.filter((value) => value < 35))}
      >
        Filter data
      </button>
      <button
        onClick={() =>
          setData([...data, Math.floor(Math.random() * 140)])
        }
      >
        Add data
      </button>
    </>
  );
};

export default BasicFour;
