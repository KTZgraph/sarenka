/*
https://d3-graph-gallery.com/graph/donut_label.html
*/

import { select, schemeDark2, scaleOrdinal, pie, arc } from "d3";
import { useState, useRef, useEffect } from "react";

// BUG - uwaga na fromat danych!!! - sam obiekt nie przejdzie, lepiej jak jest lista
const DUMMY_DATA = { a: 9, b: 20, c: 30, d: 8, e: 12, f: 3, g: 7, h: 14 };

const DonutChartGroupLabel = () => {
  // BUG  const [data, setData] = useState(DUMMY_DATA);
  const [data, setData] = useState([
    { property: "critical", value: 4 },
    { property: "b", value: 3 },
    { property: "c", value: 10 },
    { property: "d", value: 2 },
    { property: "e", value: 8 },
  ]);

  const svgRef = useRef();

  useEffect(() => {
    // set the dimensions and margins of the graph
    const widthPie = 450;
    const heightPie = 450;
    const marginPie = 40;

    // The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
    const radiusPie = Math.min(widthPie, heightPie) / 2 - marginPie;

    // append the svg object to the div called 'my_dataviz'
    const svg = select(svgRef.current)
      .append("svg")
      .attr("width", widthPie)
      .attr("height", heightPie)
      .append("g")
      .attr("transform", `translate(${widthPie / 2},${heightPie / 2})`);

    // set the color scale
    // WARNING - alerantywny zapis
    const color = scaleOrdinal().range(schemeDark2);
    // BUG - jak się wpisze scale ręcznie to lubi zakolorować na ciemniej w środku
    // const color = scaleOrdinal()
    //   // WARNING - tu można dac swój zakres kolorów
    //   .domain(["a", "b", "c", "d", "e", "f", "g", "h"])
    //   .range(schemeDark2);

    // Compute the position of each group on the pie:
    const formattedData = pie()
      // żeby nie sortowało po wielkości
      .sort(null)
      //   .value((d) => d[1])(data);
      .value((d) => d.value)(data);

    // The arc generator
    const arcGenerator = arc()
      // This is the size of the donut hole
      .innerRadius(radiusPie * 0.5)
      .outerRadius(radiusPie * 0.8);

    // Another arc that won't be drawn. Just for labels positioning
    // WARNING sztuczka na labelki
    const outerArc = arc()
      .innerRadius(radiusPie * 0.9)
      .outerRadius(radiusPie * 0.9);

    // Build the pie chart: Basically,
    // each part of the pie is a path that we build using the arc function.

    svg
      // WARNING selectAll z argumentem czy bez działa tak samo
      //   .selectAll()
      .selectAll("allSlices")
      .data(formattedData)
      .join("path")
      .attr("d", arcGenerator)
      //   przez to, ze formattedData są trochę w innej formie, to trzeba się do wartości dodastać przez
      //   d.data[1] z property data
      .attr("fill", (d) => color(d.value))
      .attr("stroke", "white")
      .style("stroke-width", "2px")
      .style("opacity", 0.7);

    // Add the polylines between chart and labels:
    // te kreseczki od wykresu na których mi zależało
    svg
      .selectAll("allPolylines")
      .data(formattedData)
      .join("polyline")
      .attr("stroke", "black")
      .style("fill", "none")
      .attr("stroke-width", 1)
      .attr("points", function (d) {
        const posA = arcGenerator.centroid(d); // line insertion in the slice
        const posB = outerArc.centroid(d); // line break: we use the other arc generator that has been built only for that
        const posC = outerArc.centroid(d); // Label position = almost the same as posB
        const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2; // we need the angle to see if the X position will be at the extreme right or extreme left
        posC[0] = radiusPie * 0.95 * (midangle < Math.PI ? 1 : -1); // multiply by 1 or -1 to put it on the right or on the left
        return [posA, posB, posC];
      });

    // Add the polylines between chart and labels:
    // napisy do labelek
    svg
      .selectAll("allLabels")
      .data(formattedData)
      .join("text")
      //   .text((d) => d.data[0])
      .text((d) => d.data.property)
      .attr("transform", function (d) {
        const pos = outerArc.centroid(d);
        const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2;
        pos[0] = radiusPie * 0.99 * (midangle < Math.PI ? 1 : -1);
        return `translate(${pos})`;
      })
      .style("text-anchor", function (d) {
        const midangle = d.startAngle + (d.endAngle - d.startAngle) / 2;
        return midangle < Math.PI ? "start" : "end";
      });

    // 4.setting up annotation
    svg
      .selectAll()
      .data(formattedData)
      .join("text")
      //WARNING   formattedData są trochę inne, dlatego, żeby dostać się do prorperty trzeba tak zrović  d.data.property
      //   .text((d) => d.data.property)
      .text((d) => "Jeden napis na środku")
      //   bez trnsalte wszystkie napisy na samym środku kółka
      //   .attr("transform", (d) => `translate(${arcGenerator.centroid(d)})`)
      .style("text-anchor", "middle");

    //   ----------------------------------
  }, [data]);

  return (
    <div
      style={{ marginLeft: "200px", overflow: "visible", background: "pink" }}
    >
      TUTAJ
      <svg
        //   WARNING - overflow visible!
        style={{ overflow: "visible", background: "green" }}
        ref={svgRef}
      ></svg>
    </div>
  );
};

export default DonutChartGroupLabel;
