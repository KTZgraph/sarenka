import styles from "./Single.module.scss";

const Single = ({ item }) => {
  return (
    <div className={styles.single}>
      <div className={styles.singleContainer}>
        <span className={styles.score}>{item.cvss_v2.base_score}</span>
        <span className={styles.vector}>{item.cvss_v2.vector}</span>
      </div>
    </div>
  );
};

export default Single;
