//  TODO uprościc swaggera przez reużywalne "parameters"
// TODO swagger.io/docs/specification/components/

import express from 'express';
const router = express.Router();
// nanoid do generowanie unikatowych id książek
import { nanoid } from 'nanoid';

const idLength = 8;

// tworzenie modelu obiketu book dla bazy, który jest używane przez swaggera
//wielolinijkowy komentarz
//swagger.io/docs/specification/components/
/**
 * @swagger
 * components:
 *  schemas:
 *      Book:
 *          type: object
 *          required:
 *              - title
 *              - author
 *          properties:
 *              id:
 *                  type: string
 *                  descriiption: The aut-generated id of the book
 *              title:
 *                  type: string
 *                  description: The book title
 *              author:
 *                  type: string
 *                  description: The book author
 *          example:
 *              id: d5fE_asz
 *              title: The New Turing Omnibus
 *              author: Alexander K. Dewdney
 */

// grupopwanoie routów w swaggerze
/**
 * @swagger
 * tags:
 *  name: Books
 *  description: The books managaging API
 */

// route routs definition
// routy dla swaggera - ale difiniować jak są relatywne w index.js tzn tutaj url root "/" jest jako "/books/" w index.js i włąsnie ta wersja globalna jest w swaggerze
/**
 * @swagger
 * /books:
 *  get:
 *      summary: Returns the list of all the books
 *      tags: [Books]
 *      responses:
 *          200:
 *              description: The list of the books
 *              content:
 *                  application/json:
 *                      schema:
 *                          type: array
 *                          items:
 *                              $ref: '#components/schemas/Book'
 */

// pobieranie listy wszsytkich ksiażek
// router.get('/', (req, res) => {
//   // obiekt req ma dostęp do obiektu app
//   // dzięki app.db = db; z index.js mamy dostęp do bazy
//   const books = req.app.db.get('books');

//   res.send(books);
// });

router.get('/', (req, res) => {
  // pobieranie danych z biblioteki
  // https://www.npmjs.com/package/@commonify/lowdb
  const books = req.app.db.data;

  res.send(books);
});

// ----------------- pobieranie ksiazki po id
/**
 * @swagger
 * /books/{id}:
 *   get:
 *     summary: Get the book by id
 *     tags: [Books]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: string
 *         required: true
 *         description: The book id
 *     responses:
 *       200:
 *         description: The book description by id
 *         contens:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Book'
 *       404:
 *         description: The book was not found
 */

router.get('/:id', (req, res) => {
  const book = req.app.db.data.books.find(
    (obj) => obj.id === req.params.id
  );

  if (!book) {
    res.sendStatus(404);
  }

  res.send(book);
});

// -------------- tworzenie nowej ksiazki - POST
/**
 * @swagger
 * /books:
 *   post:
 *     summary: Create a new book
 *     tags: [Books]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Book'
 *     responses:
 *       200:
 *         description: The book was successfully created
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Book'
 *       500:
 *         description: Some server error
 */

router.post('/', (req, res) => {
  try {
    const book = {
      // autogenerowane id o dłguości jaką ustaliliśmy
      id: nanoid(idLength),
      // FIXME niebezpieczne - powinno się parsować i sprawdzać dane od usera
      ...req.body,
    };

    // req.app.db.get('books').push(book).write();
    req.app.db.data.books.push(book);
    res.send(book);
  } catch (error) {
    return res.status(500).send(error);
  }
});

// ---------- aktualizacja ksiązki po id - PUT
/**
 * @swagger
 * /books/{id}:
 *  put:
 *      summary: Update the book by the id
 *      tags: [Books]
 *      parameters:
 *          - in: path
 *            name: id
 *            schema:
 *              type: string
 *            required: true
 *            description: The book id
 *      requestBody:
 *          required: true
 *          content:
 *              application/json:
 *                  schema:
 *                      $ref: '#/components/schemas/Book'
 *      responses:
 *          200:
 *              description: The book was updated
 *              content:
 *                  application/json:
 *                      schema:
 *                          $ref: '#components/schemas/Book'
 *          404:
 *              description: The book was not found
 *          500:
 *              description: Some error happened
 */

router.put('/:id', (req, res) => {
  //stackoverflow.com/questions/71164360/how-to-find-and-replace-an-object-with-in-array-of-objects
  try {
    // stara ksiżka
    const target = req.app.db.data.books.find(
      (obj) => obj.id === req.params.id
    );

    const source = req.body;
    Object.assign(target, source);

    // nowa ksiazka zaktulizowana
    const book = req.app.db.data.books.find(
      (obj) => obj.id === req.params.id
    );

    res.send(book);
  } catch (error) {
    return res.status(500).send(error);
  }
});

// ------------ usuwanie ksiażki - DELETE
/**
 * @swagger
 * /books/{id}:
 *   delete:
 *     summary: Remove the book by id
 *     tags: [Books]
 *     parameters:
 *       - in: path
 *         name: id
 *         schema:
 *           type: string
 *         required: true
 *         description: The book id
 *
 *     responses:
 *       200:
 *         description: The book was deleted
 *       404:
 *         description: The book was not found
 */

router.delete('/:id', (req, res) => {
  // stara ksiżka

  const target = req.app.db.data.books.find(
    (obj) => obj.id === req.params.id
  );

  if (!target) {
    res.sendStatus(404);
    return;
  }

  console.log('------------------------------');
  console.log('target: ', target);

  //   res.send(req.params.id);
  //   res.sendStatus(200);
  res.status(200).json({ book: target });
});

// export
// module.exports = router;
export default router;
