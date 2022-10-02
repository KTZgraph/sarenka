// https://www.youtube.com/watch?v=T1RgT0Yh1Lg

import { useEffect, useState, useRef } from "react";
import * as d3 from "d3";

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import "./Statistics.scss";

const Statistics = () => {
  // 1) Setup Initila data and settings -----------------------------------------------------------------------------
  const initialData = [
    {
      name: "Car", //oś X
      value: 10, // oś y
    },
    {
      name: "Food",
      value: 3,
    },
    {
      name: "Telephone",
      value: 9,
    },
    {
      name: "Electricity",
      value: 7,
    },
    {
      name: "Cinema",
      value: 7,
    },
  ];

  // dane do ustawienia chartów ich wygladau
  const width = 500;
  const height = 150;
  const padding = 20;
  const maxValue = 20; //Maximum data value

  const [chartdata, setChartdata] = useState(initialData);
  // DOM element for SVG
  const svgRef = useRef();

  // 2) Setup random data generator and SVG canvas ------------------------------------------------------------------

  const newData = () =>
    // zamiast fetcha losowe wartosci
    chartdata.map(function (d) {
      // nowa losowa wartośc max 20 bo taka wartośc ustailiśmy
      d.value = Math.floor(Math.random() * (maxValue + 1));
      return d;
    });

  useEffect(() => {
    // 3) Setup functions for Scales ----------------------------------------------------------------------------------
    // sclaes używane do mapowania danych w svg canvasie z reguły dużo oblizczeń jak przedstawić dane do fizycznego rozmiaru svg canvas /chart area
    // tutaj wymaga to trochę palnowania zanim rzeczywiscie coś anrysujemy
    // dla każdego chartu potrzebujemy scales żeby go narysować - wiec masz scale X i Y osi
    // WARNING musimy pamieać, zeby te funckje uruchomić w useEffect hook, chcemy jes tylko uruchomić gdy dane sie zmienią
    // X scales scalePoint- jeśli mamy jakieś słwoa, liczby
    // const xScale = d3.scalePoint().domain(['Car', 'food']);
    const xScale = d3
      .scalePoint()
      .domain(chartdata.map((d) => d.name))
      // coordinates
      .range([0 + padding, width - padding]); //width to 500px

    // testowanie osi
    console.log("Start - End xScale", xScale("Car"), xScale("Cinema"));

    // Y scales
    // const yScale = d3.scaleLinear().domain([start, end]);
    // minimu value - 0 , maximumvalue - 10 Car, 2 argument callback function któy zwraca wartość - coś jak arrayFilter
    const yScale = d3
      .scaleLinear()
      .domain([
        0,
        d3.max(chartdata, function (d) {
          return d.value;
        }),
      ])
      // .range([start, end]); - podobne do osi X ale jakby w dróga srotnę bo od góy do dołu się liczy
      .range([height - padding, 0 + padding]);

    console.log("Start - End yScale", yScale(0), yScale(10));

    // 4) Setup functions to draw Lines -------------------------------------------------------------------------------
    // cchemy znaleźć x i y wartość  dla każdego punktu
    // it produces drawing instructions for our line - istrnukcje do rysowania lini svg
    // .x to metoda komponentu line(komponentu d3)
    const line = d3
      .line()
      .x((d) => xScale(d.name))
      .y((d) => yScale(d.value))
      // można wyspecyfikować rożne typu curve - linia już nie jest typowo łamana
      .curve(d3.curveMonotoneX);

    console.log("chart draw commands", line(chartdata));

    // 5) Draw line ---------------------------------------------------------------------------------------------------
    // mamy referencje do DOM element przez svgRef a potem wybieramy element 'path' i z tego atrybut 'd' do rysowania ścieżki
    // można atrybut ustwaić na wartość na sztywno albo na funckję któa coś zwraca tutaj (value) => line(chartdata)
    // d3.select(svgRef.current).select("path").attr("d", "MMM");
    d3.select(svgRef.current)
      .select("path")
      .attr("d", (value) => line(chartdata))
      // Można ustawiac więcejatrybutów defaultorow byłby black - dlatego użwyamy none
      .attr("fill", "none")
      .attr("stroke", "white");

    // 6) Setup functions to draw  X and Y Axes -----------------------------------------------------------------------
    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);

    // 7) Draw x and y Axes -------------------------------------------------------------------------------------------
    // dopisanie wrapper do svg
    d3.select(svgRef.current)
      .append("g")
      .attr("transform", `translate(0,${height - padding})`)
      .attr("id", "xaxis")
      .call(xAxis);
  }, [chartdata]);

  return (
    <>
      <Sidebar currentPage="statistics" />
      <main>
        <Navbar />
        <div className="main__container statistics">
          {/* WANŻE BEZ  ref={svgRef}  nei wygenereuje wykresu*/}
          <svg id="chart" viewBox="0 0 500 150" ref={svgRef}>
            <path d="" fill="none" stroke="white" strokeWidth="5" />
          </svg>
          <p>
            <button
              className="statistics__button"
              type="button"
              onClick={() => setChartdata(newData())}
            >
              Chart data --> {JSON.stringify(chartdata)}
            </button>
          </p>
        </div>
      </main>
    </>
  );
};

export default Statistics;
