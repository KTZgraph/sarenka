// PAGINACJA
// TODO https://github.com/mui/mui-x/issues/1907
import { useState } from "react";
import { Link } from "react-router-dom";
import { DataGrid } from "@mui/x-data-grid";
import { datatableColumns } from "./columns";
import "./style.scss";

const CveDatatable = ({ data }) => {
  const [pageSize, setPageSize] = useState(10);

  const handlePageSizeChange = (params) => {
    setPageSize(params.pageSize);
  };
  const actionColumns = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: (params) => {
        return (
          <div className="cellAction">
            <Link to={`/vulns/cves/${params.row.id}`}>
              <div className="viewButton">View</div>
            </Link>
            <Link to={`/vulns/cves/${params.row.id}/delete`}>
              <div className="deleteButton">Delete</div>
            </Link>
          </div>
        );
      },
    },
  ];

  return (
    <div className="cveDatatable">
      <DataGrid
        rows={data}
        // WARNING dodawanie danych do kolumny
        columns={datatableColumns.concat(actionColumns)}
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
