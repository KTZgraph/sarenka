/*
https://www.youtube.com/watch?v=10dl-gDJLks
*/

import { select, pie, arc, scaleOrdinal, schemeSet2 } from "d3";

import { useState, useRef, useEffect } from "react";

const PieChartNoProblem = () => {
  const [data, setData] = useState([
    { property: "a", value: 4 },
    { property: "b", value: 3 },
    { property: "c", value: 10 },
    { property: "d", value: 2 },
    { property: "e", value: 8 },
  ]);

  const svgRef = useRef();
  useEffect(() => {
    // 1.setting up svg container
    const widthPie = 200;
    const heightPie = 200;
    const radiusPie = widthPie / 2;

    const svg = select(svgRef.current)
      .attr("width", widthPie)
      .attr("height", heightPie)
      .style("overflow", "visible")
      .style("margin-top", "400px");
    // 2.setting up chart
    const formattedData = pie().value((d) => d.value)(data);
    // z innerRadius można donuts stworzyć
    const arcGenerator = arc().innerRadius(0).outerRadius(radiusPie);
    const color = scaleOrdinal().range(schemeSet2);

    // 3.setting up svg data
    svg
      .selectAll()
      .data(formattedData)
      .join("path")
      .attr("d", arcGenerator)
      .attr("fill", (d) => color(d.value))
      .style("opacity", 0.7);

    // 4.setting up annotation
    svg
      .selectAll()
      .data(formattedData)
      .join("text")
      //WARNING   formattedData są trochę inne, dlatego, żeby dostać się do prorperty trzeba tak zrović  d.data.property
      .text((d) => d.data.property)
      //   bez trnsalte wszystkie napisy na samym środku kółka
      .attr("transform", (d) => `translate(${arcGenerator.centroid(d)})`)
      .style("text-anchor", "middle");
  }, [data]);

  return (
    <div style={{ marginLeft: "200px", overflow: "visible" }}>
      <svg
        //   WARNING - overflow visible!
        style={{ marginLeft: "200px", overflow: "visible" }}
        ref={svgRef}
      ></svg>
    </div>
  );
};

export default PieChartNoProblem;
