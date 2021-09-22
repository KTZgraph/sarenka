import useFetch from "../useFetch";
import CWEList from "../components/CWEList";
import SpinnerHeart from "../components/SpinnerHeart";
import Spinner from "../components/Spinner";
import SpinnerTwo from "../components/SpinnerTwo";
import SpinnerThree from "../components/SpinnerThree";

const CWEScreen = () => {
  const { data: cweList, isPending, error } = useFetch('/api/vulns/cwe-list/');

  return (
    <div className='cwe-screen'>
      {error && <div className="error-message">{error}</div>}
      {/* {isPending && <div className="loading">Loading...</div>} */}
      {isPending && <SpinnerHeart />}
      {isPending && <Spinner />}
      {isPending && <SpinnerTwo />}
      {isPending && <SpinnerThree />}
      {cweList && <CWEList cweList={cweList} />}
    </div>
  );
}

export default CWEScreen;