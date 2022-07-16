import styles from "./Home.module.scss";

const Home = () => {
  return (
    <div className={`${styles.home} wrapper`}>
      <div className={`${styles.homeContainer}`}>HOME</div>
    </div>
  );
};

export default Home;
