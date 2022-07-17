import { CircularProgressbar } from "react-circular-progressbar";
// bez styli dla progessbaru ykres jest pusty
import "react-circular-progressbar/dist/styles.css";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpOutlinedIcon from "@mui/icons-material/KeyboardArrowUpOutlined";
import styles from "./Featured.module.scss";

const Featured = () => {
  return (
    <div className={`${styles.featured} wrapper`}>
      <div className={styles.top}>
        <h1 className={styles.title}>Total Revenue</h1>
        {/* zmiana wilekości czcionki  */}
        <MoreVertIcon fontSize="large" />
      </div>
      <div className={styles.bottom}>
        <div className={styles.featuredChart}>
          {/* progress bar */}
          <CircularProgressbar value={70} text={"70%"} strokeWidth={5} />
        </div>
        <p className={styles.title}>Total sales made today</p>
        <p className={styles.amount}>$420</p>
        <p className={styles.description}>
          Previous transactions processing. Last payments may not be included.
        </p>
        <div className={styles.summary}>
          <div className={styles.item}>
            <div className={styles.itemTitle}>Target</div>
            <div className={`${styles.itemResult} ${styles.negative}`}>
              <KeyboardArrowDownIcon fontSize="small" />
              <div className={styles.resultAmount}>$12.4k</div>
            </div>
          </div>
          <div className={styles.item}>
            <div className={styles.itemTitle}>Last Week</div>
            <div className={`${styles.itemResult} ${styles.positive}`}>
              <KeyboardArrowUpOutlinedIcon fontSize="small" />
              <div className={styles.resultAmount}>$12.4k</div>
            </div>
          </div>
          <div className={styles.item}>
            <div className={styles.itemTitle}>Last Month</div>
            <div className={`${styles.itemResult} ${styles.positive}`}>
              <KeyboardArrowUpOutlinedIcon fontSize="small" />
              <div className={styles.resultAmount}>$12.4k</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Featured;
