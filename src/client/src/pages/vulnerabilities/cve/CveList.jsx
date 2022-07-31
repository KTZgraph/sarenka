import { useEffect, useState } from "react";
import Default from "../../../components/templates/default/Default";
import CveDatatable from "../../../components/organisms/cve_datatable/CveDatatable";
import Sidebar from "../../../components/organisms/sidebar/Sidebar";
import Navbar from "../../../components/organisms/navbar/Navbar";
import styles from "./CveList.module.scss";
const CveList = () => {
  const [cves, setCves] = useState(null);

  // pobieranie listy cve
  useEffect(() => {
    fetch("/api/vulnerabilities/cves")
      .then((res) => res.json())
      .then((json) => setCves(json.cves))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div className={styles.list}>
      <Sidebar />
      <div className={styles.listContainer}>
        <Navbar />
        <CveDatatable />
      </div>
    </div>
  );
};

export default CveList;
