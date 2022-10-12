import * as d3 from "d3";
const MARGIN = { TOP: 5, BOTTOM: 40, LEFT: 70, RIGHT: 50 };

export default class D3ChartVulnerabilitiesYears {
  constructor(element, dataArray, yearSelected, width, height, dataCategory) {
    let vis = this;

    d3.select("#trends-chart-id").remove();

    vis.HEIGHT = height - MARGIN.TOP - MARGIN.BOTTOM;
    vis.WIDTH = width - MARGIN.LEFT - MARGIN.RIGHT;

    vis.g = d3
      .select(element)
      .append("svg")
      .attr("class", "trends-chart__svg")
      .attr("id", "trends-chart-id")
      .attr("width", vis.WIDTH)
      .attr("height", vis.HEIGHT)
      .style("background", "white")
      .append("g")
      .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    vis.g
      .append("text")
      .attr("x", -(vis.HEIGHT / 2))
      .attr("y", -50)
      .attr("text-anchor", "middle")
      .text("Vulnerabilities")
      .attr("transform", "rotate(-90)");

    vis.xLabel = vis.g
      .append("text")
      .attr("x", vis.WIDTH / 2)
      .attr("y", vis.HEIGHT + 50)
      .attr("text-anchor", "middle")
      .text(yearSelected);

    vis.yScale = d3.scaleLinear().range([vis.HEIGHT, 0]);
    vis.yAxisGroup = vis.g.append("g");

    vis.xScale = d3.scaleBand().range([0, vis.WIDTH]).padding(0.2);
    vis.xAxisGroup = vis.g
      .append("g")
      .attr("transform", `translate(0, ${vis.HEIGHT})`);

    vis.update(dataArray, yearSelected, width, height, dataCategory);
  }

  update(dataArray, yearSelected, width, height, dataCategory) {
    console.log("update method");
    console.log("dataArray: ", dataArray);
    console.log("dataCategory: ", dataCategory);
    let vis = this;
    vis.data = dataArray;

    vis.xScale.domain(vis.data.map((d) => d.month));
    const xAxisCall = d3.axisBottom(vis.xScale);
    vis.xAxisGroup.call(xAxisCall);

    const maxVulnerabilities = d3.max(vis.data, (d) => d.vulnerabilities);
    vis.yScale.domain([0, maxVulnerabilities]);

    const yAxisCall = d3.axisLeft(vis.yScale);
    vis.yAxisGroup.transition().duration(500).call(yAxisCall);

    vis.xLabel.text(yearSelected);

    const rects = vis.g.selectAll("rect").data(vis.data);

    rects
      .exit()
      .transition()
      .duration(500)
      .attr("height", 0)
      .attr("y", vis.HEIGHT - MARGIN.TOP - MARGIN.BOTTOM)
      .remove();

    rects
      .transition()
      .duration(500)
      .attr("x", (d) => vis.xScale(d.month))
      .attr("y", (d) => vis.yScale(d.vulnerabilities))
      .attr("width", vis.xScale.bandwidth)
      .attr("height", (d) => vis.HEIGHT - vis.yScale(d.vulnerabilities));

    rects
      .enter()
      .append("rect")
      .attr("x", (d) => vis.xScale(d.month))
      .attr("y", (d) => vis.yScale(d.vulnerabilities))
      .attr("width", vis.xScale.bandwidth)
      .attr("height", (d) => vis.HEIGHT - vis.yScale(d.vulnerabilities))
      .attr("fill", "lightblue");

    // WARNING - komninowanie z liniowymi wykresami
    // 1. wyciągniecie danych po kategorii
    const vulnerabilitiesCritical = dataCategory.map((v) => v.critical);
    const vulnerabilitiesHigh = dataCategory.map((v) => v.high);
    const vulnerabilitiesMedium = dataCategory.map((v) => v.medium);
    const vulnerabilitiesLow = dataCategory.map((v) => v.low);
    console.log("vulnerabilitiesCritical: ", vulnerabilitiesCritical);

    const xScaleLine = d3
      .scaleLinear()
      .domain([0, vulnerabilitiesCritical.length - 1])
      // BUG - uważać na marginesy przy osi x tylko z prawej, bo od 0 wykres
      .range([0, width - MARGIN.RIGHT - MARGIN.LEFT]);

    const yScaleLine = d3
      .scaleLinear()
      // BUG - uważać na marginesy!
      .domain([0, height - MARGIN.BOTTOM - MARGIN.TOP])
      .range([height - MARGIN.BOTTOM - MARGIN.TOP - 50, 0]);

    const generateScaledLine = d3
      .line()
      .x((d, idx) => xScaleLine(idx))
      .y(yScaleLine)
      .curve(d3.curveCardinal);

    // dorysowywanie
    // BUG trzeba usuwać linie

    // ------------ critical
    const linesCritical = vis.g
      .selectAll(".lineCritical")
      .data([vulnerabilitiesCritical])
      // https://stackoverflow.com/questions/49137943/how-to-bring-the-selected-node-front-in-d3-js
      .raise();

    linesCritical.exit().remove();

    linesCritical
      .transition()
      .duration(500)
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "red");

    linesCritical
      .enter()
      .append("path")
      .attr("class", "lineCritical")
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "red");

    // ------------ high
    const linesHigh = vis.g
      .selectAll(".lineHigh")
      .data([vulnerabilitiesHigh])
      // https://stackoverflow.com/questions/49137943/how-to-bring-the-selected-node-front-in-d3-js
      .raise();

    linesHigh.exit().remove();

    linesHigh
      .transition()
      .duration(500)
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "orange");

    linesHigh
      .enter()
      .append("path")
      .attr("class", "lineHigh")
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "orange");

    // ------------ medium
    const linesMedium = vis.g
      .selectAll(".lineMedium")
      .data([vulnerabilitiesMedium])
      .raise();

    linesMedium.exit().remove();

    linesMedium
      .transition()
      .duration(500)
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "yellow");

    linesMedium
      .enter()
      .append("path")
      .attr("class", "lineMedium")
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "yellow");
    // ------------ low
    const linesLow = vis.g
      .selectAll(".lineLow")
      .data([vulnerabilitiesLow])
      .raise();

    linesLow.exit().remove();

    linesLow
      .transition()
      .duration(500)
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "gray");

    linesLow
      .enter()
      .append("path")
      .attr("class", "lineLow")
      .attr("d", (d) => generateScaledLine(d))
      .attr("fill", "none")
      .attr("stroke", "gray");
  }
}
