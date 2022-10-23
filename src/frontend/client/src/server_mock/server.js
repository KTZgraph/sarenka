// MOCKED server
// https://miragejs.com/docs/getting-started/overview/
// https://www.youtube.com/watch?v=Xw3K6Kk5Npw

import { createServer, Model } from "miragejs";
import { cveList } from "./cve_list";

createServer({
  models: {
    cve: Model,
    cwe: Model,
  },

  routes() {
    this.namespace = "/api";

    // CVE (Common Vulnerabilities and Exposures)
    // GET LIST
    this.get("/vulnerabilities", () => {
      return {
        cves: cveList,
      };
    });

    // GET by ID
    this.get("/vulnerabilities/:id", (schema, request) => {
      return cveList[0];
    });
  },
});
