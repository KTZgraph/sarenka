import { select, scaleLinear, scaleBand, axisBottom, max, axisLeft } from "d3";
const MARGIN = { TOP: 50, BOTTOM: 50, LEFT: 70, RIGHT: 50 };

export function drawChart(svgElement, data, yearSelected, width, height) {
  console.log("draw chart");

  const svg = select(svgElement)
    //   .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("padding", "50px");

  console.log("data", data);

  const vulnerabilitiesAll = data.map(
    (d) => d.critical + d.high + d.medium + d.low
  );
  const vulnerabilitiesCritical = data.map((d) => d.critical);
  const vulnerabilitiesHigh = data.map((d) => d.high);
  const vulnerabilitiesMedium = data.map((d) => d.medium);
  const vulnerabilitiesLow = data.map((d) => d.low);

  // WARNING  wykres słupkowy
  const xScaleBar = scaleBand()
    .domain(vulnerabilitiesAll.map((val, idx) => idx))
    .range([0, width])
    .padding(0.5);

  const yScaleBar = scaleLinear().domain([0, height]).range([height, 0]);

  //   osie
  const xAxis = axisBottom(xScaleBar).ticks(vulnerabilitiesAll.length);
  const yAxis = axisLeft(yScaleBar);

  //   dodanie osi X do wykresu
  svg
    .append("g")
    .call(xAxis)
    .attr("transform", `translate(0, ${height})`)
    .attr("class", "x-axis");
  //   dodanie osi Y
  svg.append("g").call(yAxis).attr("class", "y-axis");
}
