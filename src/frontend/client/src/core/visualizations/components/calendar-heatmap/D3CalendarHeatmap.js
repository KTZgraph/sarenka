/*
https://www.youtube.com/watch?v=x9zcWgXJcwM
TODO - przykład
https://d3-graph-gallery.com/graph/heatmap_tooltip.html
*/

import * as d3 from 'd3';
const MARGIN = { TOP: 25, BOTTOM: 10, LEFT: 20, RIGHT: 80 };
const PADDING = 2;
const RECT_SIZE = 15;

const COLORS = [
  { Range: '1-20', Color: '#FFFFFF' },
  { Range: '21-40', Color: '#FFF7DF' },
  { Range: '41-60', Color: '#FFE7BE' },
  { Range: '61-80', Color: '#FFC14D' },
  { Range: '81-100', Color: '#FF0000' },
];

function colorAssign(d) {
  if (d <= 100 && d > 80) return '#FF0000';
  else if (d <= 80 && d > 60) return '#FFC14D';
  else if (d <= 60 && d > 40) return '#FFE7BE';
  else if (d <= 40 && d > 20) return '#FFF7DF';
  else return '#FFFFFF';
}

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

export default class D3CalendarHeatmap {
  constructor(element, dataArray, dimensions) {
    let vis = this;
    vis.data = dataArray;

    console.log('dataArray constructor: ', dataArray);
    console.log('dataArray dimensions: ', dimensions.width);
    console.log('dataArray dimensions: ', dimensions.height);

    // FIXME - sztuczka z usuwaniem jednej referencji
    // FIXME - wystarczy tylko SVG używać w komponencie Reacta
    // d3.select("#calendar-heatmap-id").remove();

    //   rozmiar SVG
    vis.HEIGHT = dimensions.height - MARGIN.TOP - MARGIN.BOTTOM;
    vis.WIDTH = dimensions.width - MARGIN.LEFT - MARGIN.RIGHT;

    vis.svg = d3
      .select(element)
      .attr('width', vis.HEIGHT)
      .attr('height', vis.WIDTH)
      .style('border', '1px solid red');

    //  wyświeltanie dni na scali
    vis.xScale = d3
      .scaleLinear()
      .domain([0, vis.data.length])
      .range([0, vis.WIDTH]);

    // labelki do dni
    vis.xLabels = vis.svg
      .append('g')
      .selectAll('text')
      .data(vis.data)
      .join('text')
      .text((d) => `${d.Day}`)
      .attr('x', (d, i) => vis.xScale(i) + MARGIN.LEFT)
      .attr('y', vis.HEIGHT)
      //   .attr("fill", "white")
      .style('font-size', 14);

    vis.update(dataArray, dimensions);
    // koniec konstruktora
  }

  update(dataArray, dimensions) {
    let vis = this;
    vis.data = dataArray;
    console.log('dataArray update: ', dataArray);
    console.log('dataArray update dimensions: ', dimensions.width);
    console.log('dataArray updatedimensions: ', dimensions.height);

    //   rozmiar SVG
    vis.HEIGHT = dimensions.height - MARGIN.TOP - MARGIN.BOTTOM;
    // vis.HEIGHT = 300 - MARGIN.TOP - MARGIN.BOTTOM;
    vis.WIDTH = dimensions.width - MARGIN.LEFT - MARGIN.RIGHT;
    // vis.WIDTH = 600 - MARGIN.LEFT - MARGIN.RIGHT;

    // vis.svg.style(vis.dimensions.height).style("height", vis.dimensions.width);
    vis.svg.attr('width', vis.WIDTH).attr('height', vis.HEIGHT);

    // labelki do dni
    vis.xLabels
      .attr('x', (d, i) => vis.xScale(i) + MARGIN.LEFT)
      .attr('y', vis.HEIGHT);

    // kolumny po dwie - podział na AM i PM
    vis.data.forEach((day, i) => {
      //AM
      vis.svg
        .append('g')
        .selectAll('rect')
        .data(day.Frequency.AM)
        .join('rect')
        .attr('x', vis.xScale(i) + MARGIN.LEFT)
        // WARNING tutaj posrana matma - dla pierwszej godizny zaczynamy od dołu MARGIN.TOP
        // druga godzina/kwadrat bieże wysokosc pierwszego  kwadratu/godziny + Padding
        .attr(
          'y',
          (d, j) =>
            j * (RECT_SIZE + PADDING) + MARGIN.TOP + 6 * PADDING
        )
        // trzecia godzina/kwadrat bieże wysokosć dwóch pierwszych godzin/kwadratów + PADDING
        .attr('width', RECT_SIZE)
        .attr('height', RECT_SIZE)
        .attr('fill', (d) => colorAssign(d));

      // PM
      vis.svg
        .append('g')
        .selectAll('rect')
        .data(day.Frequency.PM)
        .join('rect')
        // trzeba zrobić miejsce dla protstokąta AM
        .attr('x', vis.xScale(i) + MARGIN.LEFT + RECT_SIZE + PADDING)
        .attr(
          'y',
          (d, j) =>
            j * (RECT_SIZE + PADDING) + MARGIN.TOP + 6 * PADDING
        )
        .attr('width', RECT_SIZE)
        .attr('height', RECT_SIZE)
        .attr('fill', (d) => colorAssign(d));
    });

    // tytuł wykresu
    // vis.svg
    //   .append("text")
    //   .text("Calendar Heatmap")
    //   .attr("x", vis.WIDTH / 2 - MARGIN.LEFT)
    //   //   .attr("y", vis.HEIGHT / 10)
    //   .attr("y", MARGIN.TOP)
    //   .attr("fill", "black")
    //   .attr("font-size", 20);
  }
}
