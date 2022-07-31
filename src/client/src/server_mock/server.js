// MOCKED server
// https://miragejs.com/docs/getting-started/overview/
// https://www.youtube.com/watch?v=Xw3K6Kk5Npw

import { createServer, Model } from "miragejs";
import { cweList } from "./cwe_list";
import { cveList } from "./cve_list";

createServer({
  models: {
    cve: Model,
    cwe: Model,
  },

  routes() {
    this.namespace = "/api";

    //  CWE (Common Weakness Enumeration)
    this.get("/vulnerabilities/cwes", () => {
      return {
        cwes: cweList,
      };
    });

    this.patch("/vulnerabilities/cwes/:id", (schema, request) => {
      let newAttrs = JSON.parse(request.requestBody);
      let id = request.params.id;
      let cwe = schema.cwes.find(id);

      return cwe.update(newAttrs);
    });

    // CVE (Common Vulnerabilities and Exposures)
    // GET LIST
    this.get("/vulnerabilities/cves", () => {
      return {
        cves: cveList,
      };
    });

    // GET by ID
    this.get("/vulnerabilities/cves/:id", (schema, request) => {
      // FIXME - coś nie działa zwracanie po schematach

      // let id = request.params.id;
      // let cve = schema.cves.find(id);
      // HACK
      return cveList[0];
    });

    // PATCH
    this.patch("/vulnerabilities/cve/:id", (schema, request) => {
      let newAttrs = JSON.parse(request.requestBody);
      let id = request.params.id;
      let cve = schema.cve.find(id);
      return cve.update(newAttrs);
    });
  },
});
