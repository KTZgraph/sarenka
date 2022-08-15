import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import DefaultSingle from "../../../components/templates/default/DefaultSingle";
import Loading from "../../../components/templates/default/Loading";
import Information from "../../../components/molecules/information";
import styles from "./Single.module.scss";

const Single = () => {
  const [cve, setCve] = useState(null);
  const { cveId } = useParams();

  // pobieranie jednego
  const getCveById = async (id) => {
    try {
      const res = await fetch(`/api/vulnerabilities/cves/${id}`);
      const json = await res.json();
      setCve(json);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    // WARNING https://devtrium.com/posts/async-functions-useeffect

    getCveById(cveId);
  }, [cveId]);

  if (cve) {
    return <Loading />;
  }

  return (
    <DefaultSingle
      subtitle={cve ? cve.code : cveId}
      actionType="update"
      actionLink={`/vulns/cves/${cveId}/update`}
    >
      <div className={styles.detailsContainer}>
        <div className={styles.detailsCard}>
          {/* <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} />
          <Information className={styles.detail} name="code" info={cve.code} /> */}
        </div>
      </div>
    </DefaultSingle>
  );
};

export default Single;
