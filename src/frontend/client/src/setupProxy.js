/*
WARNING nie używać składni ES6
https://create-react-app.dev/docs/proxying-api-requests-in-development/ nazwa pliku i ściezka z dokumentacji

Note: This file only supports Node's JavaScript syntax. Be sure to only use supported language features 
(i.e. no support for Flow, ES Modules, etc).
*/

const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api",
    createProxyMiddleware({
      // bo mój express server jest na porcie 5000
      target: "http://localhost:5000",
      changeOrigin: true,
    })
  );
};
