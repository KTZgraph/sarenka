import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Spinner from "../../../components/atoms/spinner";
import DefaultSingle from "../../../components/templates/default/DefaultSingle";

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
    getCveById(cveId);
  }, [cveId]);

  return (
    <DefaultSingle
      subtitle={cve ? cve.code : cveId}
      actionType="update"
      actionLink={`/vulns/cves/${cveId}/update`}
    >
      {cve ? (
        <div className="card">
          <div className="info">
            <span className="name">Key: </span> <p className="value">Value</p>
          </div>
          <div>{JSON.stringify(cve)}</div>
        </div>
      ) : (
        <Spinner />
      )}
    </DefaultSingle>
  );
};

export default Single;
