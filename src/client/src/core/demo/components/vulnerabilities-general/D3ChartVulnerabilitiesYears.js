import { select, scaleLinear, scaleBand, axisBottom, max, axisLeft } from "d3";
const MARGIN = { TOP: 0, BOTTOM: 0, LEFT: 70, RIGHT: 5 };

export default class D3ChartVulnerabilitiesYears {
  constructor(element, dataArray, yearSelected, width, height) {
    let vis = this;

    vis.g = select(element)
      .attr("class", "trends-chart__svg")
      .attr("id", "trends-chart-id")
      .attr("width", width)
      .attr("height", height)
      .style("background", "white")
      .append("g")
      .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    vis.g
      .append("text")
      .attr("x", -(height / 2))
      .attr("y", -50)
      .attr("text-anchor", "middle")
      //   .text("Vulnerabilities")
      .attr("transform", "rotate(-90)");

    vis.xLabel = vis.g
      .append("text")
      .attr("x", width / 2)
      .attr("y", height + 50)
      .attr("text-anchor", "middle");
    //   .text(yearSelected);

    vis.yScale = scaleLinear().range([height, 0]);
    vis.yAxisGroup = vis.g.append("g");

    vis.xScale = scaleBand().range([0, width]).padding(0.2);
    vis.xAxisGroup = vis.g
      .append("g")
      .attr("transform", `translate(0, ${height})`);

    vis.update(dataArray, yearSelected, width, height);
    // koniec konstruktora
  }

  // metoda update
  update(dataArray, yearSelected, width, height) {
    console.log("update method");
    console.log("dataArray: ", dataArray);
    let vis = this;
    vis.data = dataArray;

    vis.xScale.domain(vis.data.map((d) => d.month));
    const xAxisCall = axisBottom(vis.xScale);
    vis.xAxisGroup.call(xAxisCall);

    const maxVulnerabilities = max(vis.data, (d) => d.vulnerabilities);
    vis.yScale.domain([0, maxVulnerabilities]);
    const yAxisCall = axisLeft(vis.yScale);
    vis.yAxisGroup.transition().duration(500).call(yAxisCall);

    vis.xLabel.text(yearSelected);

    const rects = vis.g.selectAll("rect").data(vis.data);

    rects
      .exit()
      .transition()
      .duration(500)
      //   zmiana osi teraz znika słupek jakby w dół a nie tak dziwnie nachodiz na ostatni
      .attr("height", 0)
      .attr("y", height - MARGIN.TOP - MARGIN.BOTTOM)
      .remove();

    // UPDATE
    rects
      .transition()
      .duration(500)
      .attr("x", (d) => vis.xScale(d.month))
      .attr("y", (d) => vis.yScale(d.vulnerabilities))
      .attr("width", vis.xScale.bandwidth)
      .attr("height", (d) =>
        height - vis.yScale(d.vulnerabilities) > 0
          ? height - vis.yScale(d.vulnerabilities)
          : 0
      );

    // ENTER
    rects
      .enter()
      .append("rect")
      .attr("x", (d) => vis.xScale(d.month))
      .attr("y", (d) => vis.yScale(d.vulnerabilities))
      .attr("width", vis.xScale.bandwidth)
      .attr("height", (d) =>
        height - vis.yScale(d.vulnerabilities) > 0
          ? height - vis.yScale(d.vulnerabilities)
          : 0
      )
      .attr("fill", "lightblue");
  }
}
