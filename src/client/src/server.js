// MOCKED server

import { createServer } from "miragejs";

let movies = [
  { id: 1, name: "Inception", year: 2010 },
  { id: 2, name: "Interstellar", year: 2014 },
  { id: 3, name: "Dunkirk", year: 2017 },
];

createServer({
  routes() {
    this.namespace = "/api";

    // Responding to a POST request
    this.post("/movies", (schema, request) => {
      let attrs = JSON.parse(request.requestBody);
      attrs.id = Math.floor(Math.random() * 100);
      //   dokładanie nowego filmu do listy filmów
      movies.push(attrs);

      return { movie: attrs };
    });

    this.get("/movies", () => {
      return {
        // .then((json) => setData(json.movies));
        movies,
      };
    });
  },
});
