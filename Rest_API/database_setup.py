import sys, os
import os.path
import sqlite3 as sql3

import database_setup
from sanctioned_data_parser import open_file


def sql_connection(db_name="sanctioned.db"):
    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_name)
    print(db_path)
    try:
        con = sql3.connect(db_path)
        print('Connected to db...')
        return con
    
    except Error:
        print(Error)

    return None# Might be problematic


def sql_table(con):
    people, orgs, countries = 'Individuals','Organizations','Countries'
    curr = con.cursor()
    command = 'create table if not exists sanctioned('+people+' text,'+ orgs + ' text,' + countries+' text)'
    command.encode('utf-8')
    curr.execute(command)
    con.commit()


def setup_db():
    
    con = sql_connection()
    sql_table(con=con)
    populate_db(con=con)
    sql_close(con=con)
    return


def teardown_db(con=sql_connection()):

    cur = con.cursor()
    cur.execute('drop table if exists sanctioned')
    con.commit()
    sql_close(con)
    return


def sql_insert(data:dict, con=sql_connection(),):

    person, country,org = data['Individuals'],data[' Countries'], data[' Organizations']
    cur = con.cursor()
    command = 'INSERT INTO sanctioned(Individuals,Countries,Organizations) VALUES(?,?,?)'
    command.encode('utf-8')
    cur.execute(command , (person,country,org))

    con.commit()
    return


def sql_fetch(con=sql_connection()):

    cur = con.cursor()

    cur.execute('SELECT * FROM sanctioned')

    rows = cur.fetchall()

    for row in rows:
        yield row


def sql_close(con=sql_connection()):
    con.close()
    return

def build_database():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sample.csv")
    print(db_path)
    try:
        con = sql_connection()
        cur = con.cursor()

        sql_table(con)
        for row in open_file(name=db_path):

            # print(row)
            person, country,org = row['Individuals'],row[' Countries'], row[' Organizations']
            # print(f"Individual:{person} | Country:{country} | Organization:{org}")
            command = 'INSERT INTO sanctioned(Individuals,  Organizations, Countries) VALUES(?,?,?)'
            cur.execute(command, (person,country,org))
            con.commit()
        
        if con:
            con.close()
        
        
    except Exception as e:
        print("[!] Error while populating database.")
        print(f"{type(e)}:{e}")

    return


def populate_db(src:str="sanctioned.db",con=sql_connection()):

    try:
        cur = con.cursor()
        for row in open_file(name=src):

            print(row)
            person, country,org = row['Individuals'],row['Countries'], row['Organizations']
            command = 'INSERT INTO sanctioned(Individuals, Countries, Organizations) VALUES(?,?,?)'
            cur.execute(command, (person,country,org))
            con.commit()
        
        
    except Exception as e:
        print("[!] Error while populating database.")
        print(f"{type(e)}:{e}")
    
    return


if __name__ == "__main__":

    build_database()