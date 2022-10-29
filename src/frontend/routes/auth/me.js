const express = require("express");

// WARNING https://www.npmjs.com/package/node-fetch
// sposób importu z dokumentacji
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.get("/api/users/me", async (req, res) => {
  // tutaj potrzebuję cookie
  // https://youtu.be/oa_YvzYDyR8?t=1674
  //   npm install --save cookie-parser nie trzeba ale jest ładniej - import w index.js

  const { access } = req.cookies;

  //   mogę zrobić authorized request do backendu
  try {
    const apiRes = await fetch(`${process.env.API_URL}/api/users/me`, {
      method: "GET",
      headers: {
        accept: "application/json",
        // do autoryzacji
        Authorization: `Bearer ${access}`,
      },
    });

    const data = await apiRes.json();
    return res.status(apiRes.status).json(data);
  } catch (err) {
    return res.status(500).json({
      error: "Something went wrong when trying to retrieve user",
    });
  }
});

module.exports = router;
