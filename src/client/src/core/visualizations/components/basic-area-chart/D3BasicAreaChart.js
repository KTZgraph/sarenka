/*
https://www.youtube.com/watch?v=bt5Cq1Qr-90
*/
import * as d3 from 'd3';
const MARGIN = { TOP: 5, BOTTOM: 30, LEFT: 20, RIGHT: 80 };

// FIXME RESPONSYWNOŚC SVG
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

export default class D3BasicAreaChart {
  constructor(element, dataArray) {
    console.log('dataArray constructor: ', dataArray);

    // FIXME - sztuczka z usuwaniem jednej referencji
    d3.select('#basic-are-chart-id').remove();

    let vis = this;
    vis.data = dataArray;

    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'basic-are-chart-id')
      .attr('class', 'basic-are-chart')
      //   .attr("width", 800)
      //   .attr("height", 400)
      .style('width', '100%')
      .style('height', '100%')
      .style('border', '1px solid red');

    //   rozmiar SVG
    const currentSVG = d3.select('#basic-are-chart-id').node();
    let currentSVGWidth = currentSVG.getBoundingClientRect().width;
    let currentSVGHeight = currentSVG.getBoundingClientRect().height;
    vis.HEIGHT = currentSVGHeight - MARGIN.TOP - MARGIN.BOTTOM;
    vis.WIDTH = currentSVGWidth - MARGIN.LEFT - MARGIN.RIGHT;

    // skala X
    vis.xScale = d3
      .scaleTime()
      // metoda extend daje pierwszy i ostatni element z listy
      //   d3.timeParse(mojString) trzeba zamienić stringas na datę
      .domain(d3.extent(vis.data, (d) => d3.timeParse('%Y')(d.year)))
      //   szerokość - to szerokość SVG - 100px
      .range([0, vis.WIDTH - MARGIN.LEFT - MARGIN.RIGHT]);

    // wywołanie osi X - chcemy oś na dole
    vis.svg
      .append('g')
      .call(d3.axisBottom(vis.xScale))
      // przenoszenie osi na dół wykresu
      .attr(
        'transform',
        `translate(${MARGIN.LEFT}, ${vis.HEIGHT - MARGIN.BOTTOM})`
      );

    //   skala Y
    vis.yScale = d3
      .scaleLinear()
      .domain([0, d3.max(vis.data, (d) => d.count)])
      .range([vis.HEIGHT - MARGIN.BOTTOM - MARGIN.TOP, 0]);

    // wywołanie osi Y
    vis.svg
      .append('g')
      .call(d3.axisLeft(vis.yScale))
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    //TODO   AREA - tworzenie jak rects - potem JOIN, EXIT, UPDATE i ENTEr dorobić
    const area = d3
      .area()
      //WARNING  pamietac o parsowaniu STRINGA  na CZAS d3.timeParse
      .x((d) => vis.xScale(d3.timeParse('%Y')(d.year)))
      //   .y0 dół area
      .y0(vis.yScale(0))
      //   y1
      .y1((d) => vis.yScale(d.count));

    //dołożenie wykresu area do svg
    vis.svg
      .append('path')
      .datum(vis.data)
      .attr('d', area)
      .attr('fill', 'lightblue')
      .attr('stroke', 'darkblue')
      .attr('stroke-width', 2)
      .attr('transform', `translate(${MARGIN.LEFT},${MARGIN.TOP})`);

    //   koniec konstruktora
    vis.update(dataArray);
  }

  update(dataArray) {
    console.log('dataArray update: ', dataArray);
    let vis = this;
    vis.data = dataArray;
  }
}
