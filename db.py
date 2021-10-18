import pymongo
from dateutil import parser
import script
from config import USER, PASS


def get_database():
    """
    :return: Connection to the Mongo DataBase
    """
    CONNECTION_STRING = f"mongodb+srv://{USER}:{PASS}@cluster.xslp6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # Create a connection using MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['users']


def date_correct(items: dict) -> dict:
    """
    This function is correcting date-strings to date-format in Mongo.
    :param items: Dictionary of our data from site
    :return: Corrected dictionary
    """
    for item in items:
        item['dob']['date'] = parser.parse(item['dob']['date'])
        item['registered']['date'] = parser.parse(item['registered']['date'])
    return items


def drop_element(entity: dict) -> bool:
    try:
        assert entity  # Not empty
        if len(entity) > 1:
            collection_name.delete_many(entity)
        else:
            collection_name.delete_one(entity)
        return True
    except Exception as _ex:
        print(_ex)
        return False


def collect_elements() -> list:
    collection = [x for x in collection_name.find()]
    return collection


def insert_entity(entity: dict) -> bool:
    try:
        assert entity  # Entity not empty
        if len(entity) > 1:
            collection_name.insert_many(entity)
        else:
            collection_name.delete_one(entity)
        return True
    except Exception as _ex:
        print(_ex)
        return False


def main():
    # dbname = get_database()
    # Get the collection from DB
    # collection_name = dbname["data"]
    # Correcting dates
    data = date_correct(script.main())
    # Pushing changes to DB
    collection_name.insert_many(data)


if __name__ == "__main__":
    dbname = get_database()
    collection_name = dbname["data"]
    main()