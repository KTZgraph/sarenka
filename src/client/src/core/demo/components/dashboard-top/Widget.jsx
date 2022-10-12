import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import styles from "./Widget.module.scss";

const Widget = ({ data }) => {
  return (
    <div className={styles.widget}>
      <div className={styles.left}>
        <div className={styles.title}>{data.title}</div>
        <div className={styles.counter}>{data.count}</div>
        <div className={styles.link}>{data.linkName}</div>
      </div>
      <div className={styles.right}>
        <div
          className={`${styles.percentage} ${
            data.percentage >= 0 ? styles.positive : styles.negative
          }`}
        >
          <KeyboardArrowUpIcon />
          {data.percentage} %
        </div>
        {data.icon}
      </div>
    </div>
  );
};
export default Widget;
