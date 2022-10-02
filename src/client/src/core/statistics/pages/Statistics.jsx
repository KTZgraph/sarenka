// https://www.youtube.com/watch?v=T1RgT0Yh1Lg

import { useState } from "react";
import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import "./Statistics.scss";

const Statistics = () => {
  // 1) Setup Initila data and settings -----------------------------------------------------------------------------
  const initialData = [
    {
      name: "Car",
      value: 10,
    },
    {
      name: "Food",
      value: 3,
    },
    {
      name: "Telephone",
      value: 9,
    },
    {
      name: "Electricity",
      value: 7,
    },
    {
      name: "Cinema",
      value: 7,
    },
  ];

  // dane do ustawienia chartów ich wygladau
  const width = 500;
  const height = 150;
  const padding = 20;
  const maxValue = 20; //Maximum data value

  const [chartdata, setChartdata] = useState(initialData);

  // 2) Setup random data generator and SVG canvas ------------------------------------------------------------------
  // 3) Setup functions for Scales ----------------------------------------------------------------------------------
  // 4) Setup functions to draw Lines -------------------------------------------------------------------------------
  // 5) Draw line ---------------------------------------------------------------------------------------------------
  // 6) Setup functions to draw  X and Y Axes -----------------------------------------------------------------------
  // 7) Draw x and y Axes -------------------------------------------------------------------------------------------
  return (
    <>
      <Sidebar currentPage="statistics" />
      <main>
        <Navbar />
        <div className="main__container">
          {/* canvas do svg gdzie będziemy rysować paths*/}
          {/* viewBox - canvas are for a chart */}
          <svg id="chart" viewBox="0 0 500 150">
            <rect width="500" height="150" fill="blue" />
            {/* do d="" inject data , specyficzne komendy zeby rysować dane wielki M  - move i wielkie L - linia*/}

            <path
              d="M50,50 L100,150"
              fill="none"
              stroke="black"
              strokeWidth="5"
            />
          </svg>
        </div>
      </main>
    </>
  );
};

export default Statistics;
