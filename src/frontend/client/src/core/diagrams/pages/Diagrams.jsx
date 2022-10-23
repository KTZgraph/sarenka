import Navbar from '../../../shared/navbar/Navbar';
import Sidebar from '../../../shared/sidebar/Sidebar';
import ChartWrapperOne from '../components/ChartWrapperOne';
import ChartWrapperTwo from '../components/ChartWrapperTwo';
import ChartWrapperThree from '../components/ChartWrapperThree';
import ChartWrapperFour from '../components/ChartWrapperFour';

import './Diagrams.scss';

const Diagrams = () => {
  return (
    <>
      <Sidebar currentPage="diagrams" />
      <main>
        <Navbar />
        <div className="main__container diagrams">
          <h1>Diagramy</h1>
          <h2>ScatterPlot</h2>
          <ChartWrapperFour />
          <h2>
            barchart ChartWrapperThree animacja wzrostu kobbie i
            mężczyzn
          </h2>
          <ChartWrapperThree />
          <h2>
            barchart ChartWrapperTwo BarChart wzrost najwyższych
            mężczyzn
          </h2>
          <ChartWrapperTwo />
          <h2>barchart ChartWrapperOne wiek</h2>
          <ChartWrapperOne />
        </div>
      </main>
    </>
  );
};

export default Diagrams;
