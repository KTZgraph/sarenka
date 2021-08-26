import useFetch from "../useFetch";
import CWEList from "../components/CWEList";

const CWEScreen = (props) => {
  const {data:cweList, isPending, error} = useFetch('http://127.0.0.1:8000/api/vulns/cwe-list/');

  return (
    <div className='cwe-screen'>
      {error && <div className="error-message">{error}</div>}
      {isPending && <div className="loading">Loading...</div>}
      {cweList && <CWEList cweList={cweList}/>}
    </div>
  );
}

export default CWEScreen;