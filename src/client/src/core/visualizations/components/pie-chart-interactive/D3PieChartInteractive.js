/*
https://d3-graph-gallery.com/graph/pie_changeData.html
*/
import * as d3 from 'd3';

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

// jeden margines dookoła pie chart
const MARGIN = 40;

export default class D3PieChartInteractive {
  constructor(element, dataArray) {
    // FIXME - sztuczka z usuwaniem jednej referencji
    d3.select('#pie-chart-interactive-id').remove();

    let vis = this;
    vis.data = dataArray;

    vis.WIDTH = 450;
    vis.HEIGHT = 450;

    // The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
    vis.radius = Math.min(vis.WIDTH, vis.HEIGHT) / 2 - MARGIN;

    // append the svg object to the div called 'my_dataviz'
    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'pie-chart-interactive-id')
      .attr('width', vis.WIDTH)
      .attr('height', vis.HEIGHT)
      .append('g')
      .attr(
        'transform',
        `translate(${vis.WIDTH / 2}, ${vis.HEIGHT / 2})`
      );

    // set the color scale
    vis.color = d3
      .scaleOrdinal()
      .domain(['a', 'b', 'c', 'd', 'e', 'f'])
      .range(d3.schemeDark2);

    //   koniec konstruktora
    vis.update(vis.data);
  }

  update(dataArray) {
    // A function that create / update the plot for a given variable:
    console.log('dataArray', dataArray);

    let vis = this;
    vis.data = dataArray;

    // Compute the position of each group on the pie:
    vis.pie = d3
      .pie()
      .value(function (d) {
        return d[1];
      })
      .sort(function (a, b) {
        return d3.ascending(a.key, b.key);
      }); // This make sure that group order remains the same in the pie chart

    const data_ready = vis.pie(Object.entries(vis.data));

    // map to data
    // vis.u = vis.svg.selectAll("path").data(vis.data);
    vis.u = vis.svg.selectAll('path').data(data_ready);

    // Build the pie chart: Basically, each part of the pie is a path that we build
    // using the arc function.
    vis.u
      .join('path')
      .transition()
      .duration(1000)
      .attr('d', d3.arc().innerRadius(0).outerRadius(vis.radius))
      .attr('fill', function (d) {
        return vis.color(d);
      })
      .attr('stroke', 'white')
      .style('stroke-width', '2px')
      .style('opacity', 1);
  }
}
