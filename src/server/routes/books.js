import express from 'express';
const router = express.Router();
// nanoid do generowanie unikatowych id książek
import { nanoid } from 'nanoid';

const idLength = 8;

// pobieranie listy wszsytkich ksiażek
router.get('/', (req, res) => {
  // obiekt req ma dostęp do obiektu app
  // dzięki app.db = db; z index.js mamy dostęp do bazy
  const books = req.app.db.get('books');

  res.send(books);
});

// pobieranie ksiazki po id
router.get('/:id', (res, req) => {
  const book = req.app.db
    .get('books')
    .find({ id: req.params.id })
    .value();

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

    req.app.db.get('books').push(book).write();
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
