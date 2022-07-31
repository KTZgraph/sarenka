// PAGINACJA
// TODO https://github.com/mui/mui-x/issues/1907
import { DataGrid } from "@mui/x-data-grid";
import { useState } from "react";
import "./style.scss";

const CveDatatable = ({ data, actionColumns, dataColumns }) => {
  const [pageSize, setPageSize] = useState(10);

  const handlePageSizeChange = (params) => {
    setPageSize(params.pageSize);
  };

  return (
    <div className="cveDatatable">
      <DataGrid
        rows={data}
        // WARNING dodawanie danych do kolumny
        columns={dataColumns.concat(actionColumns)}
        pageSize={pageSize}
        // opcja elemntów na stronie -wybiera user
        rowsPerPageOptions={[10, 15, 20, 50, 100]}
        // zmiana ilości widocznych wierszy
        onPageSizeChange={handlePageSizeChange}
        // chckboxy z lewej
        checkboxSelection
        className="dataGrid"
      />
    </div>
  );
};

export default CveDatatable;
