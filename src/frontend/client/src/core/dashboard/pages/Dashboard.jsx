import Sidebar from "../../../shared/sidebar/Sidebar";
import Navbar from "../../../shared/navbar/Navbar";
import Widget from "../components/Widget";
import Featured from "../components/Featured";
import Chart from "../components/Chart";
import Hometable from "../components/Hometable";

import "./Dashboard.scss";
const Dashboard = () => {
  return (
    <>
      <Sidebar currentPage="home" />
      <main>
        <Navbar />
        <div className="main__container dashboard">
          <div className="dashboard__container">
            <div className="dashboard__widgets">
              <Widget type="user" />
              <Widget type="order" />
              <Widget type="earnings" />
              <Widget type="balance" />
            </div>
            <div className="dashboard__charts">
              {/* wykresiki */}
              <Featured />
              <Chart chartTitle="Last 6 Months (Revenue)" chartAspect={2 / 1} />
            </div>
            <div className="chart__list-container">
              {/* FIXME zmienić na ostatnie CVEs */}
              <div className="chart__list-title">Latest Transactions</div>
              <Hometable />
            </div>
          </div>
        </div>
      </main>
    </>
  );
};

export default Dashboard;
