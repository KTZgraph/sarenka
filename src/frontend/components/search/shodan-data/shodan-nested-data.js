import ShodanDNS from "./shodan-dns";
import ShodanShodan from "./shodan-shodan";
import classes from "./shodan-nested-data.module.css";
import ShodanLocation from "./shodan-location";
import ShodanHTTP from "./shodan-http";

function ShodanNestedData(props) {
  const data = JSON.parse(props.data);

  return (
    <div className={classes.nestedData}>
      {data.hash && (
        <p>
          <span>hash</span>
          {data.hash}
        </p>
      )}
      {data.timestamp && (
        <p>
          <span>timestamp</span>
          {data.timestamp}
        </p>
      )}
      {data.isp && (
        <p>
          <span>isp</span>
          {data.isp}
        </p>
      )}
      {data.transport && (
        <p>
          <span>transport</span>
          {data.transport}
        </p>
      )}
      {data.data && (
        <p>
          <span>data</span>
          {data.data}
        </p>
      )}
      {data.asn && (
        <p>
          <span>asn</span>
          {data.asn}
        </p>
      )}
      {data.port && (
        <p>
          <span>port</span>
          {data.port}
        </p>
      )}
      {data.hostnames && (
        <p>
          <span>hostnames</span>
          {data.hostnames}
        </p>
      )}

      {/* niezagnieżdozne */}
      {data.ip && (
        <p>
          <span>ip</span>
          {data.ip}
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
      {data.os && (
        <p>
          <span>os</span>
          {data.os}
        </p>
      )}

      {/*  niezagnieżdzoę niżej*/}
      {data.opts && (
        <p>
          <span>opts</span>
          {data.opts}
        </p>
      )}
      {data.ip_str && (
        <p>
          <span>ip_str</span>
          {data.ip_str}
        </p>
      )}

      {data.location && <ShodanLocation data={JSON.stringify(data.location)} />}
      {data.dns && <ShodanDNS data={JSON.stringify(data.dns)} />}
      {data._shodan && <ShodanShodan data={JSON.stringify(data._shodan)} />}
      {data.http && <ShodanHTTP data={JSON.stringify(data.http)} />}
    </div>
  );
}

export default ShodanNestedData;
