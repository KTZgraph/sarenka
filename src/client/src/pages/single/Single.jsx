import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import styles from "./Single.module.scss";

const Single = () => {
  return (
    <div className={styles.single}>
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
              <div className={styles.details}>
                <h1 className={styles.itemTitle}>Jane Doe</h1>
                <div className={styles.detailItem}>
                  <span className={styles.itemKey}>Email:</span>
                  <span className={styles.itemValue}>janedoe@gmail.com</span>
                </div>
                <div className={styles.detailItem}>
                  <span className={styles.itemKey}>Phone:</span>
                  <span className={styles.itemValue}>+1 2345 67 89</span>
                </div>
                <div className={styles.detailItem}>
                  <span className={styles.itemKey}>Adress:</span>
                  <span className={styles.itemValue}>
                    Teststreat 1 Testcity
                  </span>
                </div>
                <div className={styles.detailItem}>
                  <span className={styles.itemKey}>Country:</span>
                  <span className={styles.itemValue}>USA</span>
                </div>
              </div>
            </div>
          </div>
          <div className={styles.right}></div>
        </div>
        <div className={styles.bottom}></div>
      </div>
    </div>
  );
};

export default Single;
