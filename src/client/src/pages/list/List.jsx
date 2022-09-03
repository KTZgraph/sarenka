import Datatable from "../../components/organisms/datatable/Datatable";
import Navbar from "../../components/organisms/navbar/Navbar";
import Sidebar from "../../components/organisms/sidebar/Sidebar";
import styles from "./List.module.scss";

const List = () => {
  return (
    <div className={styles.list}>
      <Sidebar />
      <div className={styles.listContainer}>
        <Navbar />
        <Datatable />
      </div>
    </div>
  );
};

export default List;
