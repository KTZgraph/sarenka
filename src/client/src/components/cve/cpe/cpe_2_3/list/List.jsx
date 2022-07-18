import styles from "./List.module.scss";
import Single from "../single/Single";

const List = ({ dataList }) => {
  return (
    <div className={styles.list}>
      <div className={styles.listContainer}></div>
      {dataList && <Single item={dataList[0]} />}
    </div>
  );
};

export default List;
