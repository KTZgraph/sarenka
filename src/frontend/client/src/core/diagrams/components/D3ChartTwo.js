// nie najbardziej optymalny import komponentów z biblioiteki  d3
import * as d3 from 'd3';

const url = 'https://udemy-react-d3.firebaseio.com/tallest_men.json';

// marginesy są w środku canvasa
const MARGIN = { TOP: 10, BOTTOM: 50, LEFT: 70, RIGHT: 10 };
// WIDTH i HEIGHT określają wielkość wykresu pomniejszony o marginesy gdzie jest cały wykres bez labelek osi
// HEIGHT odnosi się tylko do pola wykresu a nie całego svg
const WIDTH = 800 - MARGIN.LEFT - MARGIN.RIGHT;
const HEIGHT = 500 - MARGIN.TOP - MARGIN.BOTTOM;

export default class D3ChartTwo {
  constructor(element) {
    // FIXME - sztuczka, żeby nie tworzyło dwóch svg o tym samym id - tylko, żeby jeden canvas został
    d3.select('#svg-id-2').remove();

    const svg = d3
      .select(element)
      .append('svg')
      .attr('id', 'svg-id-2')
      //   dynamiczna szerokość
      //   .attr("width", 800)
      .attr('width', WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
      //   dynamiczna wysokość
      //   .attr("height", 500);
      .attr('height', HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)
      //   dodawanie grupy do naszego svg canvasa
      .append('g')
      //   transformacja żeby przestrzeń była na śrdoku a nie marginesy tylko po prawej i na dole
      .attr('transform', `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

    //   pobranie danych do projektu
    // promise . then callback z argumentem do data
    d3.json(url).then((data) => {
      //   console.log(data);
      // https://github.com/d3/d3-array#statistics
      //   maksymalna wartośc dla osi Y wzrostu
      const maxHeight = d3.max(data, (d) => {
        // drugi argument to funckja, tutuaj dla osiy ma zwracać wzrost mężczyzn
        // d3.max uruchiomi tę funckje dla każdego alementu i zwrócić max atrybutu tutaj d.heigh
        return d.height;
      });

      const minHeight = d3.min(data, (d) => {
        return d.height;
      });

      // scales
      const y = d3
        .scaleLinear()
        //   domain([minimuValue, maxValue - tutaj najwyższy mężczyna 272 cm ale to wiem z danych bo je ręcznie przejrzałam])
        // .domain([0, 272])
        // dynamiczna wartosc maksymalnej wartosci wzrostu - DYNAMICZNE dane
        // ttuaj mężczyźni maja podobny wzrost więc skala od zera jest mało przejrzysta
        // .domain([0, maxHeight])
        // żeby minimalna wartosc to było 250cm a NIE 0 jeśli osoby są podobengo wzrostu - różnica wzosru staje się wyraźniejsza
        // .domain([250, maxHeight]) //na sztywno minimalna wartość
        // DYNAMICZNIE minimalna wartość wykresu - razy 0.95 żeby tak głupio jeden słupek nie był w ogóle widocnzy
        .domain([minHeight * 0.95, maxHeight])
        //   range - pixele u nas max 500
        // .range([0, 500]);
        // dynamicznie ma przeliczać sobie scale na piksele
        // .range([0, HEIGHT]); 1) zmiana skali żeby działa w drugą stronę u góry maksymalna wartość (koordynaty 0,0 czyli lewy górny róg)
        // minimlan wartośc to height - lewy górny róg a maksymalna to 0
        // .range([HEIGHT, 0]); dane - słupki sie wzięły zrobiły ultra malutkie
        .range([HEIGHT, 0]);

      // scaleLinear zwraca funckję
      console.log(y(272));

      //   oś x po kategoriach męzczyzn - po imionach mężczyzn
      const x = d3
        .scaleBand()
        .domain(data.map((d) => d.name))
        //   jak w lionwe - pierwsza najmneijsza wartość pikxele , druga najwięskza wartośc pikseli
        // dynaczminicze ma przeliczac sobie oś X
        // .range([0, 800])
        .range([0, WIDTH])
        //   tu paddingi trzeba na wyczucie sprawdzać aż wizualnie nam pasują
        .padding(0.4);

      // https://github.com/d3/d3-axis
      // WARNING  tworzenie osi X
      //   d3.axisBottom(x) jako argument scalę x
      const xAxisCall = d3.axisBottom(x);
      //   dodanie osi do wykresu svg.call(xAxisCall);
      //   svg.call(xAxisCall); dodaje oś do góry góra lewy róg -,- brzydko
      //   svg.call(xAxisCall);
      //   dodanie grupy dla każdej z osi bez tego dodaje tylko ostanią oś
      //   svg.append("g").call(xAxisCall); domyslnie oś jest u górysvg canvas
      svg
        .append('g')
        .call(xAxisCall)
        //   transformacja osi X na dół, żeby zero było u dołu podpisy imion
        .attr('transform', `translate(0, ${HEIGHT})`);

      //WARNING   tworzenie osi Y
      // argument to scala y
      const yAxisCall = d3.axisLeft(y);
      //   svg.call(yAxisCall); PROBLEM dodaje tylko drugą oś -,- i żadne ticks się ni epojawiają ale one są tutaj po lewej stronie i nie mieszczą się w svg
      //   svg.call(yAxisCall);
      //   svg.append("g").call(yAxisCall); domyslnie zaczyna się od góry do dołu oś
      svg.append('g').call(yAxisCall);
      //   od o w dół do 260 jest domyślnie

      // WARNING dodanie labelki pod osią X - legenda na dole wykresu
      // svg reprezentuje tutaj grupę
      //   .append("text") odnosi się do lementu <text> w svg
      //   pierwsze trzeba dac im x i y pozycję
      svg
        .append('text')
        .attr('x', WIDTH / 2)
        .attr('y', HEIGHT + 50) //heigh to wysokosc pola któa rośnie w dół wykresu + 50 px żeby była przestrzeń od imion na osi X
        // jest na dole po prawej bardziej labelka - trzeba wyśrodkowac text
        // .attr("text-anchor", "middle") wyśrodkowuje text ładnie
        .attr('text-anchor', 'middle')
        .text("The World's tallest men");

      // WARNING dodanie labelki przd/po lewej osi Y
      svg
        .append('text')
        //   FIXME - jak się zrobi obrót to punk rozpoczęcia labelki też się obraca - to trzeba metodą prób i błędów .attr("x", -20) .attr("y", HEIGHT / 2)
        // .attr("x", -50)
        // .attr("y", HEIGHT / 2) //labelka w połowie wyokośći wykresu (nie całego SVG)
        .attr('x', -(HEIGHT / 2))
        .attr('y', -50)
        .attr('text-anchor', 'middle')
        .text('Heigh in cm')
        // transformacja, żeby napis był niestandardowo - obrót wzgledem wskazówek zegara
        .attr('transform', 'rotate(-90)');

      const rects = svg.selectAll('rect').data(data);
      rects
        .enter()
        .append('rect')
        // .attr("x", (d, idx) => idx * 100)
        // scala x po imionach/kategoriacj mężczyzn
        .attr('x', (d) => x(d.name))
        // attr("y", 0) sprawia że słupki zaczynaja się od góy, bo corrdynaty (0,0) dla d3.js to lewy gróny róg
        // .attr("y", 0)
        // żeby wykres był od dołu to od wysokosći odejmuję przeskalowaną dla danych  wyskokosc słupka w pikselach
        // .attr("y", (d) => HEIGHT - y(d.height))
        // zmiana scali y .range([HEIGHT, 0]); sprawia że słupki teraz są malutki
        // jak obróciliśmy skalę, to musimy obrócić wartości - teraz wartośc 0 daje wartośc 500px
        // .attr("y", (d) => HEIGHT - y(d.height))
        // żeby słupki znowu były od góy rysowane
        .attr('y', (d) => y(d.height))
        // dynamicznie szerokość - po osi x miedzy słupkami
        // .attr("width", 50)
        .attr('width', x.bandwidth)
        // d.height atrybut obiektu z listy danych z jsona
        // .attr("height", (d) => d.height)
        // y funckja scali z d3.scaleLinear
        // teraz od całej wysokosci svg canvas trzeba odjąć wysokosc danych
        // .attr("height", (d) => y(d.height))
        .attr('height', (d) => HEIGHT - y(d.height))
        .attr('fill', 'grey');
    });
  }
}
