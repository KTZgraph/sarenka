import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import Widget from "../../components/widget/Widget";
import Featured from "../../components/featured/Featured";
import Chart from "../../components/chart/Chart";

import styles from "./Home.module.scss";
import Table from "../../components/datatable/Datatable";
const Home = () => {
  return (
    <div className={`${styles.home} wrapper`}>
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
          <Chart />
        </div>
        <div className={styles.listContainer}>
          {/* FIXME zmienić na ostatnie CVEs */}
          <div className={styles.listTitle}>Latest Transactions</div>
          <Table />
        </div>
      </div>
    </div>
  );
};

export default Home;
