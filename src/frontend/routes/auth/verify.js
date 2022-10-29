/*
https://youtu.be/GaKGYo2jQ2Y?t=648
weryfikacja tokenu
*/
const express = require("express");

// WARNING https://www.npmjs.com/package/node-fetch
// sposób importu z dokumentacji
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.get("/api/users/verify", async (req, res) => {
  // zostawim get bo client React nie wysyła body

  const { access } = req.cookies;

  const body = JSON.stringify({
    //WARNING zamaist body potrzebuję `token` bo
    //     token = serializers.CharField()
    token: access,
  });

  //   mogę zrobić authorized request do backendu
  try {
    // dobijam się do API Django z sarenka\src\service-core\auth_site\urls.py
    // WARNING slash na końcu do enpointa
    const apiRes = await fetch(`${process.env.API_URL}/api/token/verify/`, {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
        // nie daje header, bo to nie jest Authorized request
        // class TokenVerifyView(TokenViewBase): z sarenka\src\service-core\env\Lib\site-packages\rest_framework_simplejwt\views.py
        // class TokenVerifySerializer(serializers.Serializer): z sarenka\src\service-core\env\Lib\site-packages\rest_framework_simplejwt\serializers.py
        //WARNING zamaist body potrzebuję `token` bo
        //     token = serializers.CharField()
      },
      body,
    });

    const data = await apiRes.json();
    // jak wszsytko sie udało to data to pusty obiekt {}
    // jak błedny token to
    //     {
    //     "detail": "Token is invalid or expired",
    //     "code": "token_not_valid"
    // }
    return res.status(apiRes.status).json(data);
  } catch (err) {
    return res.status(500).json({
      error: "Something went wrong when trying to verify login status",
    });
  }
});

module.exports = router;
