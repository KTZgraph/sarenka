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

// routy dla swaggera - ale difiniować jak są relatywne w index.js tzn tutaj url root "/" jest jako "/books/" w index.js i włąsnie ta wersja globalna jest w swaggerze
/**
 * @swagger
 * /books:
 *  get:
 *      summary: Returns the list of all the books
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

// pobieranie ksiazki po id
router.get('/:id', (res, req) => {
  const book = req.app.db.data.find({ id: req.params.id }).value();

  res.send(book);
});

// tworzenie nowej ksiazki - POST
router.post('/', (req, res) => {
  try {
    const book = {
      // autogenerowane id o dłguości jaką ustaliliśmy
      id: nanoid(idLength),
      // FIXME niebezpieczne - powinno się parsować i sprawdzać dane od usera
      ...req.body,
    };

    // req.app.db.get('books').push(book).write();
    req.app.db.data.push(book).write();
    //   await req.app.db.books.write()
  } catch (error) {
    return res.status(500).send(error);
  }
});

// aktualizacja ksiązki po id - PUT
router.put('/:id', (req, res) => {
  try {
    req.app.db
      .get('books')
      .find({ id: req.params.id })
      .assign(req.body)
      .write();

    res.send(req.app.db.get('books').find({ id: req.params.id }));
  } catch (error) {
    return res.status(500).send(error);
  }
});

// usuwanie ksiażki - DELETE
router.delete('/', (req, res) => {
  // write żeby usunąć z bazy danych
  req.app.db.get('books').remove({ id: req.params.id }).write();
  res.sendStatus(200);
});

// export
// module.exports = router;
export default router;
