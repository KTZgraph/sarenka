import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import styles from "./VulnsSingle.module.scss";
import CveData from "../../components/cve_details/CveDetails";
import CveForm from "../../components/cve_form/CveForm";

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
