from cgitb import reset
import collections
from datetime import datetime

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
DEFAULT_VALUE = ""


def get_db_connector() -> pymongo.database.Database:
    client = MongoClient(CONNECTION_STRING)

    # nazwa bazy danych to 'sarenka'
    db = client.sarenka
    return db


def get_notes_collection(collection_name="notes") -> pymongo.collection.Collection:
    db = get_db_connector()

    # notes to nazwa kolekcji
    # return db.notes
    return db[collection_name]


def find_note_by_id(note_id: str) -> pymongo.cursor.Cursor:
    if note_id is None:
        return

    collection = get_notes_collection()
    result = collection.find_one({"_id": ObjectId(note_id)})

    return result


def update_note(note_id: str, data: str) -> pymongo.results.UpdateResult:
    collection = get_notes_collection()

    collection.update_one({"_id": note_id}, {"$set": {"data": data}})

    result = collection.find_one({"_id": note_id})
    return result


def save_note(note: dict) -> pymongo.results.InsertOneResult:
    collection = get_notes_collection()
    try:
        # result = collection.insert_one(note).inserted_id
        inserted_id = collection.insert_one(note).inserted_id
        result = collection.find_one({"_id": inserted_id})

        return result
    except pymongo.errors.DuplicateKeyError:
        print(f'Note with id:{note["_id"]} already exists')


def get_or_create_note(note_id):
    """
    collection.find_one({"_id": ObjectId(note_id)}) nie
    """
    if note_id is None:
        return

    collection = get_notes_collection()
    result = collection.find_one({"_id": note_id})

    if not result:
        result = save_note({"_id": note_id, "data": DEFAULT_VALUE})

    return result
