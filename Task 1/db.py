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


def initialize():
    # Get the DB
    dbname = get_database()
    # Get the collection from DB
    collection_name = dbname["data"]
    # Correcting dates
    data = date_correct(script.main())
    # Pushing changes to DB
    collection_name.insert_many(data)


if __name__ == "__main__":
    initialize()
