// PAGINACJA
// TODO https://github.com/mui/mui-x/issues/1907
import { DataGrid } from "@mui/x-data-grid";
import { useState } from "react";
import styles from "./CveDatatable.module.scss";

const CveDatatable = ({ data, actionColumns, dataColumns }) => {
  const [pageSize, setPageSize] = useState(10);

  const handlePageSizeChange = (params) => {
    setPageSize(params.pageSize);
  };

  return (
    <div className={styles.datatable}>
      <DataGrid
        rows={data}
        // WARNING dodawanie danych do kolumny
        columns={dataColumns.concat(actionColumns)}
        pageSize={pageSize}
        // opcja elemntów na stronie -wybiera user
        rowsPerPageOptions={[10, 15, 20, 50, 100]}
        // zmiana ilości widocznych wierszy
        onPageSizeChange={handlePageSizeChange}
        className={styles.dataGrid}
      />
    </div>
  );
};

export default CveDatatable;
