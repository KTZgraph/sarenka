/*
https://youtu.be/bXN9anQN_kQ?t=391
d3.stack() główna cześć tego tutroialu 

Ogólnie w d3 to tte wszystkie funckje, zwracaja funckje generujące, które potem są wykorzytywnae 
const stackGenerator = stack(); tu też widać, że ta fucnkja zwraca funkcję
*/

import {
  select,
  scaleBand,
  axisBottom,
  stack,
  max,
  scaleLinear,
  axisLeft,
} from "d3";
import { useEffect, useRef } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const StackedBarChart = ({ data, keys, colors }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    // stack() - glówna cześć tego tutroialu
    // tnie dane na warstwy które mają być jedna nad drugą
    // te warstwy/layers są nazywane "series"
    const stackGenerator = stack()
      // musze wyrażnie powiedziec, które klucze wartości chcę żeby był nad soba, tutja keys jako props otrzymuję
      .keys(keys);

    //   zwracajedną listę długiosc 3 bo takie mamy klucze 3array z obiektami array długosc 5 bo 5 lat rtóżnych
    // widac że wartości sa takie jak mają być na słupku np dla babanaów dla roku 1990 to bedzie od 20 do 40px
    console.log(stackGenerator(data));

    // albo const series bo te poszatkowane przed d3.stack() wartwy sa w d3 też nazywane series
    // teraz tych wartw potrzebujemy do wygenerowania wartsw w naszym stack  bar chart
    // to ejszcze surowe dane jeszcze nie piksele
    const layers = stackGenerator(data);
    // maksymalna wartośc dancyh - żeby wiedziec jak oś OY ma być wysoka; ale exten to od razu lista od 0 bo wiem, yże minimum to 0 i tu można na sztywno
    // WARNING tu jakby trzeba dwa razy max liczyć, np sprawdzic ze najwyższe wartości sa dla jednego z trzech jedzeń (tutaj bakłażanów)
    //WARNING a potem wybrać największą wartość jednego bakłżana
    // sequence[1] dlatego że druga liczba pokazuje do czego dąży nasz bakłażac (np <od>46, <do>80 dla roku 2000 to nas interesuje 80)
    const extent = [
      0,
      max(layers, (layer) => max(layer, (sequence) => sequence[1])),
    ];

    console.log(extent);

    // teraz ośOY żeby zmapowac słupki wysokosci na piksele

    //   sklaa X jest potrzebna do xAxis
    const xScale = scaleBand()
      // domain input to lata, map zwraca listę
      //   scaleBand sykretna - lata
      .domain(data.map((d) => d.year))
      .range([0, width]);

    // WARNING OY
    //   sklaa OY tutaj liniowa
    const yScale = scaleLinear()
      // exten to wyżej obliżoczny max i to dla maskymalnego jedzczenia - bakłażana
      //   skala liniowa  - ciągłe dane
      .domain(extent)
      .range([height, 0]);

    //   ttuaj os OY która jest ciekawsza ze wzgledu na posztatkowane dane słupków
    // WARNING axis do stworzenia ZAWSZE wymaga skali, axisLeft to tick będa po lewej
    // tu akkurat nie trzeba odbijać
    const yAxis = axisLeft(yScale);
    // teraz dodać do svg
    svg.select(".y-axis").call(yAxis);

    // WARNING - dodawanie danych od - trudne podwójny sleect danych
    //**** rendering  *********************************************** */
    svg
      .selectAll(".layer")
      .data(layers)
      // dla każdej grupy stwórz mi proszę nową grupoę g
      .join("g")
      //   WARNING wszsytko napisane po tym join, jest uruchaminiane dla każdej grupy czyli trzy razy
      // dodaje klase, zeby można je było potem updatować
      .attr("class", "layer")
      //   hej, d3 dla wszystkich grup które stworzyłeś, prozszę wybierz wszystkie istniejące prostokąty (po jednym dla jedzonka jednego)
      // i zsynchronizuje je z danymi - dane to jedna wartwa z katulanego zbioru layers
      // teraz tworzymy nowy prostokąt dla każdej sekwnecji tej warstwy
      .selectAll("rect")
      //   to layer ejst z brane z grupy w której aktualnie jesteśmy
      .data((layer) => layer)
      //   teraz można join żeby stworzył prostokąt dla każdej tej wartswy
      .join("rect");

    //******************************************************************** */

    // WARNING OX
    // renderuje oś X axisBottom osniosi się do ticks a nie do samej pozycji opsić która domyslnie będzie od gróy svg
    const xAxis = axisBottom(xScale);
    // teraz dodać do svg
    svg
      .select(".x-axis")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);
  }, [colors, data, dimensions, keys]);

  return (
    <>
      <div
        ref={wrapperRef}
        style={{
          marginBottom: "2rem",
          overflow: "visible",
          width: "100%",
          height: "100%",
          padding: "40px",
          minHeight: "500px",
        }}
      >
        <svg
          ref={svgRef}
          style={{ overflow: "visible", width: "100%", height: "100%" }}
        >
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default StackedBarChart;
