import { useRef, useEffect } from 'react';
import { select, hierarchy, forceSimulation } from 'd3';
import useResizeObserver from '../../../../hooks/useResizeObserver';

/*
component, that renders a force layout for hierarchical data
*/

const PhysicsBasedForceLayout = ({ data }) => {
  const svgRef = useRef();
  const wrapperRef = useRef();
  const dimensions = useResizeObserver(wrapperRef);

  // will be calle dinitailly and on every data change
  useEffect(() => {
    if (!dimensions) return;
    const svg = select(svgRef.current);

    // d3 util to work with hierarchical data
    const root = hierarchy(data);
    //   wierzchołki
    const nodeData = root.descendants();
    //   połaćzeniamiedzy wezłami
    //   WARNING nodeData są referencją w danych linkData dlatego też x, y moga być wzięte podczas svg.<..>.data(linkData)
    const linkData = root.links();

    //   jako argument, do czego chce dodac siłę - chcę do moich nodów
    const simulation = forceSimulation(nodeData)
      // WARNING force - te alphaTarget i alphaMin z 'tick' emulują/zmieniają dane

      // alphaTarget dzięki temu symulacja jest nieskończona, ale ona się nigdy nie skońcyzć bo symulacja sie kończy na punkcie 0.001
      .alphaTarget(0.2)
      // .alpahMin - punk zakończenia symulacjia
      .alphaMin(0.5)
      //   tworzenie symulacjia
      .on('tick', () => {
        // tick jest wywoływany tak długo jak długo działa symulacja
        // by default zaczyna się od wartości simulation.alpha 1 a końcyz się gdy simulation.alpha wynosi 0.001cośtam
        //   funckja zostanie wywołana
        // simulation obiket któy dostajemy docallbacka,
        // simulation.alpha jest do aktualnej wartości siły
        console.log('current force', simulation.alpha());

        //  WARNING render our nodes, links
        // links
        svg
          .selectAll('.link')
          .data(linkData)
          .join('line')
          .attr('class', 'link')
          .attr('stroke', 'black')
          .attr('fill', 'none')
          //WARNING  x, y bardzo ważne - one nie są generowane przy const linkData = root.links();
          // WARNING one są dodawane podczas symulacji forceSimulation(nodeData) tutaj siła dodaje wsóółrzędne
          .attr('x1', (link) => link.source.x)
          .attr('y1', (link) => link.source.y)
          .attr('x2', (link) => link.source.x)
          .attr('y2', (link) => link.source.y);

        // nodes
        //   renderuje wszystkei nody
        svg
          .selectAll('.node')
          // przekazuję nodeData
          .data(nodeData)
          // dla każdego noda tworzę kółko
          .join('circle')
          .attr('class', 'node')
          .attr('r', 4)
          // tu dodaje wsłrzedne x, y które są generowane przez forceSimulation forceSimulation(nodeData)
          .attr('cx', (node) => node.x)
          .attr('cy', (node) => node.y);

        // labels
        svg
          .selectAll('.label')
          .data(nodeData)
          .join('text')
          .attr('class', 'label')
          .attr('text-anchor', 'middle')
          .attr('font-size', 10)
          .text((node) => node.data.name)
          .attr('x', (node) => node.x)
          .attr('y', (node) => node.y);
      });
  }, [data, dimensions]);

  return (
    <div ref={wrapperRef} style={{ marginBottom: '2rem' }}>
      <svg ref={svgRef}></svg>
    </div>
  );
};

export default PhysicsBasedForceLayout;
