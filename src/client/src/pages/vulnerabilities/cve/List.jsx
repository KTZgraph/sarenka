import { useEffect, useState } from "react";

const List = () => {
  const [cves, setCves] = useState(null);

  // pobieranie listy cve
  useEffect(() => {
    fetch("/api/vulnerabilities/cves")
      .then((res) => res.json())
      .then((json) => setCves(json.cves))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <h1 className="title">CVE list pobieranie</h1>
      <div>{cves?.length > 0 ? <p>{JSON.stringify(cves)}</p> : <p>NIe</p>}</div>
    </div>
  );
};

export default List;
