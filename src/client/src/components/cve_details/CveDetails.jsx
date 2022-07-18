import styles from "./CveData.module.scss";
import { dummyCve } from "./dummy_cve";

const CveData = () => {
  return (
    <div className={styles.cveDetails}>
      <h1 className={styles.title}>Information</h1>
      <div>{JSON.stringify(dummyCve)}</div>
    </div>
  );
};

export default CveData;
