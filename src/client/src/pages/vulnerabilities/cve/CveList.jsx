import { useEffect, useState } from "react";
import Default from "../../../components/templates/default/Default";
import CveDatatable from "../../../components/organisms/cve_datatable/CveDatatable";
import Sidebar from "../../../components/organisms/sidebar/Sidebar";
import Navbar from "../../../components/organisms/navbar/Navbar";
import styles from "./CveList.module.scss";
import { Link } from "react-router-dom";
import { datatableColumns } from "./DatatableColumns";

const CveList = () => {
  const [cves, setCves] = useState(null);

  // pobieranie listy cve
  useEffect(() => {
    fetch("/api/vulnerabilities/cves")
      .then((res) => res.json())
      .then((json) => setCves(json.cves))
      .catch((error) => console.log(error));
  }, []);

  // dodatkowe kolumny do tabelki
  const actionColumns = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: (params) => {
        return (
          <div className={styles.cellAction}>
            <Link to={`/vulns/cves/${params.row.id}`}>
              <div className={styles.viewButton}>View</div>
            </Link>
            <Link to={`/vulns/cves/${params.row.id}`}>
              <div className={styles.deleteButton}>Delete</div>
            </Link>
          </div>
        );
      },
    },
  ];

  return (
    <div className={styles.list}>
      <Sidebar />
      <div className={styles.listContainer}>
        <Navbar />
        {cves?.length > 0 ? (
          <CveDatatable
            data={cves}
            actionColumns={actionColumns}
            dataColumns={datatableColumns}
          />
        ) : (
          <p>Nie</p>
        )}
      </div>
    </div>
  );
};

export default CveList;
