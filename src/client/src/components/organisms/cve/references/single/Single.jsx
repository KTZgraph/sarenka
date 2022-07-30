import styles from "./Single.module.scss";

const Single = ({ item }) => {
  return (
    <div className={styles.single}>
      <div className={styles.singleContainer}>
        <p>
          <span>name:</span>
          {item.name}
        </p>
        <p>
          <span>url:</span>
          {item.url}
        </p>
        <p>
          <span>refsource:</span>
          {item.refsource}
        </p>
        <p>
          <span>tags:</span>
          {item.tags}
        </p>
      </div>
    </div>
  );
};

export default Single;
