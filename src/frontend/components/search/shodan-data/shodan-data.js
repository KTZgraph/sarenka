import ShodanNestedData from "./shodan-nested-data";
import classes from "./shodan-data.module.css";

function ShodanData(props) {
  const data = JSON.parse(props.data);

  return (
    <div className={classes.data}>
      {data.ip && (
        <p>
          <span>ip</span>
          {data.ip}
        </p>
      )}
      {data.ip_str && (
        <p>
          <span>ip_str</span> {data.ip_str}
        </p>
      )}
      {data.city && (
        <p>
          <span>city</span>
          {data.city}
        </p>
      )}
      {data.region_code && (
        <p>
          <span>region_code</span>
          {data.region_code}
        </p>
      )}
      {data.os && (
        <p>
          <span>os</span>
          {data.os}
        </p>
      )}
      {data.tags && (
        <p>
          <span>tags</span>
          {data.tags}
        </p>
      )}
      {data.isp && (
        <p>
          <span>isp</span>
          {data.isp}
        </p>
      )}
      {data.area_code && (
        <p>
          <span>area_code</span>
          {data.area_code}
        </p>
      )}
      {data.longitude && (
        <p>
          <span>longitude</span>
          {data.longitude}
        </p>
      )}
      {data.last_update && (
        <p>
          <span>last_update</span>
          {data.last_update}
        </p>
      )}
      {data.ports && (
        <p>
          <span>ports</span>
          {data.ports}
        </p>
      )}
      {data.latitude && (
        <p>
          <span>latitude</span>
          {data.latitude}
        </p>
      )}
      {data.hostnames && (
        <p>
          <span>hostnames</span>
          {data.hostnames}
        </p>
      )}
      {data.country_code && (
        <p>
          <span>country_code</span>
          {data.country_code}
        </p>
      )}
      {data.country_name && (
        <p>
          <span>country_name</span>
          {data.country_name}
        </p>
      )}
      {data.domains && (
        <p>
          <span>domains</span>
          {data.domains}
        </p>
      )}
      {data.org && (
        <p>
          <span>org</span>
          {data.org}
        </p>
      )}
      {data.asn && (
        <p>
          <span>asn</span>
          {data.asn}
        </p>
      )}

      {/* na rozbudowę po oddaniu projektu */}
      {/* zwraca listę z danymi */}
      {/* {data.data.map((d, i) => console.log("d: ", d, "i: ", i) )} */}
      {/* {data.data.map((d, i) => <ShodanNestedData key={i} data={JSON.stringify(d)} />)} */}
    </div>
  );
}

export default ShodanData;
