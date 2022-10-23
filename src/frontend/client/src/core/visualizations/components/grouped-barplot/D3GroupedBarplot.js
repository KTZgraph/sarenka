/*
https://d3-graph-gallery.com/graph/barplot_stacked_highlight.html
*/
import * as d3 from 'd3';

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

const MARGIN = { TOP: 10, RIGHT: 30, BOTTOM: 20, LEFT: 50 };

export default class D3GroupedBarplot {
  constructor(element, dataArray, dataColumns) {
    // FIXME - sztuczka z usuwaniem jednej referencji
    d3.select('#grouped-barplot-svg-id').remove();

    console.log('constructor ', dataArray);
    let vis = this;
    vis.data = dataArray;
    vis.dataColumns = dataColumns;

    vis.WIDTH = 460 - MARGIN.LEFT - MARGIN.RIGHT;
    vis.HEIGHT = 400 - MARGIN.TOP - MARGIN.BOTTOM;

    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'grouped-barplot-svg-id')
      .attr('width', vis.WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
      .attr('height', vis.WIDTH + MARGIN.TOP + MARGIN.BOTTOM)
      .append('g')
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    // List of subgroups = header of data
    vis.subgroups = vis.dataColumns.slice(1);

    // List of groups = species here = value of the first column called group -> I show them on the X axis
    vis.groups = vis.data.map((d) => d.group);

    // Add X axis
    vis.xScale = d3
      .scaleBand()
      .domain(vis.groups)
      .range([0, vis.WIDTH])
      .padding([0.2]);

    vis.svg
      .append('g')
      .attr('transform', `translate(0, ${vis.HEIGHT})`)
      .call(d3.axisBottom(vis.xScale).tickSizeOuter(0));

    // Add Y axis
    const maxH = d3.max(
      vis.data,
      (d) => d.critical + d.high + d.medium + d.low
    );
    vis.yScale = d3
      .scaleLinear()
      // troche ziwększam bo głupio to wygląda
      .domain([0, maxH * 1.05])
      .range([vis.HEIGHT, 0]);

    vis.svg.append('g').call(d3.axisLeft(vis.yScale));

    // color palette = one color per subgroup
    // vis.color = d3.scaleOrdinal().domain(vis.subgroups).range(d3.schemeSet2);
    vis.color = d3
      .scaleOrdinal()
      .domain(vis.subgroups)
      // FIXME - kolory takie jak z firmy do podatności
      .range(['red', 'orange', 'yellow', 'gray']);

    //stack the data? --> stack per subgroup
    vis.stackedData = d3.stack().keys(vis.subgroups)(vis.data);

    // Show the bars
    vis.svg
      .append('g')
      .selectAll('g')
      // Enter in the stack data = loop key per key = group per group
      .data(vis.stackedData)
      .join('g')
      .attr('fill', (d) => vis.color(d.key))
      .attr('class', (d) => 'myRect ' + d.key) // Add a class to each subgroup: their name
      .selectAll('rect')
      // enter a second time = loop subgroup per subgroup to add all rectangles
      .data((d) => d)
      .join('rect')
      .attr('x', (d) => vis.xScale(d.data.group))
      .attr('y', (d) => vis.yScale(d[1]))
      .attr('height', (d) => vis.yScale(d[0]) - vis.yScale(d[1]))
      .attr('width', vis.xScale.bandwidth())
      .attr('stroke', 'grey')
      .on('mouseover', function (event, d) {
        // What happens when user hover a bar

        // what subgroup are we hovering?
        const subGroupName = d3.select(this.parentNode).datum().key;

        // Reduce opacity of all rect to 0.2
        d3.selectAll('.myRect').style('opacity', 0.2);

        // Highlight all rects of this subgroup with opacity 1. It is possible to select them since they have a specific class = their name.
        d3.selectAll('.' + subGroupName).style('opacity', 1);
      })
      .on('mouseleave', function (event, d) {
        // When user do not hover anymore

        // Back to normal opacity: 1
        d3.selectAll('.myRect').style('opacity', 1);
      });

    // koniec konstruktora
  }
  update(dataArray) {
    console.log('update ', dataArray);
  }
}
