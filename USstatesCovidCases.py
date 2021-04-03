from flask import Flask, render_template, request, jsonify
import json
import requests
import pymysql

conet = pymysql.connect(
                host = 'cloudcomputing.c5rdeo5n93cd.us-east-1.rds.amazonaws.com',
                port = 3306,
                user = 'JoshJain',
                password = '12345678',
                db = 'Country_Cases')

app = Flask(__name__)

#this function gets all the data present in MYSQL database
@app.route('/covidUScases', methods=['GET'])
def get_USstatesCovidData():
        csr = conet.cursor()
        csr.execute("""SELECT * from Country_Cases.United_States""")
        details = csr.fetchall()
        if len(details):
                return jsonify({'The Columns are as followed':'StateName, Confirmed, Deaths, Updated'}, details[:]), 200
        else:
                return jsonify({'error':'No data present'}), 400


#this function adds a perticular  data to the existing database
@app.route('/covidUScases', methods=['POST'])
def add_State():
        csr = conet.cursor()
        csr.execute("""INSERT INTO Country_Cases.United_States VALUES('Mississippi', 304695, 7001, '30-03-2021')""")
        details = csr.fetchall()
        return jsonify({'Success':'Data Added'}), 200

# to update the place, run the command in the terminal:-
#curl -i -H "content-Type: application/json" -X POST -d details http://<paste the public DNS>:5000/covidUScases


#this function updates a perticular data in the database
@app.route('/covidUScases', methods=['PUT'])
def update_State():
        csr = conet.cursor()
        csr.execute("""UPDATE Country_Cases.United_States SET Confirmed = 305417, Deaths = 7048, updated = '01-04-2021' WHERE StateName = 'Mississippi'""")
        details = csr.fetchall()
        return jsonify({'success':'Data Updated'})

# to update the place, run the command in the new window in terminal:-
# curl -i -H "content-Type: application/json" -X PUT -d details http://<paste the public DNS>:5000/covidUScases


#this function delets a perticular data in database
@app.route('/covidUScases', methods=['DELETE'])
def delete_State():
        csr = conet.cursor()
        csr.execute("""DELETE FROM Country_Cases.United_States WHERE StateName='Alaska'""")
        details = csr.fetchall()
        return jsonify({'Success':'Data Deleted'}), 200

#to delete the place, run the command in the terminal:-
#curl -X "DELETE" http://<paste the public DNS>:5000/covidUScases


if __name__=="__main__":
    app.run(host='0.0.0.0')
