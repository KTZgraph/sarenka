/*
https://youtu.be/oa_YvzYDyR8?t=2528
*/

const express = require("express");

// do parsowanie cookie
const cookie = require("cookie");

const router = express.Router();

// WARNING - tu nie trzeba async bo nic nie robię z jsonem na serwerze
// BUG to będzie potrzebne jak chcemy zrobić tocken blacklisting na serwerze
router.get("/api/users/logout", (req, res) => {
  // cookies z requesta są; ale w usmie ich nie potrzebuję chce ustawić ich wartośći w headerze i go wysłać
  res.setHeader("Set-Cookie", [
    cookie.serialize("access", "", {
      httpOnly: true,
      //   maxAge: 60 * 30,
      // maxAge nie potrzebuję, tylko expires
      //   Date(0) zwraca date z przesłości diokładnie  Thu Jan 01 1970 01:00:00 GMT+0100
      expires: new Date(0),
      path: "/api",
      sameSite: "strict",
      secure: process.env.NODE_ENV === "production",
    }),
    cookie.serialize("refresh", "", {
      httpOnly: true,
      //   maxAge: 60 * 30,
      // maxAge nie potrzebuję, tylko expires
      //   Date(0) zwraca date z przesłości diokładnie  Thu Jan 01 1970 01:00:00 GMT+0100
      expires: new Date(0),
      path: "/api",
      sameSite: "strict",
      secure: process.env.NODE_ENV === "production",
    }),
  ]);

  return res.status(200).json({ success: "Logged out successfully" });
});

module.exports = router;
