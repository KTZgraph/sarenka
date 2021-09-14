import { Link } from "react-router-dom";

const CWEList = ({ cweList }) => {
  return (
    <div className="cwe-list">
      <h1>Common Weakness Enumeration List</h1>
      {cweList.map(cwe => (
        <div className="cwe-preview" key={cwe.id}>
          <Link to={`/cwe/${cwe.id}`}>
            <h2>{`CWE-${cwe.id}`}</h2>
            <p>{cwe.name}</p>
          </Link>
        </div>
      ))}
    </div>
  )
}

export default CWEList;