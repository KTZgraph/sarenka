import { DataGrid, GridColDef, GridValueGetterParams } from "@mui/x-data-grid";
import styles from "./Datatable.module.scss";
import { userColumns } from "./DatatableColumns";
import { userRows } from "../../dummy_data/datatablesource";

// FIXME responsywność
const Datatable = () => {
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
        rows={userRows}
        // to co pokazujemy w datatable
        // columns={userColumns}
        // WARNING dodawanie danych do kolumny
        columns={userColumns.concat(actionColumn)}
        // paginacja
        pageSize={5}
        rowsPerPageOptions={[3]}
        checkboxSelection
        className={styles.dataGrid}
      />
    </div>
  );
};

export default Datatable;
