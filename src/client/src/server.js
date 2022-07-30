// MOCKED server
//https://miragejs.com/docs/getting-started/overview/

import { createServer, Model } from "miragejs";

createServer({
  models: {
    movie: Model,
  },

  seeds(server) {
    server.create("movie", { name: "Inception", year: 2010 });
    server.create("movie", { name: "Interstellar", year: 2014 });
    server.create("movie", { name: "Dunkirk", year: 2017 });
  },

  routes() {
    this.namespace = "/api";

    this.get("/movies", (schema, request) => {
      return schema.movies.all();
    });

    this.get("/movies/:id", (schema, request) => {
      let id = request.params.id;

      return schema.movies.find(id);
    });

    this.post("/movies", (schema, request) => {
      let attrs = JSON.parse(request.requestBody);

      return schema.movies.create(attrs);
    });

    this.patch("/movies/:id", (schema, request) => {
      let newAttrs = JSON.parse(request.requestBody);
      let id = request.params.id;
      let movie = schema.movies.find(id);

      return movie.update(newAttrs);
    });

    this.delete("/movies/:id", (schema, request) => {
      let id = request.params.id;

      return schema.movies.find(id).destroy();
    });
  },
});
