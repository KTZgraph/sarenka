import Sidebar from "../../../components/sidebar/Sidebar";
import Navbar from "../../../components/navbar/Navbar";
import CveData from "../../../components/cve/details/Single";
import styles from "./Single.module.scss";

// FIXME logo w navbarze znika tutaj
const Single = () => {
  return (
    <div className={styles.single}>
      <Sidebar />
      <div className={styles.singleContainer}>
        <Navbar />
        <div className={styles.top}>
          <CveData />
        </div>
        <div className={styles.bottom}></div>
      </div>
    </div>
  );
};

export default Single;
