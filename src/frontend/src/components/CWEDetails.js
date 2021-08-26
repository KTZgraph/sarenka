import {useHistory, useParams} from 'react-router-dom';
import useFetch from "../useFetch";

const CWEDetails = () => {
  const {id} = useParams();
  const {data:cwe, error, isPending} = useFetch('http://127.0.0.1:8000/api/vulns/cwe/' + id);
  const history = useHistory();

  return (
    <div className="cwe-details">
      {isPending && <div>Loading...</div>}
      {error && <div>{error}</div>}
      {cwe && (
        <article>
          <h2 className="cwe-details__id">CWE-{cwe.id}</h2>
          <h3 className="cwe-details__name">{cwe.name}</h3>
          <p className="cwe-details__description">description: {cwe.description}</p>
          <p className="cwe-details__extended-description">extended_description: {cwe.extended_description}</p>
          <p className="cwe-details__abstraction">abstraction: {cwe.abstraction}</p>
          <p className="cwe-details__status">status: {cwe.status}</p>
          <p className="cwe-details__structure">structure: {cwe.structure}</p>
        </article>
      )}
    </div>
  );
}

export default CWEDetails;