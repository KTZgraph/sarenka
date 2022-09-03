// IMPORTY

// const express = require('express');
import express from 'express';

// const cors = require('cors');
import cors from 'cors';
// const morgan = require('morgan');
import morgan from 'morgan';

// propblem z importem https://www.npmjs.com/package/lowdb
// const low = require('lowdb');
import { Low, JSONFile } from 'lowdb';

import { dirname } from 'path';
import { fileURLToPath } from 'url';
import { join } from 'path';
const __dirname = dirname(fileURLToPath(import.meta.url));
const file = join(__dirname, 'db.json');

// domyślny port aplikacji
const PORT = process.env.PORT || 4000;

// dane zapisywane w pliku
// const FileSync = require('lowdb/adapters/FileSync');
// specyfikacja w którym pliku zapisujemy dane
// const adapter = new FileSync('db.json');
const adapter = new JSONFile(file);

// const db = low(adapter);

const db = new Low(adapter);
console.log(db);

// defaultowe dane - pusta lista ksiażek
// db.defaults({ books: [] }).write();
// https://github.com/typicode/lowdb/issues/505 problem TypeError: db.defaults is not a function
// Set some defaults
if (db.data === null) {
  db.data = { books: [] };
  db.write();
}

console.log(db);

// inicjalizacja aplikacji express
const app = express();
// dopisanie danych - można potem skorzystać z bazy za pomocą routów
app.db = db;

// inicjalizacja corsów
app.use(cors());
// middlewary
app.use(express.json());
app.use(morgan('dev'));

// właczenie serwera do snasłuchiwania
app.listen(PORT, () =>
  console.log(`The server is running on port ${PORT}`)
);
