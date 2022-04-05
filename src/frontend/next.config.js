const nextTranslate = require("next-translate");

const { PHASE_DEVELOPMENT_SERVER } = require("next/constants");

module.exports = (phase) => {
  // credentiale do bazy danych z pliku ./.env
  if (phase === PHASE_DEVELOPMENT_SERVER) {
    //gdy jesteśmy w developerskim serwerze
    return {
      ...nextTranslate(),
      trailingSlash: true,
      reactStrictMode: true,
    };
  }

  // gdy jestesmy w produckji
  return {
    ...nextTranslate(),
    trailingSlash: true,
    reactStrictMode: true,
  };
};