from flask import Flask, request, jsonify, make_response,g

import sqlite3 as sql

app = Flask(__name__)

DATABASE = '/sanctioned.db'

def get_db():
    db = getattr(g,'_database', None)

    if not db:
        db = g._database = sql.connect(DATABASE)
    db.row_factory = sql.Row# returns all rows as named tuples
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database', None)

    if not db:
        db.close()

def make_dicts(cursor, row):
    return {(cursor.description[idx][0], value) for idx, value in enumerate(row)}

def query_db(query, args=(), one= False):
    cur = get_db().execute(query,args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def test_data():
    data = [{'name':'Kristopher Doe',
              'sanctioned':True},
            {'name':'Royal Arctic Line',
              'sanctioned':True},
            ]
    return data

@app.route('/', methods=['GET'])
def home():
    return "<h1>Sanctions Archive</h1><p>This site is a prototype API for verifying sanctioned indivs.</p>"

@app.route('/sanctioned/all',methods=['GET'])
def all_sanctioned():
    return jsonify(test_data())

@app.route('/sanctioned/<str:name>',methods=['GET'])
def get_sanctioned(name:str):
    sanctioned=[]
    #check here if in the sanctioned list or not
    for user in query_db('select * from sanctioned'):
        sanctioned.append(user)
    
    return

@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error':'Not Found'}),404)

if __name__ == "__main__":
    app.run(debug=True)