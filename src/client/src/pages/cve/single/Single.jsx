import { useEffect, useState } from "react";
import Sidebar from "../../../components/sidebar/Sidebar";
import Navbar from "../../../components/navbar/Navbar";
import CveData from "../../../components/cve/details/Single";
import styles from "./Single.module.scss";

const Single = () => {
  const [data, setData] = useState(null);
  const [name, setName] = useState("");
  const [year, setYear] = useState("");

  // pobieranie danych GET
  useEffect(() => {
    fetch("/api/movies")
      .then((res) => res.json())
      .then((json) => setData(json.movies))
      // FIXME - globalne informowanie o errorze
      .catch((error) => console.log(error));
  }, []);

  // POST - tworzenie nowego filmu
  const submitForm = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("/api/movies", {
        method: "POST",
        body: JSON.stringify({ name, year }),
      });

      const json = await res.json();
      // spread operator - dodawanie nowych danych do listy
      setData([...data, json.movie]);
      // czyszczenie inputów formularza
      setName("");
      setYear("");
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className={styles.single}>
      <Sidebar />
      <div className={styles.singleContainer}>
        <Navbar />
        <div className={styles.top}>
          {/* dodawanie danych - form */}
          <form onSubmit={submitForm}>
            <div className="row">
              <div className="col">
                <input
                  type="text"
                  className="form-contorl"
                  placeholder="Name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </div>
              <div className="col">
                <input
                  type="number"
                  className="form-contorl"
                  placeholder="Year"
                  value={year}
                  onChange={(e) => setYear(e.target.value)}
                />
              </div>
              <div className="col">
                <button type="submit" className="submit">
                  Create
                </button>
              </div>
            </div>
          </form>

          {/* wyuświetlanie danych */}
          <h1>Movies</h1>
          {data?.length > 0 ? (
            <table>
              <thead>
                <tr>
                  <th>id</th>
                  <th>name</th>
                  <th>year</th>
                </tr>
              </thead>
              <tbody>
                {data.map(({ id, name, year }) => (
                  <tr key={id}>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{year}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No movies</p>
          )}
        </div>
        <div className={styles.bottom}></div>
      </div>
    </div>
  );
};

export default Single;
