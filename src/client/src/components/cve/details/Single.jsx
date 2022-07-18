import AssignedUser from "../actions/assigned/AssignedUser";
import AttachTo from "../actions/attach/AttachTo";
import Comment from "../form/Comment";
import V2 from "../base_metric/cvss_v2/Single";
import V3 from "../base_metric/cvss_v3/Single";
import ReferenceList from "../references/list/List"; //używam aliasu
import CpeList from "../cpe/cpe_2_3/list/List"; //używam aliasu
import styles from "./Single.module.scss";

import { dummyCve as data } from "./dummy_cve";

const Single = () => {
  return (
    <div className={styles.details}>
      <div className={styles.detailsContainer}>
        <h1 className={styles.title}>{data.cwe_code}</h1>
        <div className={styles.status}>
          {/* FIXME dane o statusie np Verified */}
          verified na sztywno
        </div>
        <AssignedUser />
        <AttachTo />
        <div className={styles.dateInfo}>
          <span>Released:</span> {data.published}
        </div>
        <div className={styles.dateInfo}>
          <span>Modified:</span> {data.modified}
        </div>
        <div className={styles.description}>
          <span>Description:</span> {data.description}
        </div>
        {/* TODO plugins */}
        <V2 item={data.base_metric_v2} />
        <V3 item={data.base_metric_v3} />
        <div className={styles.riskLevel}>
          <span>Risk Level:</span> Jakies obliczneia?
        </div>
        <div className={styles.references}>
          <ReferenceList dataList={data.references_list} />
        </div>

        <div className={styles.affected}>
          <p>
            <span>Affected software:</span>jakieś software
          </p>
        </div>
        <div className={styles.cpe}>
          <CpeList dataList={data.cpe_list} />
        </div>
        <div className={styles.cweInfo}>
          <p>
            <span>CWE:</span>
            {data.cwe_code}
          </p>
        </div>

        {/* <div>{JSON.stringify(dummyCve)}</div> */}

        {/* formularz na samym dole */}
        <div className={styles.actions}>
          <Comment />
        </div>
      </div>
    </div>
  );
};

export default Single;
