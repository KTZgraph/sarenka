import styles from "./Featured.module.scss";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import { CircularProgress } from "react-circular-progressbar";

const Featured = () => {
  return (
    <div className={styles.featured}>
      <div className={styles.top}>
        <h1 className={styles.title}>Total Revenue</h1>
        {/* zmiana wilekości czcionki  */}
        <MoreVertIcon fontSize="large" />
      </div>
      <div className={styles.bottom}>
        <div className={styles.featuredChart}>{/* progress bar */}</div>
      </div>
    </div>
  );
};

export default Featured;
