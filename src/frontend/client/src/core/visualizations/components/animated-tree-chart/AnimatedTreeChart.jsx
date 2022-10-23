// hierarchy funckja transofrmuje dane pozwala na ektrachowanie nodów i linków naszych danych
//https://github.com/d3/d3-hierarchy#cluster nie trzeba manualnie przechodizć przez nody z hierarchy(data)
// https://github.com/d3/d3-hierarchy#tree podobne do clustera
// https://github.com/d3/d3-hierarchy#treemap to akurat działa inaczej

// linkVertical do połączenie linków w drzewie, nazywa się linkVertical "Vertical" bo są połaczeniem od roota do dziecka a domyślnie drzewo jest pionowe góra dół
// WARNING tak żeby wykres był pionowy linkVertical
// WARNING tak żeby wykres był poziomy linkHorizontal

// animacja
// stroke-dasharray i stroke-dashoffset do animowania zmian - //links     svg.selectAll(".link")
// stroke-dasharray i stroke-dashoffset atrybuty na <path> element które można ustawić, które typowo ustawiaja jak stroke jest dashed

// FIXME FIXME FIXME Improve - animacj atrigeruje się od nowa
// wyciągnac funckje do pliku, bo za każdnym razem gdy okno jest rezied a całąśc jest w useEffect zaleznym od dimensions to animacja się trigeruje od nowa

import {
  select,
  hierarchy,
  tree,
  linkVertical,
  linkHorizontal,
} from 'd3';
import React, { useRef, useEffect } from 'react';

import useResizeObserver from '../../../../hooks/useResizeObserver';

function AnimatedTreeChart({ data }) {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  useEffect(() => {
    const svg = select(svgRef.current);
    if (!dimensions) return;

    // dane zagnieżdżone jsony
    const root = hierarchy(data);
    // flat array używana do renderowania wszystkich 6 Nodów/doc łacznie z elementem root, jest informacja o głebości parametr "depth"
    console.log(root.descendants());
    // flat array 5 obiektów, które reprezentują bezposrednie połączenie z między naszą dataArray
    // ma property source i target, które wskazują na inen punkty Node
    // pierwszy element wskazuje na połaczenie między root element a jednym z jego dzieci, pierwszy poziom
    // ta lista będzie do renderowania linków międyz danymi
    console.log(root.links());

    // tutaj podajemy szerokosć i wysokosć
    // WARNING tak żeby wykres był piowy
    // const treeLayout = tree().size([dimensions.width, dimensions.height]);
    // WARNING tak żeby wykres był poziomy
    const treeLayout = tree().size([
      dimensions.height,
      dimensions.width,
    ]);
    // treeLayout defaultowy renderuje drzewo w pionie od góry do dołu
    treeLayout(root);

    // po użyciu treeLayout(root) teraz mają koordynaty x i y
    console.log(root.descendants());
    console.log(root.links());

    // nodes
    // d3.js wybiera wszystkie elemnty z klasą .node i sychnronizuje z danymi
    // WARNING dane to teraz root.descendants() zamiast po prostu data
    // stworzy 6 kółeczek
    svg
      .selectAll('.node')
      .data(root.descendants())
      .join('circle')
      //   klasa do kółek bo potem można je aktualizować
      .attr('class', 'node')
      .attr('r', 4)
      .attr('fill', 'black')
      // WARNING callback ma teraz dostęp do danych z  root.descendants()
      //   property x i y wpsółrzedne Nodów są  wziete z treeLayout(root);
      //   FIZME - przekalowac współrzędne tak żeby się zmieściły
      //   WARNING tak żeby wykres był pionowy
      //   .attr("cx", (node) => node.x)
      //   .attr("cy", (node) => node.y);
      //   WARNIGN tak żeby wykres był poziomy
      .attr('cx', (node) => node.y)
      .attr('cy', (node) => node.x)
      //   dane przed animacją - opacity 0 żeby było niewiodzne
      .attr('opacity', 0)
      .transition()
      //   WARNING animacja ze wzgledu na głebokośc nodów
      .duration(500)
      // ta sama logika oopóźnienia animacji, zeby animowało się też wejście wierzchołka root
      .delay((node) => node.depth * 500)
      //   opacity żeby było widoczne
      .attr('opacity', 1);

    //   WARNING helps with the "d" attribute of a path element
    // połączenia miedzy wierzchołkami (kółkami) linkVertical
    // linkGenerator dostaniepóźniej jeden z obiektów link root.links() żeby wiedziec, co jest source Node a co jest target Node
    // teraz jak mam linkGenerator to mogę ich użyć do mojego svg
    // same linki będą elementami <path> z svg a sam linkGenerator pozwoli pomóc wygenerować wartośc atrybutu "d" na ścieżkach
    // też wie gdzie sie linia zaczyna gdzie kończy, w jakis sposób ma być zakrzywiona
    // WARNING tak żeby wykres był pionowy
    // const linkGenerator = linkVertical()
    // WARNING tak żeby wykres był poziomy
    const linkGenerator = linkHorizontal()
      // WARNING  source i target sa defaultowo wiec nie muszę ich definiowac tak jak tutaj, bo i tak używam w ten sposób link ocjects
      //   .source((link) => link.source)
      //   .target((link) => link.target)
      //   potrzebujee koordynatów x startowego noda i koordynaty x docelowego Noda
      //   WARNING tak żeby wykres był piowny  .x((node) => node.x) .y((node) => node.y);
      //   .x((node) => node.x)
      //   .y((node) => node.y);
      //   tak zeby wykres był poziomy
      .x((node) => node.y)
      .y((node) => node.x);

    //   links - dodawanie liinków do canvasa svg
    // WARNIGN teraz dane to root.links()
    svg
      .selectAll('.link')
      .data(root.links())
      // dla każdego fragmentu danych chcę wygenerowac path element
      .join('path')
      .attr('class', 'link')
      //   domyślnei fill  bardzo brzydkie kształy koloruje
      .attr('fill', 'none')
      .attr('stroke', 'black')
      //   teraz zeby były widoczne trzeba atrbutu "d" z <path d="..."> dodać, ale wartosc tego atrybutu jest generowana przez linkGenerator
      //   dane to root.links() więc  linkObj jest jednym  elementem z płaskiego array flat array 5 obiektów, które reprezentują bezposrednie połączenie z między naszą dataArray
      // WARNING  .attr("d", (linkObj) => linkGenerator(linkObj)); skrótowy zapis to po prostu podanie callbacka bez parametrów, bo linkObj z root.links() jest domyślnie zwracany
      //   .attr("d", (linkObj) => linkGenerator(linkObj));
      .attr('d', linkGenerator)
      //   animacja
      //   WARNING  stroke-dasharray i stroke-dashoffset celem jest animowanie tego offsetu 225 back to zero so that invisible line moves out and the visible line moves
      //   WARNING back in i to jest cały trick za animacją
      //   .attr("stroke-dasharray", "100 50"); linia się renderuje przez 100 jednostek a potem przerywa na 50 jednostek i znowu się renderuje na 100 jednostek
      //   .attr("stroke-dasharray", "225 225") zahardkowane na sztywno
      // FIXME - żeby zrobić dobra animację trzeba obliczyć aktualną długosć ścieżki
      .attr('stroke-dasharray', function () {
        // RESPONSWYNOSC
        // callback tutaj mamy dostęp do aktualnej długosci ścieżki
        // WARNING zwykład funckja, bo chcemy się dostać do "this" ktroy jest niedsotępny w ()=>{}
        // .getTotalLength() metoda która zwraca dłguosc <path>
        const length = this.getTotalLength();
        // jedna wartosc dla widocznej czeście, druga wartosc dla NIEWiwodocznej ścieżki
        // BUG trzeba zrobić stringa z wartości
        return `${length} ${length}`;
      })

      //    stroke-dashoffset trochę tak przesuwa tę niewidzialną linię na sam początek
      //   stroke-dashoffset tak trochę jak gumka, albo renderowanie niewidzialnej linii
      //   stroke-dashoffset przeuwa ten pattern rysowania linków o pewną wartość na sztywno - taka transofrmacja jak w macierzach
      //   .attr("stroke-dashoffset", 100) teraz linia zaczyna się od wierzchołka z przerwą na samym początku przez 100 jednostek, POTEM dopiero renderuje 100 jednostek
      //   .attr("stroke-dashoffset", 100);
      //   przed animacją neiwidoczne
      //   .attr("stroke-dashoffset", 225) ZAHARDKODOWANE
      .attr('stroke-dashoffset', function () {
        // RESPONSWYNOSC
        // callback tutaj mamy dostęp do aktualnej długosci ścieżki
        // WARNING zwykład funckja, bo chcemy się dostać do "this" ktroy jest niedsotępny w ()=>{}
        // .getTotalLength() metoda która zwraca dłguosc <path>
        const length = this.getTotalLength();
        // BUG trzeba zrobić stringa z wartości
        return `${length}`;
      })
      //   animowanie żeby wróciła linia
      .transition()
      .duration(500)
      //   WARNING - delay() zależnie od głebokosci żeby najwpier animował się pierwszy node a potem drugi - jakby linia rosła od wierzchołków
      //   clalback żeby wziac wartośc z obiektu - dane to root.links()
      //   linkObj.source to obiekt Node
      //   przemnozenie o 500 ms tak jak pierwszy czas animacji o wierzchołka root się animował
      .delay((linkObj) => linkObj.source.depth * 500)
      //   trik polega na tym, ze te "stroke-dasharray" i "stroke-dashoffset" ustawić na całą długość path
      //  WARNING  jak stroke-dashoffset ustawi się na zero to zwnou widzimy linię
      .attr('stroke-dashoffset', 0);

    // labels
    // labelki opisujące wierzchołki
    svg
      .selectAll('.label')
      .data(root.descendants())
      .join('text')
      .attr('class', 'label')
      .text((node) => node.data.name)
      .attr('text-anchor', 'middle')
      .attr('font-size', 12)
      //   teraz trzeba je wypozycjonować tak, żeby były nad kółkami
      // WARNING współrzedne na odwrót żeby wykres był poziomy
      .attr('x', (node) => node.y)
      //   -10 żeby był troszeczkę napis nad kółkiem
      .attr('y', (node) => node.x - 10)
      //   POD ANIIMACJE labelek, zeby one też dopiero się pojawiały jak kólka nody i links p<path> ze wzgledu na poziomy głebokości
      // opacity, zeby było niewiodczne przed animacją
      .attr('opacity', 0)
      .transition()
      .duration(500)
      // callbakc opóźnienie ze względu na głebokosc noda, node to obiekt z listy root.descendants()
      .delay((node) => node.depth * 500)
      .attr('opacity', 1);
  }, [data, dimensions]);

  return (
    <div
      ref={wrapperRef}
      style={{
        marginBottom: '2rem',
        maxWidth: '100%',
        maxHeight: '100%',
        overflow: 'visible',
      }}
    >
      <svg
        ref={svgRef}
        style={{
          maxWidth: '100%',
          maxHeight: '100%',
          overflow: 'visible',
        }}
      ></svg>
    </div>
  );
}

export default AnimatedTreeChart;
