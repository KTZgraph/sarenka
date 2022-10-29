// https://youtu.be/oa_YvzYDyR8?t=518
// WARNING - ustawienia cookies
// dwa sposoby
// 1. directly on the browser
// 2 przez fetch
// jak w odpowiedzi dostanie się setCookieHeader, to powie przeglądarce - ok musimy ustawić cookies
// i wysłanie header along with that cookie header i przeglądarka wie what to set

const express = require("express");

// https://www.npmjs.com/package/cookie
const cookie = require("cookie");

// WARNING https://www.npmjs.com/package/node-fetch
// sposób importu z dokumentacji
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.post("/api/users/login", async (req, res) => {
  // dobicie się do django - do tych z tokenami /api/token
  // \sarenka\src\service-core\auth_site\urls.py
  const { email, password } = req.body;

  const body = JSON.stringify({ email, password });

  try {
    // API_URL odnosi się do serwera Django
    const apiRes = await fetch(`${process.env.API_URL}/api/token/`, {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body,
    });

    const data = await apiRes.json();

    if (apiRes.status === 200) {
      // jak się udało, to sutawiania cookies
      //   data bedize mieć refresh i acces token
      //   zamiast wysyłać i expose tokeny do klienta to chcę mieć je w cookies

      // WARNING - ustawianie cookie, dwa ciastka ustawiam to lista
      // https://youtu.be/oa_YvzYDyR8?t=822
      res.setHeader("Set-Cookie", [
        // WARNING - mozna zaisntalowac paczkę która wszystko łądnie ustawi za mnie
        // https://www.npmjs.com/package/cookie
        // `access=${data.access}; HttpOnly; Secure; Max-Age:1800;`
        cookie.serialize("access", data.access, {
          // opcje z dokuemnecjai, encode, expires, domain etc.
          httpOnly: true,
          // bo na backnediz eustawiałm,ze token ma być aktywny przez 30 min
          // sarenka\src\service-core\auth_site\settings.py
          //   SIMPLE_JWT = {
          // "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
          //   jak będzie expired to browser usunie cookie
          maxAge: 60 * 30,
          path: "/api/",
          //  sameSite: "strict", to ważne, żeby cookie nie wyszły poza same origin
          sameSite: "strict",
          //   secure odnosi się do https, na produkcji ma być wałsnie https
          secure: process.env.NODE_ENV === "production",
        }),
        // to wszytko można zapisac w jednym stringu zamiast uzywać cookie biblioteki
        // `access=${access}; HttpOnly; MAx-Age: 1800; Path: /api/; SameSite:Strict; secure:false`

        cookie.serialize("refresh", data.refresh, {
          // cookie do tokena rrefresh
          httpOnly: true,
          // jedne dzień jest token aktywny, bo simple-token z Django domyślnie expired after a day
          maxAge: 60 * 60 * 24,
          path: "/api/",
          sameSite: "strict",
          secure: process.env.NODE_ENV === "production",
        }),
      ]);

      return res.status(200).json({ success: "Logged in succesfully" });
    } else {
      // status i dane ze zworkti
      return res.status(apiRes.status).json(data);
    }
  } catch (err) {
    return res.status(500).json({
      error: "Somethin when wrong whne logging in",
    });
  }
});

module.exports = router;
