// IMPORTY

// const express = require('express');
import express from 'express';

// const cors = require('cors');
import cors from 'cors';
// const morgan = require('morgan');
import morgan from 'morgan';

// propblem z importem https://www.npmjs.com/package/lowdb
// const low = require('lowdb');
import { join, dirname } from 'path';
import { Low, JSONFile } from 'lowdb';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
// dane zapisywane w pliku
// const FileSync = require('lowdb/adapters/FileSync');
// specyfikacja w którym pliku zapisujemy dane
// const adapter = new FileSync('db.json');
const file = join(__dirname, 'db.json');
const adapter = new JSONFile(file);
// Use JSON file for storage

const db = new Low(adapter);
// Read data from JSON file, this will set db.data content
await db.read();

// po słowie books będzie ogarniać sobie w routach
db.data ||= { books: [] };

//------------------------------------------------------------------------------------------------------------------------------------------------
//  import swaggera
import swaggerUI from 'swagger-ui-express';
import swaggerJsDoc from 'swagger-jsdoc';

// importowanie routów z server/routes/books.js
import booksRouter from './routes/books.js';

// domyślny port aplikacji
const PORT = process.env.PORT || 4000;

console.log(db);

// swagger PRZED stworzeniem aplikacji express
// obiekt opcji dla swaggera
const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Library API',
      version: '1.0.0',
      description: 'A simple Express Library API',
    },

    servers: [
      // lista serverów, można mieć kilka np testing, production etc, tu mam jeden
      {
        url: 'http://localhost:4000',
      },
    ],
  },

  // apis na tym samym poziomie co definition
  // lista gdzie mamy routy, bo moze być wiecej niż tylko server/routes/books.js
  apis: ['./routes/*.js'],
};

// inicjalizacja swaggera
const specs = swaggerJsDoc(options);

// inicjalizacja aplikacji express
const app = express();
// aplikacja ma używać swaggera
app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(specs));

// dopisanie danych - można potem skorzystać z bazy za pomocą routów
app.db = db;

// inicjalizacja corsów
app.use(cors());
// middlewary
app.use(express.json());
app.use(morgan('dev'));

// dołączanie routów z server/routes/books.js
app.use('/books', booksRouter);

// właczenie serwera do snasłuchiwania
app.listen(PORT, () =>
  console.log(`The server is running on port ${PORT}`)
);
