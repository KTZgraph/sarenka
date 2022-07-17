import Datatable from "../../components/datatable/Datatable";
import Navbar from "../../components/navbar/Navbar";
import Sidebar from "../../components/sidebar/Sidebar";
import styles from "./List.module.scss";

const List = () => {
  return (
    <div className={`${styles.list} wrapper`}>
      <Sidebar />
      <div className={styles.listContainer}>
        <Navbar />
        <Datatable />
      </div>
    </div>
  );
};

export default List;
