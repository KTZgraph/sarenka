import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import Chart from "../../components/chart/Chart";
import Hometable from "../../components/hometable/Hometable";
import styles from "./VulnsSingle.module.scss";

// FIXME logo w navbarze znika tutaj
const Single = () => {
  return (
    <div className={styles.single}>
      <Sidebar />
      <div className={styles.singleContainer}>
        <Navbar />
        VULNS SIGLE
      </div>
    </div>
  );
};

export default Single;
