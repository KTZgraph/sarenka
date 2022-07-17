import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import styles from "./Hometable.module.scss";

const rows = [
  {
    id: 1143155,
    product: "Acer Nitro 5",
    img: "https://m.media-amazon.com/images/I/81bc8mA3nKL._AC_UY327_FMwebp_QL65_.jpg",
    customer: "John Smith",
    date: "1 March",
    amount: 785,
    method: "Cash on Delivery",
    status: "Approved",
  },
  {
    id: 2235235,
    product: "Playstation 5",
    img: "https://m.media-amazon.com/images/I/31JaiPXYI8L._AC_UY327_FMwebp_QL65_.jpg",
    customer: "Michael Doe",
    date: "1 March",
    amount: 900,
    method: "Online Payment",
    status: "Pending",
  },
  {
    id: 2342353,
    product: "Redragon S101",
    img: "https://m.media-amazon.com/images/I/71kr3WAj1FL._AC_UY327_FMwebp_QL65_.jpg",
    customer: "John Smith",
    date: "1 March",
    amount: 35,
    method: "Cash on Delivery",
    status: "Pending",
  },
  {
    id: 2357741,
    product: "Razer Blade 15",
    img: "https://m.media-amazon.com/images/I/71wF7YDIQkL._AC_UY327_FMwebp_QL65_.jpg",
    customer: "Jane Smith",
    date: "1 March",
    amount: 920,
    method: "Online",
    status: "Approved",
  },
  {
    id: 2342355,
    product: "ASUS ROG Strix",
    img: "https://m.media-amazon.com/images/I/81hH5vK-MCL._AC_UY327_FMwebp_QL65_.jpg",
    customer: "Harold Carol",
    date: "1 March",
    amount: 2000,
    method: "Online",
    status: "Pending",
  },
];
// FIXME zmienić na czysta tablekę HTMl https://www.youtube.com/watch?v=vIxGDq1SPZQ
const Datatable = () => {
  return (
    <TableContainer component={Paper} className={styles.hometable}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            {/* moje dane do tabelki zmoją nazwą klasy */}
            <TableCell className={styles.tableCell}>Tracking ID</TableCell>
            <TableCell className={styles.tableCell}>Product</TableCell>
            <TableCell className={styles.tableCell}>Customer</TableCell>
            <TableCell className={styles.tableCell}>Date</TableCell>
            <TableCell className={styles.tableCell}>Amount</TableCell>
            <TableCell className={styles.tableCell}>Payment Method</TableCell>
            <TableCell className={styles.tableCell}>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              // unikalne id tego co standardowo rect wymaga
              key={row.id}
            >
              <TableCell className={styles.tableCell}>{row.id}</TableCell>
              <TableCell className={styles.tableCell}>
                {/* obrazek produktu */}
                <div className={styles.cellWrapper}>
                  <img src={row.img} alt="" className={styles.cellImg} />
                  {row.product}
                </div>
              </TableCell>
              <TableCell className={styles.tableCell}>{row.customer}</TableCell>
              <TableCell className={styles.tableCell}>{row.date}</TableCell>
              <TableCell className={styles.tableCell}>{row.amount}</TableCell>
              <TableCell className={styles.tableCell}>{row.method}</TableCell>
              <TableCell className={styles.tableCell}>
                {/* <span className={`${styles.status} ${row.status}`}> */}
                <span
                  className={
                    row.status === "Pending"
                      ? `${styles.status} ${styles.Pending}`
                      : `${styles.status} ${styles.Approved} `
                  }
                >
                  {row.status}
                </span>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default Datatable;
