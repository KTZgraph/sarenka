import { DataGrid, GridColDef, GridValueGetterParams } from "@mui/x-data-grid";
import styles from "./VulnsDatatable.module.scss";
import { userColumns } from "./VulnsDatatableDatatableColumns";
import { dummyCves } from "./dummy_cves";

// FIXME responsywność
const VulnsDatatable = () => {
  const actionColumn = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: () => {
        return (
          <div className={styles.cellAction}>
            <div className={styles.viewButton}>View</div>
            <div className={styles.deleteButton}>Delete</div>
          </div>
        );
      },
    },
  ];

  return (
    <div className={styles.datatable}>
      <DataGrid
        //   rows - dane
        rows={dummyCves}
        // to co pokazujemy w datatable
        // columns={userColumns}
        // WARNING dodawanie danych do kolumny
        // columns={userColumns.concat(actionColumn)}
        columns={userColumns}
        // paginacja
        pageSize={10}
        rowsPerPageOptions={[3]}
        checkboxSelection
        className={styles.dataGrid}
      />
    </div>
  );
};

export default VulnsDatatable;
