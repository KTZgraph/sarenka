function ShodanShodan(props) {
  const data = JSON.stringify(props);
  return (
    <div>
      <h3>_shodan</h3>
      {data.crawler && (
        <p>
          <span>crawler</span>
          {data.crawler}
        </p>
      )}
      {data.options && (
        <p>
          <span>options</span>
          {data.options}
        </p>
      )}
      {data.id && (
        <p>
          <span>id</span>
          {data.id}
        </p>
      )}
      {data.module && (
        <p>
          <span>module</span>
          {data.module}
        </p>
      )}
      {data.ptr && (
        <p>
          <span>ptr</span>
          {data.ptr}
        </p>
      )}
    </div>
  );
}

export default ShodanShodan;
