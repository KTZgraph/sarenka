/*
https://www.youtube.com/watch?v=GGpl4uKE4T4&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=15
drugi wykres pokazujacy fragment zaznaczony przez brush w komponencie rodzica

https://youtu.be/GGpl4uKE4T4?t=539
clipPath and a clip path is basically a windows which sits in front of your SVG elements and it will only make the parts of your SVG visible
which are iside of this window frame and to do that you have to got to any SVG elemnt and define the <defs> the definitions like so
and you have to create a new clipPath definition like so


*/

import {
  select,
  scaleLinear,
  max,
  line,
  curveCardinal,
  axisBottom,
  axisLeft,
} from "d3";
import { useRef, useEffect } from "react";

import useResizeObserver from "../../../../hooks/useResizeObserver";

// selection to teraz props z rodzica
const FilteringVisuallyChild = ({
  data,
  selection,
  // props w domyślną wartością
  clipPathId = "clipPath-id",
}) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  //   will be called initially and on every dta change
  useEffect(() => {
    const svg = select(svgRef.current);
    // dla content grupy - okrojeone wykresu
    const content = svg.select(".content");

    const { width, height } =
      dimensions || wrapperRef.current.getBoundingClientRect();

    //   scales + line generator
    const xScale = scaleLinear()
      // selection array jako zakres osi X - selection to ta cześć zaznczona przez brusha w komponencie rodzica
      .domain(selection)
      // .range([0, width]);
      // tak samo padding do osi OX
      .range([10, width - 10]);

    const yScale = scaleLinear()
      .domain([0, max(data)])
      // .range([height, 0]);
      // WARNING dodanie paddigu od osi OY żeby tak od brzegu do brzegu wartości nie były
      .range([height - 10, 10]);

    const lineGenerator = line()
      .x((d, idx) => xScale(idx))
      .y((d) => yScale(d))
      .curve(curveCardinal);

    // teriaz linie renderuje w grupie content
    content
      .selectAll(".myLine")
      .data([data])
      .join("path")
      .attr("class", "myLine")
      .attr("stroke", "black")
      .attr("fill", "none")
      .attr("d", lineGenerator);

    // teraz kropki renderuję w grupie content
    content
      .selectAll(".myDot")
      .data(data)
      .join("circle")
      .attr("class", "myDot")
      .attr("stroke", "black")
      .attr("r", (value, idx) =>
        idx >= selection[0] && idx <= selection[1] ? 4 : 2
      )
      .attr("fill", (value, idx) =>
        idx >= selection[0] && idx <= selection[1] ? "orange" : "black"
      )
      .attr("cx", (value, idx) => xScale(idx))
      .attr("cy", yScale);

    // WARNING - osie zostają w samym svg A NIe w grupie content
    const xAxis = axisBottom(xScale);
    svg
      .select(".x-axis")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);

    const yAxis = axisLeft(yScale);

    svg.select(".y-axis").call(yAxis);
  }, [data, dimensions, selection]);

  // BUG jak się używam <clipPath id="myClipPath-id"> z tym samym id to są problemy
  // BUG żeby to naprawić, trzeba pozwolić komponentom na zmianę tego id np przez extracting this value  "myClipPath-id" by the prop for example
  return (
    <>
      <div ref={wrapperRef} className="filtering-visually-chart">
        <svg ref={svgRef}>
          {/* WARNING teraz wyrkes musi być renderowanie nie w samym <svg> ale w  grupie <g className="content" />*/}
          {/* cmipPath - okno przed SVG definiowanie co ma być widoczne*/}
          <defs>
            {/* clipPath musi mieć id */}
            {/* <clipPath id="myClipPath-id"> */}
            {/* BUG roziwązanie problemu rtego samego id w cliPath */}
            <clipPath id={clipPathId}>
              {/* trzeba zdefiniować kształ okna - prostokąta tutaj od góra lewo punk do prawo dół punk*/}
              <rect x="0" y="0" width="100%" height="100%" />
            </clipPath>
          </defs>
          {/* dopisanie clipPath do nowej grupy bo chcę windows położyć przed wykresem, ale nie  przed osiami, żeby dalej były widoczne*/}
          {/* dodaje isę przez url z id cliPath */}
          {/* <g className="content" clipPath="url(#myClipPath-id)" /> */}
          {/* BUG roziwązanie problemu rtego samego id w cliPath */}
          <g className="content" clipPath={`url(#${clipPathId})`} />
          <g className="x-axis" />
          <g className="y-axis" />
        </svg>
      </div>
    </>
  );
};

export default FilteringVisuallyChild;
