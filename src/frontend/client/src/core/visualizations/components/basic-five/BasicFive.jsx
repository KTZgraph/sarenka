// responsywność wykresu

import { select, axisBottom, scaleLinear, axisRight, scaleBand } from "d3";
import { useRef, useEffect, useState } from "react";
import useResizeObserver from "../../../../hooks/useResizeObserver";

const BasicFive = () => {
  const [data, setData] = useState([25, 30, 45, 60, 20, 65, 75]);
  const svgRef = useRef();
  const wrapperRef = useRef();
  //   BUG useResizeObserver NIE dizała z SVG
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);

    if (!dimensions) return;

    const xScale = scaleBand()
      .domain(data.map((value, index) => index))
      .range([0, dimensions.width]) //change na dynmiczną TODO
      .padding(0.5);

    const yScale = scaleLinear()
      // domain zmienić na dynamiczną, bo nie znamy wysokosci wykresu
      .domain([0, dimensions.height]) //TODO
      .range([150, 0]);

    const colorScale = scaleLinear()
      .domain([75, 100, 150]) //teraz 100 będzie pomarańczowe
      .range(["green", "orange", "red"]) //rozwiazanie brdzydkiego przejsci akolorostycznego przez brzydki brąz
      .clamp(true);

    const xAxis = axisBottom(xScale).ticks(data.length);

    svg
      .select(".x-axis")
      //   BUG - dopisać px inaczej dziwnie się zachowuje!
      .style("transform", `translateY(${dimensions.height}px)`)
      .call(xAxis);

    const yAxis = axisRight(yScale);
    svg
      .select(".y-axis")
      //   BUG - dopisać px inaczej dziwnie się zachowuje!
      .style("transform", `translateX(${dimensions.width}px)`)
      .call(yAxis);

    svg
      .selectAll(".bar")
      .data(data)
      .join("rect")
      .attr("class", "bar")
      .attr("x", (value, idx) => xScale(idx))
      .attr("width", xScale.bandwidth())
      .style("transform", "scale(1, -1)")
      .attr("y", -150)
      // BUG na eventach nie ma indexu w callbacku
      .on("mouseenter", (event, value) => {
        svg
          .selectAll(".tooltip")
          .data([value])
          .join((enter) => enter.append("text").attr("y", yScale(value) - 4))
          .attr("class", "tooltip")
          .text(value)
          //   .attr("text-anchor", "middle")
          //   BUG - brak id w nowej wersji d3.js
          .attr("x", event.target.getBoundingClientRect().x)

          //   BUG - fixnięte - jeszcze troszekę na prawo schodzi - padding
          //  TODO z dodatkowymi danymi nie działa ;/ tooltip
          .style(
            "transform",
            `translate(${
              -(dimensions.width / xScale.bandwidth()) *
              (dimensions.width / xScale.bandwidth())
            }px)`
          )

          .transition()
          .attr("opacity", 1)
          .attr("y", yScale(value) - 7);

        console.log(
          "event.target.getBoundingClientRect().x",
          event.target.getBoundingClientRect().x
        );

        console.log(
          "-(dimensions.width / xScale.bandwidth) * (data.length * 2 + 1)",
          `${(dimensions.width / xScale.bandwidth()) * 15}`
        );
        console.log("dimensions.width", dimensions.width);
        console.log("xScale.bandwidth()", xScale.bandwidth());
        console.log("xScale.bandwidth()", xScale.bandwidth());
        // tu koniec event
      })

      //   MATMA danych 0- słupków 6 za n przyjmuję 6
      // width/bandwith = 15 czyli width/bandwith = n+ 1

      .on("mouseleave", () => svg.select(".tooltip").remove())
      .transition()
      .attr("height", (value) => 150 - yScale(value))
      .attr("fill", colorScale);
  }, [data, dimensions]);

  return (
    <>
      <div
        ref={wrapperRef}
        className="svg-container"
        style={{ padding: "50px", overflow: "visible" }}
      >
        <svg
          ref={svgRef}
          style={{
            overflow: "visible",
            width: "100%",
            display: "block",
            background: "#eee",
          }}
        >
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
      <br />
      <button onClick={() => setData(data.map((value) => value + 5))}>
        Update data
      </button>
      <button onClick={() => setData(data.filter((value) => value < 35))}>
        Filter data
      </button>
      <button
        onClick={() => setData([...data, Math.floor(Math.random() * 140)])}
      >
        Add data
      </button>
    </>
  );
};

export default BasicFive;
