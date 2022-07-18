// FIXME wybrać pola, dodac responsywnosć
import styles from "./VulnsDatatable.module.scss";
// schemat dla tabeli danych, zeby tego nie trzymać w client\src\components\datatable\Datatable.jsx

export const userColumns = [
  { field: "code", headerName: "ID", width: 120 },
  { field: "cwe_code", headerName: "CWE", width: 100 },
  // { field: "description", headerName: "Description", width: 400 },

  // { field: "assigner", headerName: "Assigner", width: 150 },
  // { field: "data_format", headerName: "Data Format", width: 150 },
  // { field: "data_format", headerName: "Data Format", width: 150 },
  // field: "base_metric_v2.cvss_v2.base_score",
  {
    //bgc zależnie od wartości
    field: "cvss_v3",
    headerName: "CVSSV3",
    width: 100,
    renderCell: (params) => {
      // const keys = Object.keys(params.row);
      return <p>{params.row.base_metric_v3.cvss_v3.base_score || ""}</p>;
    },
  },
  {
    //bgc zależnie od wartości
    field: "cvss_v2",
    headerName: "CVSSV2",
    width: 100,
    renderCell: (params) => {
      return <p>{params.row.base_metric_v2.cvss_v2.base_score || ""}</p>;
    },
  },
  {
    //bgc zależnie od wartości
    field: "exploitability_score",
    headerName: "exploitability_score",
    width: 230,
    renderCell: (params) => {
      return <p>{params.row.base_metric_v3.exploitability_score || ""}</p>;
    },
  },

  {
    field: "vector",
    headerName: "Vector",
    width: 400,
    //kolor tekstu zależnie od wartości
    renderCell: (params) => {
      return <p>{params.row.base_metric_v3.cvss_v3.vector || ""}</p>;
    },
  },

  { field: "published", headerName: "Published", width: 150 },
  { field: "modified", headerName: "Modified", width: 150 },
  // { field: "version", headerName: "Version", width: 150 },
];
