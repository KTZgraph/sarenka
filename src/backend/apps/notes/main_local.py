# połączenie z lokalną bazą danych mongoDB
# https://docs.mongodb.com/manual/reference/operator/ dokumentacja do operatorów wyszukiwania
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

cluster = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false'
client = MongoClient(cluster)

# print(client.list_database_names())

# test to nazwa bazy danych
db = client.test

# print(db.list_collection_names())

# dodanie danych do bazy, słownik
todo1 = {
    "name": "Imie",
    "text": "Przykladowy tekst",
    "status": "open",
    "tags": ["python", "codig"],  # nested documents
    "date": datetime.utcnow()  # nie trzeba zamieniać na stringa
}

# todo to nazwa kolekcji z bazy test
todos_collection = db.todo

# result = todos_collection.insert_one(todo1)

# dodanie wielu dokumentów - listy dokumentów
todos2 = [
    {
        "name": "Imie2",
        "text": "Przykladowy tekst2",
        "status": "open",
        "tags": ["python", "codig"],  # nested documents
        "date": datetime.utcnow()  # nie trzeba zamieniać na stringa
    },
    {
        "name": "Imie3",
        "text": "Przykladowy tekst3",
        "status": "open",
        "tags": ["c++", "codig"],  # nested documents
        "date": datetime.utcnow()  # nie trzeba zamieniać na stringa
    }
]


# result = todos_collection.insert_many(todos2)


#pobieranie danych - pierwszy match zwróci
result = todos_collection.find_one()
# print(result)

#pobieranie konkretnedo dokuemntu - query
result = todos_collection.find_one({"name": "Imie3"})
# print(result)

#więcej filtrów
result = todos_collection.find_one({"name": "Imie3", "text": "Przykladowy tekst3"})
# print(result)

#szuaknei po zagnieżdżonych danych tutaj tagach
result = todos_collection.find_one({"tags": "c++"})
# print(result)

#szukanie po id z bazy MongoDB - nie działa po samym stringu
# result = todos_collection.find_one({"_id": "61ffd49d3a88cf84ab6c40c3"})
result = todos_collection.find_one({"_id": ObjectId("61ffd49d3a88cf84ab6c40c3")})
# print(result)

#samo find #uwać na cursor - tylko raz wyświetla dane
results = todos_collection.find({"name": "Imie"}) #<pymongo.cursor.Cursor object at 0x0000016757F1CDC0>
# print(list(results))

#można iterować
# for result in results:
    # print(result)
#albo zamienić na listę
# print(list(results)) #jak sie tu wyprintuje to curson już pustą listę zwraca


#zliczanie WSZYSTKICH dokuemntów - pusty obiekt do filtrów
# print(todos_collection.count_documents({}))
#zliczanie np po tagach
# print(todos_collection.count_documents({"tags": "c++"}))
# print(todos_collection.count_documents({"tags": "python"}))

#szukanie po zakresie - daty $lt - less than przed tą datą coś n
d = datetime(2022, 2, 5)
# results = todos_collection.find({"date": {"$lt": d}}) #$lt - less than przed tą datą coś n
# results = todos_collection.find({"date": {"$gt": d}})  #$gt - greater than przed tą datą coś n
results = todos_collection.find({"date": {"$gt": d}}).sort("name")  #sortowanie po kluczu
for result in results:
    print("po dacie")
    print(result)

#usuwanie
result = todos_collection.delete_one({"_id": ObjectId("61ffd49d3a88cf84ab6c40c2")}) #usuwanie po id
# result = todos_collection.delete_many({"name": "Imie"}) #usuwanie wielu

# UWAGA ! usuwanie wsyzstkeigo
# result = todos_collection.delete_many({})

# UPDATE po lewej wyszukwanie, po prawej co aktualizujemy $set - zmiana statusu
result = todos_collection.update_one({"tags": "c++"}, {"$set": {"status": "done"}})

# $unset - usuwanie specyficzne pole z dokumnetu
result = todos_collection.update_one({"tags": "c++"}, {"$unset": {"status": None}})

#można w ten sam sposób co update dodać nowe pole
result = todos_collection.update_one({"tags": "c++"}, {"$set": {"status": "newStatus"}})
