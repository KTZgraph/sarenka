/*
https://www.youtube.com/watch?v=cvu6a3P9S0M 3:30
npm i --save node-fetch

https://www.npmjs.com/package/node-fetch
z dokumentacji
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

*/
const express = requires("express");
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.post("/api/users/register", (req, res) => {
  // dobicie się do Django
  const { first_name, last_name, email, password } = req.body;
  try{

    const registerRes = await fetch('api/users/register')
  }catch(err){

  }

  
});

module.exports = router;
