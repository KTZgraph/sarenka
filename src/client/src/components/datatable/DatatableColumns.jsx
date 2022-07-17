import styles from "./Datatable.module.scss";
// schemat dla tabeli danych, zeby tego nie trzymać w client\src\components\datatable\Datatable.jsx
export const userColumns = [
  { field: "id", headerName: "ID", width: 70 },
  {
    field: "user",
    headerName: "User",
    width: 230,
    renderCell: (params) => {
      return (
        <div className={styles.cellWithImg}>
          <img className={styles.cellImg} src={params.row.img} alt="avatar" />
          {params.row.username}
        </div>
      );
    },
  },
  { field: "email", headerName: "Email", width: 230 },
  { field: "age", headerName: "Age", width: 100 }, //mniejsza bo tylko numer
  {
    field: "status",
    headerName: "Status",
    width: 160,
    // zamiast valueGetter można użyć renderCell:
    // valueGetter: (params) =>
    // `${params.row.firstName || ""} ${params.row.lastName || ""}`,
    //   WARNING uważać na składnie - jak sie zrobi błąd to dane sie nie wyświetlają
    renderCell: (params) => {
      // FIXME style
      return (
        <div
          className={
            params.row.status === "active"
              ? `${styles.cellWithStatus} ${styles.active}`
              : params.row.status === "passive"
              ? `${styles.cellWithStatus} ${styles.passive}`
              : `${styles.cellWithStatus} ${styles.pending}`
          }
        >
          {params.row.status}
        </div>
      );
    },
  },
];

// className={
//   row.status === "Pending"
//     ? `${styles.status} ${styles.Pending}`
//     : `${styles.status} ${styles.Approved} `
// }
