import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Spinner from "../../../components/atoms/spinner";
import DefaultSingle from "../../../components/templates/default/DefaultSingle";

import { cveList } from "../../../server_mock/cve_list";

const Single = () => {
  const [cve, setCve] = useState(null);
  const { cveId } = useParams();

  // pobieranie listy cve
  useEffect(() => {
    fetch(`/api/vulnerabilities/cves/${cveId}`)
      .then((res) => res.json())
      .then((json) => setCve(json.cves))
      .catch((error) => console.log(error));
  }, [cve]);

  const data = cveList[0];
  return (
    <DefaultSingle
      subtitle={data.code}
      actionType="update"
      actionLink={`/vulns/cves/${cveId}/update`}
    >
      <div>{data ? data.published : <Spinner />}</div>
    </DefaultSingle>
  );
};

export default Single;
