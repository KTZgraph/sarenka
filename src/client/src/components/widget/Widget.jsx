import styles from "./Widget.module.scss";

const Widget = () => {
  return (
    <div className={styles.widget}>
      <div className={styles.left}>left</div>
      <div className={styles.right}>right</div>
    </div>
  );
};

export default Widget;
