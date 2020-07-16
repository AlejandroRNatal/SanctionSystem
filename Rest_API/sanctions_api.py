from flask import Flask, request, jsonify, make_response,g,json
import typing
import Sanction
import sanctioned_data_parser
import sqlite3 as sql

app = Flask(__name__)

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sanctioned.db")


# DATABASE = 'sanctioned.db'
DATABASE = db_path

def get_db():
    db = getattr(g,'_database', None)

    if not db:
        db = g._database = sql.connect(DATABASE)
    db.row_factory = sql.Row# returns all rows as named tuples
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database', None)

    if db:
        db.close()

def make_dicts(cursor, row):
    return {(cursor.description[idx][0], value) for idx, value in enumerate(row)}

def query_db(query, args=(), one= False):
    cur = get_db().execute(query,args)
    rv = cur.fetchall()
    # cur.close()
    # NEVER  CLOSES THE CURSOR, MIGHT BE MEMORY LEAK
    # return (rv[0] if rv else None) if one else rv
    return [dict(zip([column[0] for column in cur.description], str(row)))for row in rv]

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

@app.route('/sanctioned/individuals/<string:name>',methods=['GET'])
def get_sanctioned_individual(name):
    sanctioned=[]
    people, countries, orgs =sanctioned_data_parser.parsed_data_params()
    
    #check here if in the sanctioned list or not
    for row in query_db('select * from sanctioned'):
        sanctioned.append(row[people])
    
    # probability = Sanction.sanction_list_probability(name, sanctioned)

    status, prob = Sanction.is_sanctioned(name, sanctioned)
    
    return jsonify({people : name,'Sanctioned':status , 'Probability':prob})


@app.route('/sanctioned/organizations/<string:name>',methods=['GET'])
def get_sanctioned_organization(name):
    sanctioned=[]
    people, countries, orgs =sanctioned_data_parser.parsed_data_params()
    
    #check here if in the sanctioned list or not
    for row in query_db('select * from sanctioned'):
        sanctioned.append(row[orgs])

    status, prob = Sanction.is_sanctioned(name, sanctioned)
    
    return jsonify({orgs : name,'Sanctioned':status , 'Probability':prob})


@app.route('/sanctioned/countries/<string:name>',methods=['GET'])
def get_sanctioned_countries(name):
    sanctioned=[]
    people, countries, orgs =sanctioned_data_parser.parsed_data_params()
    
    #check here if in the sanctioned list or not
    for row in query_db('select * from sanctioned'):
        sanctioned.append(row[countries])

    status, prob = Sanction.is_sanctioned(name, sanctioned)
    
    return jsonify({countries : name,'Sanctioned':status , 'Probability':prob})


@app.route('/sanctioned/',methods=['GET'])
def get_sanctioned():
    # sanctioned=[]

    # #check here if in the sanctioned list or not
    # for user in query_db('select * from sanctioned'):
    #     sanctioned.append(user)
    all = [di for di in query_db('select * from sanctioned')]
    # print(all)
    # print(type(all[0]))

    
    # response = app.response_class(
    #     response=all,
    #     status=200,
    #     mimetype='application/json'
    # )

    # return {"sanctioned":all[0],}
    # return response
    return jsonify(all)


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error':'Not Found'}),404)


if __name__ == "__main__":
    app.run(debug=True)