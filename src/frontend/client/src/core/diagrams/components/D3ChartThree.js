// nie najbardziej optymalny import komponentów z biblioiteki  d3
// WARNING PODZIAŁ NA DWIE METODY
import * as d3 from 'd3';

// marginesy są w środku canvasa
const MARGIN = { TOP: 10, BOTTOM: 50, LEFT: 70, RIGHT: 10 };
// WIDTH i HEIGHT określają wielkość wykresu pomniejszony o marginesy gdzie jest cały wykres bez labelek osi
// HEIGHT odnosi się tylko do pola wykresu a nie całego svg
const WIDTH = 800 - MARGIN.LEFT - MARGIN.RIGHT;
const HEIGHT = 500 - MARGIN.TOP - MARGIN.BOTTOM;

export default class D3ChartThree {
  constructor(element, genderSelected) {
    // konstruktor który uruchamia się tylko raz
    // WARNING zabezpieczenie przed odnoszeniem się do dobrego this - tutaj żeby zawsze to było do instancji klasy - tutaj nazywam to vis od visualization
    const vis = this;

    // dopisanie wartości dropdown
    vis.genderSelected = genderSelected;
    console.log('vis.genderSelected: ', vis.genderSelected);

    // FIXME - sztuczka, żeby nie tworzyło dwóch svg o tym samym id - tylko, żeby jeden canvas został
    d3.select('#svg-id-3').remove();

    // const svg = d3
    // przypisanei zmiennej do instancji, tak, zżny metoda update() klasy miała dostęp do ego atrybutu
    vis.svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'svg-id-3')
      .attr('width', WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
      .attr('height', HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)
      .append('g')
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    // LABELKI - zawsze są na tej samej pozycji - więc moga być w konstruktorze
    // svg    // przypisanei zmiennej do instancji, tak, zżny metoda update() klasy miała dostęp do ego atrybutu
    // przyspianie do zmiennej żeby móc zmienić tekst pod wykresem
    vis.xLabel = vis.svg
      .append('text')
      .attr('x', WIDTH / 2)
      .attr('y', HEIGHT + 50)
      .attr('text-anchor', 'middle')
      //   text labelki się zmienia
      .text("The World's tallest men");

    // svg    // przypisanei zmiennej do instancji, tak, zżny metoda update() klasy miała dostęp do ego atrybutu
    vis.svg
      .append('text')
      .attr('x', -(HEIGHT / 2))
      .attr('y', -50)
      .attr('text-anchor', 'middle')
      .text('Heigh in cm')
      .attr('transform', 'rotate(-90)');

    vis.xAxisGroup = vis.svg
      .append('g')
      .attr('transform', `translate(0, ${HEIGHT})`);

    vis.yAxisGroup = vis.svg.append('g');

    // ładowanie danych - callback odpowiedzialny za ich wyświetlanie - zwraca Promise
    /*d3.json(url).then((data) => {
      // data  przypisanie do instancji klasy  D3ChartThree  // przypisanei zmiennej do instancji, tak, zżny metoda update() klasy miała dostęp do ego atrybutu
      vis.data = data;
      // callback odpowiedzialny za ładowanie danych
      // WARNING - d3.interval loop do animacji
      d3.interval(() => {
        console.log("Hello interval d3.js");
        //   tu gdzieś trzeba wcisnąc metodę update - jest w środku callbacka bo tutaj  ma dostęp do danych
        // this. odnosi się do instancji klasy D3ChartThree ale to dlatego, ze używamy arrowSyntax
        // this.update();
        // używam zmiennej `vis` zamiast this żeby mieć pewnosc że do  dobrej instancji (instancji tej klasy D3ChartThree) odnosi się this
        // możnaby przekazać jako paramatery ale terog nie chcemy
        // vis.update(data, svg); weżmiemy te dwie property jak d3 class instance
        vis.update();
      }, 1000);
    });*/

    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
    // Promise all do danych z dwóch urli - pozwala na pracę z wieloma promisami, gdzie można od razu żadać wszsytkich dancyh
    Promise.all([
      d3.json(
        'https://udemy-react-d3.firebaseio.com/tallest_men.json'
      ),
      d3.json(
        'https://udemy-react-d3.firebaseio.com/tallest_women.json'
      ),
    ]).then((datasets) => {
      console.log(datasets);
      vis.menData = datasets[0];
      vis.womenData = datasets[1];
      console.log('genderSelected: ', genderSelected);
      vis.update(vis.genderSelected);

      /*
      //wypakowanie dwóch list- dużo czytelniejsze
      const [men, women] = datasets;
      //   wcześniej dane przypisywaliśmy do vis.data a teraz chcemy żeby się zmieniały dane - FLAGA
      //   za pierwszym razem gdy program się uruchomi to flaga na true i mamy zbiór danych meżczyzn
      let flag = true;
      //fix - żeby wyświetliły sie dane mężczyzn - bo d3.interval czeka jedną sekundę na dane
      vis.data = men;
      vis.update();
      //   interval
      d3.interval(() => {
        // problem z intervalem - pierwszą sekundę nic się nie wyświetla bo czeka
        // coś jak setTimeout ale loop się nie kończy
        vis.data = flag ? men : women;
        vis.update();
        // zmiana wartosci flagi - za drugim razem uruchomi się ze zbiorem kobiet
        flag = !flag;
      }, 1000);
      */
    });

    // koniec konstruktora
  }

  //   metoda wenątrz klasy
  update(genderSelected) {
    // przypisanei this dfo zminnej żeby nie było problemu gdy użyje skłaski funckji innej niż arrowFunctionSyntax
    const vis = this;

    // wybieramy dane zależnie od selecta płci
    vis.data = genderSelected === 'men' ? vis.menData : vis.womenData;

    // aktualizacja podpisu wykresu - pod osią X zależnie od danych
    vis.xLabel.text(`The world's tallest ${genderSelected}`);

    // metoda w klasie - parametry któe się zmieniaja zależnie od dancyh
    //   scales - to trzeba do danych dostosować
    // const maxHeight = d3.max(data, (d) => {
    const maxHeight = d3.max(vis.data, (d) => {
      return d.height;
    });

    // const minHeight = d3.min(data, (d) => {
    const minHeight = d3.min(vis.data, (d) => {
      return d.height;
    });

    const y = d3
      .scaleLinear()
      .domain([minHeight * 0.95, maxHeight])
      .range([HEIGHT, 0]);

    console.log(y(272));

    const x = d3
      .scaleBand()
      //   .domain(data.map((d) => d.name))
      .domain(vis.data.map((d) => d.name))
      .range([0, WIDTH])
      .padding(0.4);

    const xAxisCall = d3.axisBottom(x);
    // dodanie do labelki X poziomej pod wykresem
    vis.xAxisGroup.call(xAxisCall);

    // svg
    /*
    vis.svg
      // tu prioblem bo co interval dodaję nowa grupę do svg i one na siebie nachodzą a CHCEMY DODAC TYLKO RAZ -> czyli W KONSTRUKTORZE a potem tylko aktualizować dane w grupie
      .append("g")
      .call(xAxisCall)
      .attr("transform", `translate(0, ${HEIGHT})`);
    */

    const yAxisCall = d3.axisLeft(y);
    // svg.append("g").call(yAxisCall);
    // dodanie transition bo oznaczenia osi Y pionowej centrymetry dziswnie przeksakuję
    vis.yAxisGroup.transition().duration(500).call(yAxisCall);

    // słupki też w metodzie update
    // const rects = svg.selectAll("rect").data(data);
    // DATA JOIN
    // mówi które dane chcemy assiociate with our shapes
    const rects = vis.svg.selectAll('rect').data(vis.data);

    //  EXIT - tu też transition żeby dziwnie nie znikały elementy
    rects
      .exit()
      .transition()
      .duration(500)
      //   zmiana osi teraz znika słupek jakby w dół a nie tak dziwnie nachodiz na ostatni
      .attr('height', 0)
      .attr('y', HEIGHT)
      .remove();

    // UPDATE
    rects
      // .append("rect") jak się tutaj doda append to słupki po kolei dodaje i jest DZIWNIE
      //   też wymagają transition - bo zmienia się pozycja
      .transition()
      .duration(500)
      .attr('x', (d) => x(d.name))
      .attr('y', (d) => y(d.height))
      .attr('width', x.bandwidth)
      .attr('height', (d) => HEIGHT - y(d.height));

    // ENTER
    rects
      .enter()
      .append('rect')
      .attr('x', (d) => x(d.name))
      .attr('width', x.bandwidth)
      .attr('fill', 'grey')
      //   .attr("y", HEIGHT) bez tego efekt jakby słupki spadały z góry
      .attr('y', HEIGHT)
      .transition()
      .duration(500)
      .attr('height', (d) => HEIGHT - y(d.height))
      .attr('y', (d) => y(d.height));

    console.log('po dodaniu', rects);

    // koniec metody update
  }
}
