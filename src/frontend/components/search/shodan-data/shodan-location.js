function ShodanLocation(props) {
  const data = JSON.parse(props.data);
  return (
    <div>
      <h3>location</h3>
      {data.city ? (
        <p>
          <span>city</span>
          {data.city}
        </p>
      ) : null}
      {data.region_code && (
        <p>
          <span>region_code</span>
          {data.region_code}
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
      {data.latitude && (
        <p>
          <span>latitude</span>
          {data.latitude}
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
    </div>
  );
}

export default ShodanLocation;
