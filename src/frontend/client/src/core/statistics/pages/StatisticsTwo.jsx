import { useRef } from "react";

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import "./StatisticsTwo.scss";

const StatisticsTwo = () => {
  const svgRef = useRef();

  return (
    <>
      <Sidebar currentPage="statistics" />
      <main>
        <Navbar />
        <div className="main__container statistics-two">
          <h1>https://www.youtube.com/watch?v=bUM0m-cYVuQ</h1>
          <h2>
            https://dhsiteorg.files.wordpress.com/2021/11/datavis-d3js.pdf
          </h2>
          <h3>
            https://www.theguardian.com/environment/interactive/2013/may/14/alaska-villages-frontline-global-warming
          </h3>
          <h3>
            https://archive.nytimes.com/www.nytimes.com/interactive/2012/09/06/us/politics/convention-word-counts.html
          </h3>
          <h3>
            https://www.nytimes.com/newsgraphics/2013/09/07/director-star-chart/index.html
          </h3>
          {/* svg do wykresów */}
          <svg
            className="chart-statistics-two"
            id="chart-statistics-two"
            viewBox="0 0 500 150"
            ref={svgRef}
          >
            <path d="" fill="none" stroke="black" strokeWidth="5" />
          </svg>
        </div>
      </main>
    </>
  );
};

export default StatisticsTwo;
