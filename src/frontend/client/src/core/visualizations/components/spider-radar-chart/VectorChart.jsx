import { select, scaleLinear, line } from "d3";
import { useRef, useState, useEffect } from "react";

// https://www.first.org/cvss/calculator/3.0
// https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2022-34878&vector=AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=NIST
// wersja 3.0

// TODO skala na okręgu
const CVSSV3 = [
  {
    id: 1,
    long: "Attack Vector",
    short: "AV",
    values: [
      { long: "Network", short: "AV:N" },
      { long: "Adjacent Network", short: "AV:A" },
      { long: "Local", short: "AV:L" },
      { long: "Physical", short: "AV:P" },
    ],
  },

  {
    id: 2,
    long: "Attack Complexity",
    short: "AC",
    values: [
      { long: "Low", short: "AC:L" },
      { long: "High", short: "AC:H" },
    ],
  },

  {
    id: 3,
    long: "Privileges Required",
    short: "PR",
    values: [
      { long: "None", short: "PR:N" },
      { long: "Low", short: "PR:L" },
      { long: "High", short: "PR:H" },
    ],
  },

  {
    id: 4,
    long: "User Interaction",
    short: "UI",
    values: [
      { long: "None", short: "UI:N" },
      { long: "Required", short: "UI:R" },
    ],
  },

  {
    id: 5,
    long: "Scope",
    short: "S",
    values: [
      { long: "Unchanged", short: "S:U" },
      { long: "Changed", short: "S:C" },
    ],
  },

  {
    id: 6,
    long: "Confidentiality Impact",
    short: "C",
    values: [
      { long: "None", short: "C:N" },
      { long: "Low", short: "C:L" },
      { long: "High", short: "C:H" },
    ],
  },

  {
    id: 7,
    long: "Integrity Impact",
    short: "I",
    values: [
      { long: "None", short: "I:N" },
      { long: "Low", short: "I:L" },
      { long: "High", short: "I:H" },
    ],
  },

  {
    id: 8,
    long: "Availability Impact",
    short: "A",
    values: [
      { long: "None", short: "A:N" },
      { long: "Low", short: "A:L" },
      { long: "High", short: "A:H" },
    ],
  },
];

let features = [
  "Attack Vector",
  "Attack Complexity",
  "Privileges Required",
  "User Interaction",
  "Scope",
];

const VectorChart = () => {
  const wrapperRef = useRef();
  const svgRef = useRef();
  const [data, setData] = useState([
    {
      "Attack Vector": 10,
      "Attack Complexity": 10,
      "Privileges Required": 10,
      "User Interaction": 10,
      Scope: 10,
    },
  ]);

  useEffect(() => {
    const svg = select(svgRef.current)
      .attr("width", 600)
      .attr("height", 600)
      .style("border", "1px solid green");

    // Plotting the Gridlines - okręgi
    let radialScale = scaleLinear().domain([0, 10]).range([0, 250]);

    let ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

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

    // add text labels nad okregami od srodka
    ticks.forEach((t) =>
      svg
        .append("text")
        .attr("x", 300)
        // ciut wyżej chcę ticks nad okregami
        .attr("y", 298 - radialScale(t))
        .text(t.toString())
    );

    // Plotting the Axes
    // mamy 5 featerów, wiec 360/5 daje 72 stopnie i o taki kąt trzeba je rozdzelić
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
      // TODO text się źle wyświetla - dodatkowy okręg na labelki
      svg
        .append("text")
        .attr("x", label_coordinate.x)
        .attr("y", label_coordinate.y)
        .text(ft_name);
    }

    // Plotting the Data
    //  tutuaj mam 1 ale będzie więcej jak będę porównywać CVe kilka ze sobą
    // - wtedy kazda płąszczyzna musi miec inny kolor
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
        let tmp = angleToCoordinate(angle, data_point[ft_name]);
        console.log("tmp: ", tmp);
        coordinates.push(angleToCoordinate(angle, data_point[ft_name]));
      }

      // bo linie się nie łączą
      let firstCoordinate = coordinates[0];
      console.log("firstCoordinate: ", firstCoordinate);
      coordinates = [...coordinates, firstCoordinate];
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
        .attr("class", "myPath")
        .attr("stroke-width", 3)
        // .attr("stroke", color)
        .attr("stroke", "black")
        .attr("fill", color)
        .attr("stroke-opacity", 1)
        .attr("opacity", 0.5);
    }
  }, [data]);

  return (
    <div ref={wrapperRef} className="svg-wrapper">
      <h2>Vector Chart</h2>
      <p>{JSON.stringify(data)}</p>
      <svg ref={svgRef} className="svg-chart"></svg>
    </div>
  );
};

export default VectorChart;
