import styles from "./List.module.scss";
import Single from "../single/Single";

const List = ({ dataList }) => {
  return (
    <div className={styles.list}>
      <div className={styles.listContainer}>
        {/* FIXME poiterować po liście */}

        {dataList && <Single item={dataList[0]} />}
        {/* <Single reference={data[0]} /> */}
      </div>
    </div>
  );
};

export default List;
