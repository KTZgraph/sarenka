import Sidebar from "../../../components/sidebar/Sidebar";
import Navbar from "../../../components/navbar/Navbar";
import CveData from "../../../components/cve/details/CveDetails";
import CveForm from "../../../components/cve/form/CveForm";
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
        <div className={styles.bottom}>
          <CveForm />
        </div>
      </div>
    </div>
  );
};

export default Single;
