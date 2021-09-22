import useFetch from "../useFetch";
import HttpComponentList from "../components/HttpComponentList";
import SpinnerHeart from "../components/SpinnerHeart";

const ShodanQueriesScreen = () => {
  const { data, isPending, error } = useFetch('api/engines/shodan-queries/');

  return (
    <div className='wrap'>
      {error && <div className="error-message">{error}</div>}
      ShodanQueriesScreen
      {isPending && <SpinnerHeart />}
      {data && <HttpComponentList dataList={data} />}

    </div>
  );
}

export default ShodanQueriesScreen;