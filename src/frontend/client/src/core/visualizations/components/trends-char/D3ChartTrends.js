import * as d3 from 'd3';
// TODO Multiple Lines Chart  https://www.goodmarketing.club/guide/d3-js-multiple-lines-chart-w-line-by-line-code-explanations/
// RESPONSYWNOŚC SVG
// TODO reponsywnowśc https://www.youtube.com/watch?v=T1L2ZY5QYBA
// https://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js

const MARGIN = { TOP: 5, BOTTOM: 40, LEFT: 70, RIGHT: 5 };

// const WIDTH = 500 - MARGIN.LEFT - MARGIN.RIGHT;
// const HEIGHT = 300 - MARGIN.TOP - MARGIN.BOTTOM;

export default class D3ChartTrends {
  constructor(element, dataArray, yearSelected) {
    let vis = this;

    d3.select('#trends-chart-id').remove();

    //   początkowe DIVA wymiary jak się otowrzy okno
    const currentSVG = d3.select('.dashboard__trends-chart').node();
    let currentSVGWidth = currentSVG.getBoundingClientRect().width;
    let currentSVGHeight = currentSVG.getBoundingClientRect().height;
    vis.HEIGHT = currentSVGHeight - MARGIN.TOP - MARGIN.BOTTOM;
    vis.WIDTH = currentSVGWidth - MARGIN.LEFT - MARGIN.RIGHT;

    console.log('currentSVGWidth: ', currentSVGWidth);
    console.log('currentSVGHeight: ', currentSVGHeight);

    vis.g = d3
      .select(element)
      .append('svg')
      .attr('class', 'trends-chart__svg')
      .attr('id', 'trends-chart-id')
      .attr('width', currentSVGWidth)
      .attr('height', currentSVGHeight)
      .style('background', 'white')
      .append('g')
      //   wyśrodkowanie wykresu wzgledem całego svg
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    // podpis osi Y
    vis.g
      .append('text')
      .attr('x', -(vis.HEIGHT / 2))
      .attr('y', -50)
      .attr('text-anchor', 'middle')
      .text('Vulnerabilities')
      .attr('transform', 'rotate(-90)');

    vis.xLabel = vis.g
      .append('text')
      .attr('x', vis.WIDTH / 2)
      .attr('y', vis.HEIGHT + 50)
      .attr('text-anchor', 'middle')
      //   text labelki się zmienia
      .text(yearSelected);

    // osie sie moga pokazac od razu

    // WARNING oś Y rośnie w dół - na odwrót
    vis.yScale = d3.scaleLinear().range([vis.HEIGHT, 0]);
    vis.yAxisGroup = vis.g.append('g');

    vis.xScale = d3.scaleBand().range([0, vis.WIDTH]).padding(0.2);
    vis.xAxisGroup = vis.g
      .append('g')
      //   na dół przenosi
      .attr('transform', `translate(0, ${vis.HEIGHT})`);

    vis.update(dataArray);
    // koniec konstruktora
  }

  // metoda update
  update(dataArray, yearSelected) {
    console.log('update method');
    console.log('dataArray: ', dataArray);
    let vis = this;
    vis.data = dataArray;

    // domain ustalam dopiero po aktualizacji danych
    // oś X
    // FIXME - nastawić się na długość danych
    vis.xScale.domain(vis.data.map((d) => d.month));
    // const numberArray = Array.from({ length: vis.data.lenght }, (v, k) => k);
    // console.log(numberArray);
    // vis.xScale.domain(numberArray.map((d) => d));
    const xAxisCall = d3.axisBottom(vis.xScale);
    vis.xAxisGroup.call(xAxisCall);

    // oś Y
    // generowanie listy numerów z numeru
    //  Array.from({ length: vis.data.lenght }, (v, k) => k + 1);

    const maxVulnerabilities = d3.max(
      vis.data,
      (d) => d.vulnerabilities
    );
    // WARNING oś Y rośnie w dół - na odwrót wartości
    vis.yScale.domain([0, maxVulnerabilities]);
    const yAxisCall = d3.axisLeft(vis.yScale);
    vis.yAxisGroup.transition().duration(500).call(yAxisCall);

    // opis wykresu - oś x
    vis.xLabel.text(yearSelected);

    // Dodanie wykresów
    const rects = vis.g.selectAll('rect').data(vis.data);

    // EXIT - usuwanie gdy sie zmieniaja dane
    rects
      .exit()
      .transition()
      .duration(500)
      //   zmiana osi teraz znika słupek jakby w dół a nie tak dziwnie nachodiz na ostatni
      .attr('height', 0)
      .attr('y', vis.HEIGHT - MARGIN.TOP - MARGIN.BOTTOM)
      .remove();

    // UPDATE
    rects
      .transition()
      .duration(500)
      .attr('x', (d) => vis.xScale(d.month))
      .attr('y', (d) => vis.yScale(d.vulnerabilities))
      .attr('width', vis.xScale.bandwidth)
      .attr(
        'height',
        (d) => vis.HEIGHT - vis.yScale(d.vulnerabilities)
      );

    // ENTER
    rects
      .enter()
      .append('rect')
      .attr('x', (d) => vis.xScale(d.month))
      .attr('y', (d) => vis.yScale(d.vulnerabilities))
      .attr('width', vis.xScale.bandwidth)
      .attr(
        'height',
        (d) => vis.HEIGHT - vis.yScale(d.vulnerabilities)
      )
      .attr('fill', 'lightblue');
  }
}
