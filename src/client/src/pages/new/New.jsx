import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import styles from "./New.module.scss";

const New = () => {
  return (
    <div className={styles.new}>
      <Sidebar />
      <div className={styles.newCotainer}>
        <Navbar />
        NEW
      </div>
    </div>
  );
};

export default New;
