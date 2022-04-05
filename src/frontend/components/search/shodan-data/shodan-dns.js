function ShodanDNS(props) {
  const data = JSON.parse(props.data);
  return (
    <div>
      <h3>dns</h3>
      {data.resolver_hostname && (
        <p>
          <span>resolver_hostname</span>
          {data.resolver_hostname}
        </p>
      )}
      {data.recursive && (
        <p>
          <span>recursive</span>
          {data.recursive}
        </p>
      )}
      {data.resolver_id && (
        <p>
          <span>resolver_id</span>
          {data.resolver_id}
        </p>
      )}
      {data.software && (
        <p>
          <span>software</span>
          {data.software}
        </p>
      )}
    </div>
  );
}

export default ShodanDNS;
