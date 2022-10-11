/*
https://www.youtube.com/watch?v=ww54a4Xbdds&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=17
scalePoint() - skla dla wykresy chart area
*/

import {
  select,
  scaleBand,
  axisBottom,
  stack,
  max,
  scaleLinear,
  axisLeft,
  stackOrderAscending,
  area, // funckja do tworsenai wykresów area
  scalePoint,
  curveCardinal, // zakrzywienie do funckji generejuącej char area areaGenerator
} from "d3";
import { useEffect, useRef } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const StackedAreaChart = ({ data, keys, colors }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();
    const stackGenerator = stack()
      .keys(keys)
      // sortowanie jest dobrowolne - teraz jedzonko, które ma najmneijsze wartości będzie na dolną wartswą w area chart
      //  BUG  ale jak to się usunie i potem odklika awokado, a potem znowu zaklika, zeby były dane widoczne to dodaj na smej górze tę warstwę
      .order(stackOrderAscending);
    const layers = stackGenerator(data);
    const extent = [
      0,
      max(layers, (layer) => max(layer, (sequence) => sequence[1])),
    ];

    // WARNING scale Band fajny do słupkowych, ale tutaj sprawia ze ostatni słupek wydaje się pusty,
    // WARNING bo dane sa reprezentowane przez wysokosc po lewej i wykres wydaje się "ucięty" z prawe jakby bez wartości dla roku 2020
    // const xScale = scaleBand()
    // BUG -area chart to scala scalePoint
    // scalePoint zamiast podziału na pionowe fragmenty dzieli przesteżń wykresu na 5 punktów dla kazdej dekady i teraz nie ma już tej przerwy na końcu wykresu
    const xScale = scalePoint()
      .domain(data.map((d) => d.year))
      .range([0, width]);
    //   WARNING - do area chart trzeba usunac padding bo będzie wyśrodkowany wykres bna osi OX

    const yScale = scaleLinear().domain(extent).range([height, 0]);

    const yAxis = axisLeft(yScale);
    svg.select(".y-axis").call(yAxis);

    // WARNIGN area funckja z d3.js ktróa zwraca fumnckję
    const areaGenerator = area()
      // dane to te poszatkowane warstwy
      // współrzeda x to rok
      .x((sequence) => xScale(sequence.data.year))
      //   WARNING tricki - mamy dwie koordyunaty dla każdej z wartw - niższa np 20 dla bananów i wyższa na 45 dla mbananów
      .y0((sequence) => yScale(sequence[0]))
      //   górna wartosc w area
      .y1((sequence) => yScale(sequence[1]))
      //   .padding(0.25); // UWUWAMY
      // dodanie zakryzwenia/zaokrąglenioa do chartArea
      .curve(curveCardinal);

    // WARNING - zmiana na chartArea
    svg
      .selectAll(".layer")
      .data(layers)
      //   zamiast grupy <g> tworzymy ścieżki <path>
      .join("path")
      .attr("class", "layer")
      .attr("fill", (layer) => {
        console.log("layer", layer);
        return colors[layer.key];
      })
      //   atrybut d obiektu svg <path>
      //   teraz można przekazać layer jako argument do generatora area
      .attr("d", (layer) => areaGenerator(layer));
    //   ponizej skrótowy zapis
    //   .attr("d", areaGenerator);

    const xAxis = axisBottom(xScale);
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
          width: "80%",
          height: "300px",
          padding: "20px",
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

export default StackedAreaChart;
