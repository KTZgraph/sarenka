// nie najbardziej optymalny import komponentów z biblioiteki  d3
import * as d3 from 'd3';

// syntax d3js
const url = 'https://udemy-react-d3.firebaseio.com/ages.json';

export default class D3ChartOne {
  constructor(element) {
    // FIXME - sztuczka, żeby nie tworzyło dwóch svg o tym samym id - tylko, żeby jeden canvas został
    d3.select('#svg-id-1').remove();

    const svg = d3
      .select(element)
      // method chaining
      .append('svg')
      .attr('id', 'svg-id-1')
      .attr('width', 500)
      .attr('height', 500);

    // ładowanie do D3 danych typu json - zwraca promisa
    // .then callback powinien mieć jeden argument który daje dostęp do danych
    // callback odpowiada za całe wyśietlanie danych bo ma do nich dostęp
    d3.json(url).then((agesData) => {
      console.log(agesData);
      //   robienie prostokątów na podstawie danych jsona
      //   json to lista obiektów - uwaga na ustawianie parametrów z dsanych
      const rects = svg.selectAll('rect').data(agesData);
      rects
        // enter() methoda
        .enter()
        .append('rect')
        //   używamy metody .data(mojeDane) - wiec nie trzeba forEchat żeby dostać się do parametrów
        //    d- elem,ent z Array data , idx to indeks
        .attr('x', (d, idx) => idx * 100)
        .attr('y', 50)
        .attr('width', 50)
        .attr('height', (d) => d.age * 10)
        .attr('fill', (d) => {
          // kolorowanie zależnie od wartosci atrybutu  .name obiektu
          if (d.age > 10) {
            return 'red';
          }
          return 'green';
        });
    });

    // data.forEach((d, idx) => {
    //   //   dodanie protostokąta
    //   svg
    //     .append("rect")
    //     .attr("x", idx * 100)
    //     .attr("y", 50)
    //     .attr("width", 50)
    //     .attr("height", d)
    //     .attr("fill", "grey");
    // });

    //
  }
}
