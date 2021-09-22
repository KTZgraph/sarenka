import { Link } from "react-router-dom";

const HttpComponentList = ({ dataList }) => {
  return (
    <div className="cwe-list">
      <h1>HttpComponentList</h1>
      {dataList.map(query => (
        <div className="cwe-preview">
          <h2>{query.name}</h2>
          <p>{query.query}</p>
          <Link to={query.url}>{query.url}</Link>
          <br />
        </div>
      ))}

    </div>
  )
}

export default HttpComponentList;