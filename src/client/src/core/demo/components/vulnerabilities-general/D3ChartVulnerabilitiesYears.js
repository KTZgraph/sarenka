import { select, scaleLinear, scaleBand, axisBottom, max, axisLeft } from "d3";
const MARGIN = { TOP: 50, BOTTOM: 50, LEFT: 70, RIGHT: 50 };

export default class D3ChartVulnerabilitiesYears {
  constructor(svgElement, data, yearSelected, width, height) {
    // select("#vulnerabilities-year-chart-id").remove();

    let vis = this;
    console.log("drawChart konstruktor");

    vis.svg = select(svgElement)
      //   .append("svg")
      .attr("width", width)
      .attr("height", height)
      .attr("id", "vulnerabilities-year-chart-id");
    // vis.update(data, yearSelected, width, height);
  }
  // svgRef.current, data, yearSelected, width, height
  update(data, yearSelected, width, height) {
    let vis = this;

    console.log("drawChart update");

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
    vis.svg
      .append("g")
      .call(xAxis)
      .attr("transform", `translate(0, ${height})`);
    //   dodanie osi Y
    vis.svg.append("g").call(yAxis);
  }
}
