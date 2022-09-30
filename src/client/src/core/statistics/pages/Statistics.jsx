import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import "./Statistics.scss";

const Statistics = () => {
  return (
    <>
      <Sidebar currentPage="statistics" />
      <main>
        <Navbar />
        <div className="main__container">
          <h1>Statystki D3.js</h1>
        </div>
      </main>
    </>
  );
};

export default Statistics;
