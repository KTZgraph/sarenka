import VulnsDatatable from "../../../components/organisms/vulns_datatable/VulnsDatatable";
import Sidebar from "../../../components/organisms/sidebar/Sidebar";
import Navbar from "../../../components/organisms/navbar/Navbar";

import styles from "./List.module.scss";
const List = () => {
  return (
    <div className={styles.list}>
      <Sidebar />
      <div className={styles.listContainer}>
        <Navbar />
        <VulnsDatatable />
      </div>
    </div>
  );
};

export default List;
