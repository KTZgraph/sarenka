/*
TODO
http://bl.ocks.org/dbuezas/9306799
*/
import * as d3 from 'd3';

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

export default class D3PieChartLabels {
  constructor(element, dataArray) {
    console.log('dataArray constructor: ', dataArray);

    // FIXME - sztuczka z usuwaniem jednej referencji
    d3.select('#pie-chart-labels-id').remove();

    let vis = this;
    vis.data = dataArray;

    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'pie-chart-labels-id')
      .attr('class', 'pie-chart-labels');
  }

  update(dataArray) {
    console.log('dataArray update: ', dataArray);
  }
}
