import * as d3 from 'd3';

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

const MARGIN = { TOP: 10, RIGHT: 30, BOTTOM: 20, LEFT: 50 };

export default class D3BarplotThreeBars {
  constructor(element, dataArray) {
    // FIXME - sztuczka z usuwaniem jednej referencji
    d3.select('#barplot-three-bars-svg-id').remove();

    console.log('constructor ', dataArray);
    let vis = this;
    vis.data = dataArray;

    vis.WIDTH = 460 - MARGIN.LEFT - MARGIN.RIGHT;
    vis.HEIGHT = 400 - MARGIN.TOP - MARGIN.BOTTOM;

    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'barplot-three-bars-svg-id')
      .attr('width', vis.WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
      .attr('height', vis.WIDTH + MARGIN.TOP + MARGIN.BOTTOM)
      .append('g')
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    // List of subgroups = header of the csv files = soil condition here
    vis.subgroups = vis.data.columns.slice(1);

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
      .call(d3.axisBottom(vis.xScale).tickSize(0));

    // Add Y axis
    vis.yScale = d3
      .scaleLinear()
      .domain([0, 40])
      .range([vis.HEIGHT, 0]);
    vis.svg.append('g').call(d3.axisLeft(vis.yScale));

    // Another scale for subgroup position?
    vis.xSubgroup = d3
      .scaleBand()
      .domain(vis.subgroups)
      .range([0, vis.xScale.bandwidth()])
      .padding([0.05]);

    // color palette = one color per subgroup
    vis.color = d3
      .scaleOrdinal()
      .domain(vis.subgroups)
      .range(['#e41a1c', '#377eb8', '#4daf4a']);

    // Show the bars
    vis.svg
      .append('g')
      .selectAll('g')
      // Enter in data = loop group per group
      .data(vis.data)
      .enter()
      .append('g')
      .attr('transform', function (d) {
        return `translate(${vis.xScale(d.group)},0)`;
      })
      .selectAll('rect')
      .data(function (d) {
        return vis.subgroups.map(function (key) {
          return { key: key, value: d[key] };
        });
      })
      .enter()
      .append('rect')
      .attr('x', function (d) {
        return vis.xSubgroup(d.key);
      })
      .attr('y', function (d) {
        return vis.yScale(d.value);
      })
      .attr('width', vis.xSubgroup.bandwidth())
      .attr('height', function (d) {
        return vis.HEIGHT - vis.yScale(d.value);
      })
      .attr('fill', function (d) {
        return vis.color(d.key);
      });

    // koniec konstruktora
  }
  update(dataArray) {
    console.log('update ', dataArray);
  }
}
