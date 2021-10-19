from flask import Flask, jsonify, request, abort, Response
import db


app = Flask(__name__)


@app.route('/api/', methods=['GET'])
def get_collection():
    dbname = db.get_database()
    collection_name = dbname["data"]
    return jsonify(str([x for x in collection_name.find()]))


@app.route('/api/', methods=['POST'])
def insert_entity():
    json = request.get_json()
    if not json:
        abort(400)
    else:
        dbname = db.get_database()
        collection_name = dbname["data"]
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
        dbname = db.get_database()
        collection_name = dbname["data"]
        result = collection_name.find_one_and_delete(json)
        if result is not None:
            return Response(status=200)
    return Response(status=501)


if __name__ == '__main__':
    if not db.get_database().list_collection_names():
        db.initialize()
    app.run(debug=False)
