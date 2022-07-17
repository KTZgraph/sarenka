import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import styles from "./Home.module.scss";
import Widget from "../../components/widget/Widget";

const Home = () => {
  return (
    <div className={`${styles.home} wrapper`}>
      <Sidebar />
      <div className={`${styles.homeContainer}`}>
        <Navbar />
        <div className={styles.widgets}>
          <Widget type="user" />
          <Widget type="order" />
          <Widget type="earnings" />
          <Widget type="balance" />
        </div>
      </div>
    </div>
  );
};

export default Home;
