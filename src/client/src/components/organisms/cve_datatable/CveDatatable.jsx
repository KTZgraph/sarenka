import { DataGrid } from "@mui/x-data-grid";
import styles from "./CveDatatable.module.scss";
import { cveDatatableColumns } from "./CveDatatableColumns";
import { dummyCves } from "./dummy_cves";
import { Link } from "react-router-dom";

// FIXME responsywność
const CveDatatable = () => {
  const actionColumn = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: () => {
        return (
          <div className={styles.cellAction}>
            <Link to="/vulns/123">
              <div className={styles.viewButton}>View</div>
            </Link>
            <Link to="/vulns/123">
              <div className={styles.deleteButton}>Delete</div>
            </Link>
          </div>
        );
      },
    },
  ];

  return (
    <div className={styles.datatable}>
      <DataGrid
        rows={dummyCves}
        // WARNING dodawanie danych do kolumny
        columns={cveDatatableColumns.concat(actionColumn)}
        pageSize={10}
        rowsPerPageOptions={[3]}
        checkboxSelection
        className={styles.dataGrid}
      />
    </div>
  );
};

export default CveDatatable;
