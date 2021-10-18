import pymongo
from dateutil import parser
import script


User = 'HaveNoMatter'
Pass = 'QdxzpoVpM2OxpFyj'


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://{User}:{Pass}@cluster.xslp6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClien
    client = pymongo.MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['users']


def date_correct(items):
    """
    This function is correcting date-strings to date-format in Mongo.
    :param items: Dictionary of our data from site
    :return: Corrected dictionary
    """
    for item in items:
        item['dob']['date'] = parser.parse(item['dob']['date'])
        item['registered']['date'] = parser.parse(item['registered']['date'])
    return items


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
    collection_name = dbname["data"]
    data = date_correct(script.main())

    collection_name.insert_many(data)




