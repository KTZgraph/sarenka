import Sidebar from "../../components/organisms/sidebar/Sidebar";
import Navbar from "../../components/organisms/navbar/Navbar";
import Widget from "../../components/widget/Widget";
import Featured from "../../components/featured/Featured";
import Chart from "../../components/chart/Chart";

import styles from "./Home.module.scss";
import Hometable from "../../components/hometable/Hometable";

const Home = () => {
  return (
    <div className={styles.home}>
      <Sidebar />
      <div className={`${styles.homeContainer}`}>
        <Navbar />
        <div className={styles.widgets}>
          <Widget type="user" />
          <Widget type="order" />
          <Widget type="earnings" />
          <Widget type="balance" />
        </div>
        <div className={styles.charts}>
          {/* wykresiki */}
          <Featured />
          <Chart chartTitle="Last 6 Months (Revenue)" chartAspect={2 / 1} />
        </div>
        <div className={styles.listContainer}>
          {/* FIXME zmienić na ostatnie CVEs */}
          <div className={styles.listTitle}>Latest Transactions</div>
          <Hometable />
        </div>
      </div>
    </div>
  );
};

export default Home;
