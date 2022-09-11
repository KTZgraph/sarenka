import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
// import Loading from '../../../components/templates/default/Loading';
import LoadingTemplate from '../../components/templates/LoadingTemplate';
import Information from '../../components/molecules/information';
// import { VulnerabilityWrapper } from "../../../lib/vulnerability_wrapper";
import styles from './Single.module.scss';

const Single = () => {
  const [cve, setCve] = useState(null);
  const { cveId } = useParams();

  // pobieranie jednego
  const getCveById = async (id) => {
    try {
      const res = await fetch(`/api/vulnerabilities/cves/${id}`);
      const json = await res.json();
      console.log(json);
      // const parsedData = new VulnerabilityWrapper(json).getData();
      console.log('parsedData: ', json);

      // setCve(parsedData);
      setCve(json);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    // WARNING https://devtrium.com/posts/async-functions-useeffect

    getCveById(cveId);
  }, [cveId]);

  if (!cve) {
    return <LoadingTemplate />;
  }

  return (
    <div className={styles.detailsContainer}>
      <div className={styles.detailsCard}>
        <Information
          className={styles.detail}
          name="code"
          info={cve.key}
        />
        <Information
          className={styles.detail}
          name="cwe"
          info={cve.cwe}
        />
        <Information
          className={styles.detail}
          name="assigner"
          info={cve.assigner}
        />
        <Information
          className={styles.detail}
          name="baseScoreV2"
          info={cve.baseScoreV2}
        />
        <Information
          className={styles.detail}
          name="vectorV2"
          info={cve.vectorV2}
        />
        <Information
          className={styles.detail}
          name="versionV2"
          info={cve.versionV2}
        />
        <Information
          className={styles.detail}
          name="baseScoreV3"
          info={cve.baseScoreV3}
        />
        <Information
          className={styles.detail}
          name="vectorV3"
          info={cve.vectorV3}
        />
        <Information
          className={styles.detail}
          name="versionV3"
          info={cve.versionV3}
        />
        <Information
          className={styles.detail}
          name="dataFormat"
          info={cve.dataFormat}
        />
        <Information
          className={styles.detail}
          name="description"
          info={cve.description}
        />
        <Information
          className={styles.detail}
          name="modified"
          info={cve.modified}
        />
        <Information
          className={styles.detail}
          name="published"
          info={cve.published}
        />
        {/* TODO lista referencji */}
        {/* <Information
            className={styles.detail}
            name="references"
            info={cve.references}
          /> */}
        <Information
          className={styles.detail}
          name="version"
          info={cve.version}
        />
      </div>
    </div>
  );
};

export default Single;
