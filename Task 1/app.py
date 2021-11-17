from flask import Flask, jsonify, request, abort, Response
from db import get_database as dbname
from db import initialize


app = Flask(__name__)


@app.route('/api/', methods=['GET'])
def get_collection():
    collection_name = dbname()["data"]
    return jsonify(str([x for x in collection_name.find()]))


@app.route('/api/', methods=['POST'])
def insert_entity():
    json = request.get_json()
    if not json:
        abort(400)
    else:
        collection_name = dbname()["data"]
        try:
            collection_name.insert_one(json)
        except Exception as _ex:
            return abort(500)
    return Response(status=200)


@app.route('/api/', methods=['DELETE'])
def del_item():
    json = request.get_json()
    if not json:
        abort(400)
    else:
        collection_name = dbname()["data"]
        result = collection_name.find_one_and_delete(json)
        if result is not None:
            return Response(status=200)
    return Response(status=501)


if __name__ == '__main__':
    if not dbname().list_collection_names():
        initialize()
    app.run(debug=True)
