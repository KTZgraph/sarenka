function ShodanHTTP(props) {
  const data = JSON.parse(props.data);
  return (
    <div>
      <h3>HTTP</h3>
      {data.status && (
        <p>
          <span>status</span>
          {data.status}
        </p>
      )}
      {data.robots_hash && (
        <p>
          <span>robots_hash</span>
          {data.robots_hash}
        </p>
      )}
      {/* ponizej lista */}
      {/* {data.redirects && (<p><span>redirects</span>{data.redirects}</p>)} */}
      {data.securitytxt && (
        <p>
          <span>securitytxt</span>
          {data.securitytxt}
        </p>
      )}
      {data.title && (
        <p>
          <span>title</span>
          {data.title}
        </p>
      )}
      {data.sitemap_hash && (
        <p>
          <span>sitemap_hash</span>
          {data.sitemap_hash}
        </p>
      )}
      {data.html_hash && (
        <p>
          <span>html_hash</span>
          {data.html_hash}
        </p>
      )}
    </div>
  );
}

export default ShodanHTTP;
