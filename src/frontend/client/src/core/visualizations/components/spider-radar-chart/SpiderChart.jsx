/*
https://yangdanny97.github.io/blog/2019/03/01/D3-Spider-Chart
*/
import { select, scaleLinear, line } from "d3";
import { useRef, useState, useEffect } from "react";

// let data = [];
let features = ["A", "B", "C", "D", "E", "F"];
// //generate the data
// for (var i = 0; i < 3; i++){
//     var point = {}
//     //each feature will be a random number from 1-9
//     features.forEach(f => point[f] = 1 + Math.random() * 8);
//     data.push(point);
// }

const SpiderChart = () => {
  const wrapperRef = useRef();
  const svgRef = useRef();
  const [data, setData] = useState([
    {
      A: 1.5073162478091486,
      B: 5.383649875965705,
      C: 2.1593749277074163,
      D: 8.747164125435429,
      E: 2.119171087179632,
      F: 8.51252474027632,
    },
    {
      A: 7.628088026067431,
      B: 7.0659436225533625,
      C: 8.22750562899154,
      D: 8.14706302409668,
      E: 2.0275660867750886,
      F: 5.6271641860470965,
    },
    {
      A: 4.158300227965418,
      B: 8.770931279904376,
      C: 5.682196648550601,
      D: 5.193537635011426,
      E: 8.148788419190963,
      F: 4.991488565834359,
    },
  ]);

  useEffect(() => {
    const svg = select(svgRef.current)
      .attr("width", 600)
      .attr("height", 600)
      .style("border", "1px solid red");

    // Plotting the Gridlines
    let radialScale = scaleLinear().domain([0, 10]).range([0, 250]);
    let ticks = [2, 4, 6, 8, 10];

    // dodanie szarych okręgów
    ticks.forEach((t) =>
      svg
        .append("circle")
        .attr("cx", 300)
        .attr("cy", 300)
        .attr("fill", "none")
        .attr("stroke", "gray")
        .attr("r", radialScale(t))
    );

    // add text labels nad okregami od srodka 2, 4, 6, 8, 10 cyferki nad okregami na północ
    ticks.forEach((t) =>
      svg
        .append("text")
        .attr("x", 305)
        .attr("y", 300 - radialScale(t))
        .text(t.toString())
    );

    // Plotting the Axes
    // mamy 6 featerów, wiec 360/6 daje 60 stopni i o taki kąt trzeba je rozdzelić
    function angleToCoordinate(angle, value) {
      // funkcja HELPER
      let x = Math.cos(angle) * radialScale(value);
      let y = Math.sin(angle) * radialScale(value);
      return { x: 300 + x, y: 300 - y };
    }

    for (var i = 0; i < features.length; i++) {
      // dzieli okrąg na na 60 stopni odleglosi dla features i rusuje 3 linie przecinajace koła
      let ft_name = features[i];
      let angle = Math.PI / 2 + (2 * Math.PI * i) / features.length;
      let line_coordinate = angleToCoordinate(angle, 10);
      let label_coordinate = angleToCoordinate(angle, 10.5);

      //draw axis line
      svg
        .append("line")
        .attr("x1", 300)
        .attr("y1", 300)
        .attr("x2", line_coordinate.x)
        .attr("y2", line_coordinate.y)
        .attr("stroke", "black");

      //draw axis label
      svg
        .append("text")
        .attr("x", label_coordinate.x)
        .attr("y", label_coordinate.y)
        .text(ft_name);
    }

    // Plotting the Data
    //  we know our data only has 3 points,
    // scaleOrdinal and map to an array of more colors  dla większych zborów danych
    let svgLine = line()
      // zmiana nazwy względem tutoralu
      .x((d) => d.x)
      .y((d) => d.y);
    let colors = ["darkorange", "gray", "navy"];

    function getPathCoordinates(data_point) {
      //  funkjca HELPER
      let coordinates = [];
      for (var i = 0; i < features.length; i++) {
        let ft_name = features[i];
        let angle = Math.PI / 2 + (2 * Math.PI * i) / features.length;
        coordinates.push(angleToCoordinate(angle, data_point[ft_name]));
      }
      return coordinates;
    }

    for (var i = 0; i < data.length; i++) {
      let d = data[i];
      let color = colors[i];
      let coordinates = getPathCoordinates(d);

      //draw the path element
      svg
        .append("path")
        .datum(coordinates)
        .attr("d", svgLine)
        .attr("stroke-width", 3)
        .attr("stroke", color)
        .attr("fill", color)
        .attr("stroke-opacity", 1)
        .attr("opacity", 0.5);
    }
  }, [data]);

  return (
    <div ref={wrapperRef} className="svg-wrapper">
      <h2>Spider Chart</h2>
      <p>{JSON.stringify(data)}</p>
      <svg ref={svgRef} className="svg-chart"></svg>
    </div>
  );
};

export default SpiderChart;
