import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import styles from "./Single.module.scss";

const Single = () => {
  return (
    <div className={`${styles.single} wrapper`}>
      <Sidebar />
      <div className={styles.singleContainer}>
        <Navbar />
        <div className={styles.top}>
          <div className={styles.left}>
            {/* position absolut przycisku do edycji */}
            <div className={styles.editButton}>Edit</div>
            <h1 className={styles.title}>Infromation</h1>
            <div className={styles.item}>
              <img
                src="https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260"
                alt=""
                className={styles.itemImg}
              />
            </div>
            <div className={styles.details}>details</div>
          </div>
          <div className={styles.right}></div>
        </div>
        <div className={styles.bottom}></div>
      </div>
    </div>
  );
};

export default Single;
