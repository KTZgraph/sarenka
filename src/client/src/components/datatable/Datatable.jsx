import { DataGrid, GridColDef, GridValueGetterParams } from "@mui/x-data-grid";
import styles from "./Datatable.module.scss";
import { userColumns } from "./DatatableColumns";
import { userRows } from "../../dummy_data/datatablesource";

// FIXME responsywność
const Datatable = () => {
  return (
    <div className={styles.datatable}>
      <DataGrid
        //   rows - dane
        rows={userRows}
        // to co pokazujemy w datatable
        columns={userColumns}
        // paginacja
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
        className={styles.dataGrid}
      />
    </div>
  );
};

export default Datatable;
