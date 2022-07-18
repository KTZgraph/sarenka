import React from "react";
import VulnsDatatable from "../../components/vulns_datatable/VulnsDatatable";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";

import styles from "./VulnList.module.scss";
const VulnList = () => {
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

export default VulnList;
