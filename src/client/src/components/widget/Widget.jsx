import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import PersonOutlineIcon from "@mui/icons-material/PersonOutline";
import styles from "./Widget.module.scss";

const Widget = () => {
  return (
    <div className={styles.widget}>
      <div className={styles.left}>
        <div className={styles.title}>users</div>
        <div className={styles.counter}>21312</div>
        <div className={styles.link}>See all users</div>
      </div>
      <div className={styles.right}>
        <div className={`${styles.percentage} ${styles.negative}`}>
          <KeyboardArrowUpIcon />
          20 %
        </div>
        <PersonOutlineIcon className={styles.icon} />
      </div>
    </div>
  );
};

export default Widget;
