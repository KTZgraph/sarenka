import { useEffect, useState } from "react";
import Sidebar from "../../../components/organisms/sidebar/Sidebar";
import Navbar from "../../../components/organisms/navbar/Navbar";
import styles from "./Single.module.scss";
import Spinner from "../../../components/atoms/spinner";

const Single = () => {
  const [data, setData] = useState(null);
  // id filmu
  const [movieId, setMovieId] = useState(null);
  // informacja o tym, że jesteśmy w stanie update
  const [updating, setUpdating] = useState(false);
  // stan dla formularza
  const [name, setName] = useState("");
  const [year, setYear] = useState("");
  // stan dla aktorów filmu
  const [actors, setActors] = useState(null);

  // pobieranie danych GET
  useEffect(() => {
    fetch("/api/movies")
      .then((res) => res.json())
      .then((json) => setData(json.movies))
      // FIXME - globalne informowanie o errorze
      .catch((error) => console.log(error));
  }, []);

  // POST - tworzenie nowego filmu

  // osobna funckja do tworzenia filmów
  const createMovie = async () => {
    // tworzenie NOWEGO filmu
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

  // osobna funkjc ado aktualizji filmów
  const updateMovie = async () => {
    // tworzenie NOWEGO filmu
    try {
      const res = await fetch(`/api/movies/${movieId}`, {
        method: "PATCH",
        body: JSON.stringify({ name, year }),
      });
      const json = await res.json();

      // nie tworzymy tylko aktulizujemy jeden obiekt z listy
      // żeby być reaktywnym musimy skopiowac listę najpierw
      // 1. szukamy tego filmu zakutlizowanego po id w liście (dlatego index findIndex)
      const dataCopy = [...data]; // spread the existing movies
      const index = data.findIndex((m) => m.id === movieId);
      // aktulizuję tylko jeden element w liście
      dataCopy[index] = json.movie;

      // stan danych w komponencie to zaktualizowana lista ze zmienionym filmem
      setData(dataCopy);
      // czyszczenie inputów formularza
      setName("");
      setYear("");
      // koniec updatu - zmienna stanowa znowu na false
      setUpdating(false);
      // czyszcze movieId żeby nie było powtorki z upsdatem niechcący na tym samy co poprzednio obiekcie
      setMovieId(null);
    } catch (error) {
      console.log(error);
    }
  };

  // albo tworzy nowy film albo go atulizuuje zaleźnie od stanu updating
  const submitForm = async (e) => {
    e.preventDefault();

    if (updating) {
      updateMovie();
    } else {
      createMovie();
    }
  };

  // DELETE -usuwanie filmu
  const deleteMovie = async (id) => {
    try {
      await fetch(`/api/movies/${id}`, { method: "DELETE" });
      setData(data.filter((m) => m.id !== id));
    } catch (error) {
      console.log(error);
    }
  };

  // zwykła funckja do aktualizowania filmu
  const setMovieToUpdate = (id) => {
    const movie = data.find((m) => m.id === id);
    // gdy z jakiegoś powodu nie ma tego filmu to zwracamy i nic nie robimy
    if (!movie) return;
    // informowanie o stanie, że jesteśmy w trakcie aktualizacji
    setUpdating(true);
    // id ale dopiero ze znalezionego obiektu, a nie id podanego od usera
    setMovieId(movie.id);

    // ustawianie stanow dla formularza
    setName(movie.name);
    setYear(movie.year);
  };

  // pobieranie aktorów dla filmu
  const fetchActors = async (id) => {
    try {
      const res = await fetch(`/api/movies/${id}/actors`);
      const json = await res.json();

      setActors(json.actors);
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
                {/* przyciks dla formularrza - albo akutlizujemy albo tworzymy - stan 'updating' informuje co robimy */}
                <button type="submit" className="submit">
                  {updating ? "Update" : "Create"}
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
                  <th>action</th>
                  <th>actors</th>
                </tr>
              </thead>
              <tbody>
                {data.map(({ id, name, year }) => (
                  <tr key={id}>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{year}</td>
                    {/* map[owanie -lista aktorów] */}
                    <td>
                      {actors?.map((actor) => (
                        // WARNING pamiętac o kluczu dla reacta
                        <p key={actor.id}>{actor.name}</p>
                      ))}
                    </td>
                    <td>
                      {/* update movie */}
                      <button
                        className="buttonUpdate"
                        onClick={() => setMovieToUpdate(id)}
                      >
                        Update
                      </button>
                      {/* relacja aktorzy - pobieranie aktorów dla filmu*/}
                      <button
                        className="buttonFetch"
                        onClick={() => fetchActors(id)}
                      >
                        Fetch actor
                      </button>
                      {/* usuwanie filmu po id */}
                      <button
                        className="buttonDelete"
                        onClick={() => deleteMovie(id)}
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : data ? (
            <p>No movies</p>
          ) : (
            <Spinner />
          )}
        </div>
        <div className={styles.bottom}></div>
      </div>
    </div>
  );
};

export default Single;
