// age and height are continuous
import * as d3 from 'd3';

const MARGIN = { TOP: 10, BOTTOM: 80, LEFT: 70, RIGHT: 10 };
const WIDTH = 500 - MARGIN.LEFT - MARGIN.RIGHT;
const HEIGHT = 300 - MARGIN.TOP - MARGIN.BOTTOM;

export default class D3ChartFour {
  constructor(element, dataArray, setActiveName) {
    let vis = this;
    vis.setActiveName = setActiveName;
    console.log('dataArray: ', dataArray);

    // FIXME - sztuczka, żeby nie tworzyło dwóch svg o tym samym id - tylko, żeby jeden canvas został
    // d3.select("#svg-id-4").remove();

    // vis.data = dataArray;

    vis.g = d3
      .select(element)
      .append('svg')
      .attr('id', 'svg-id-4')
      .attr('width', WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
      .attr('height', HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)
      .append('g')
      //   wyśrodkowanie wykresu wzgledem całego svg
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    //  ------------------- scales

    vis.x = d3
      .scaleLinear()
      //   domain aktualziuję w update, żeby na bieżco się resklaowało
      // odpowiada output values przeskalowanych do pikseli svg canvasa cześci przenzaczonych na wykres
      .range([0, WIDTH]);

    //  OŚ Y TU JEST DZIWNE< bo oś Y rośnie w dół
    vis.y = d3
      .scaleLinear()
      //   domain aktualziuję w update, żeby na bieżco się resklaowało
      .range([HEIGHT, 0]);

    // osie są stałe, wiec dopisuję je w konstruktorze
    // oś x domyslnie u góry svg
    vis.xAxisGroup = vis.g
      .append('g')
      //   na dół przenosi
      .attr('transform', `translate(0, ${HEIGHT})`);
    //   do update przenosze podpisy osi, bo mogą się zmienić gdy dane się zmienią

    vis.yAxisGroup = vis.g.append('g');

    // podpis osi X
    vis.g
      .append('text')
      .attr('x', WIDTH / 2)
      .attr('y', HEIGHT + 40)
      .attr('font-size', 20)
      .attr('text-anchor', 'middle')
      .text('Age');

    // WARNING opis osi Y - dziwne
    vis.g
      .append('text')
      .attr('x', -(HEIGHT / 2))
      .attr('y', -50)
      .attr('transform', 'rotate(-90)')
      .attr('font-size', 20)
      .attr('text-anchor', 'middle')
      .text('Heigh in cm');

    vis.update(dataArray);
    // koniec konstruktora
  }

  update(updatedArray, setActiveName) {
    let vis = this;
    vis.data = updatedArray;
    vis.setActiveName = setActiveName;

    console.log('updatedArray: ', updatedArray);

    vis.x // odpowiada input values które dodajemy do scale - dane od 0 do maskymalnego wzrostu z dancyh
      //   trzeba zamienić na liczbę, bo w pliku to stringi
      .domain([0, d3.max(vis.data, (d) => Number(d.age))]);

    vis.y
      //   trzeba zamienić na liczbę, bo w pliku to stringi
      .domain([0, d3.max(vis.data, (d) => Number(d.height))]);

    // osie - tworzenie
    const xAxisCall = d3.axisBottom(vis.x);
    const yAxisCall = d3.axisLeft(vis.y);

    // osie - dodawanie do screen + dodanie animacji
    // transition(1000) to sktór składni .transition().duration(1000)
    // vis.xAxisGroup.transition(1000).call(xAxisCall);
    vis.xAxisGroup.transition(1000).call(xAxisCall);
    // vis.yAxisGroup.call(yAxisCall);
    vis.yAxisGroup.transition(1000).call(yAxisCall);

    // DATA JOIN - where we connect and empty selection of circles to our data
    // FIXME  problem gdy są dwie osoby z tym samym imieniem - można np konkatencje trzech danych, albo dodac idki
    const circles = vis.g
      .selectAll('circle')
      .data(vis.data, (d) => d.name);

    // EXIT - what we remove any old elements from the screen
    // +animacja transitions przed usuniecie kółek + punk schodzi do zera
    // circles.exit().remove();
    circles.exit().transition(1000).attr('cy', vis.y(0)).remove();

    // UPDATE - when we rearrange existing circles which have changed positions
    // +animacja przed umieszczeniem kółek w nowej lokalizacji
    circles
      .transition(1000)
      .attr('cx', (d) => vis.x(Number(d.age)))
      .attr('cy', (d) => vis.y(Number(d.height)));

    // ENTER - we can add in new circles item in our array that have been added in
    // ENTER
    circles
      .enter()
      .append('circle')
      //   animacja w taki sposób że punkty zaczynają rosnąc od dołu wykresu
      .attr('cy', vis.y(0))
      .attr('cx', (d) => vis.x(d.age))
      .attr('r', 5)
      .attr('fill', 'grey')
      // WANRING event listener żeby po kliknięciu na odpowiednie kółeczko ustawiała się zmienna activName z Reacta i  klsa css zmieniała  na aktywną
      //   pierwszy argument - rodzaj zdarzenia  tutaj klik, funckja którą chcemy wywołać
      //   do d mamy dostęp bo korzystamy z metod biblioteki d3
      //  BUG trzeba e też wziać jako argument https://stackoverflow.com/questions/67314864/d3-js-undefined-data-value-in-callback-function-click-event
      .on('click', (e, d) => vis.setActiveName(d.name))
      .transition(1000)
      //   teraz ładnie kropki wjadą na swoje miejsce
      .attr('cy', (d) => vis.y(d.height));
  }
}
