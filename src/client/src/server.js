// MOCKED server
//https://miragejs.com/docs/getting-started/overview/
// https://www.youtube.com/watch?v=Xw3K6Kk5Npw

import { createServer, Model, hasMany, belongsTo } from "miragejs";

createServer({
  // https://miragejs.com/docs/getting-started/overview/#relationships
  models: {
    movie: Model.extend({
      // liczba mnoga - jeden film ma wielu aktorów
      actors: hasMany(),
    }),
    actor: Model.extend({
      movie: belongsTo(),
    }),
  },

  seeds(server) {
    // WARNING - średniki po obiektach
    // można aktorów utworzyć tutaj osobno a potem dodawac tego samego do wielu różnych filmów
    const matt = server.create("actor", { name: "Matthew McConaughey" });
    const anne = server.create("actor", { name: "Anne Hathaway" });
    const jess = server.create("actor", { name: "Jessica Chastain" });
    const tom = server.create("actor", { name: "Tom Hardy" }); // w dwóch filmach gra
    const cillian = server.create("actor", { name: "Cilcian Muphry Chastain" });
    // po prostu lista aktorów którzy grają w filmie jako atrybut obiektu
    server.create("movie", {
      name: "Inception",
      year: 2010,
      actors: [matt, tom],
    });
    server.create("movie", {
      name: "Interstellar",
      year: 2014,
      actors: [matt, anne],
    });
    server.create("movie", {
      name: "Dunkirk",
      year: 2017,
      actors: [cillian, tom],
    });
  },

  routes() {
    this.namespace = "/api";

    // this.get("/movies", (schema, request) => {
    //   return schema.movies.all();
    // });

    // this.get("/movies/:id", (schema, request) => {
    //   let id = request.params.id;

    //   return schema.movies.find(id);
    // });

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

    // this.delete("/movies/:id", (schema, request) => {
    //   let id = request.params.id;

    //   return schema.movies.find(id).destroy();
    // });

    // skrótowe
    // https://miragejs.com/docs/getting-started/overview/#shorthands
    this.get("/movies");
    this.get("/movies/:id");
    // WARNING problemy z dzaiłąniem metody post i patch prawdopodobnie prze zustawienia serializatora
    // this.post("/movies");
    // this.patch("/movies/:id");
    this.del("/movies/:id");

    // endpoint do pobierania aktorów
    this.get("/movies/:id/actors", (schema, request) => {
      let movie = schema.movies.find(request.params.id);
      return movie.actors; // zwraca listę aktorów z obiektu filmu
    });
  },
});
