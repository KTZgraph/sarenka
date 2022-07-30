import styles from "../single/Single";

const Single = ({ item }) => {
  return (
    <div className={styles.single}>
      <div className={styles.signleContainer}>
        <p>
          <span>uri:</span>
          {item.uri}
        </p>
        <p>
          <span>vulnerable:</span>
          {item.is_vulnerable ? "TRUE" : "FALSE"}
        </p>
      </div>
    </div>
  );
};

export default Single;
