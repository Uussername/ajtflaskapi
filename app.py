#Code by Joe Axberg
#Commented by AJ Thompson
# updated 12/13/2020

#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#mongo database connection
app.config["MONGO_URI"] = "mongodb://192.168.0.75:27017/temperature"
mongo = PyMongo(app)

#pointing to html files
@app.route('/')
@app.route('/index/')
def index():
    #homepage
    return render_template('index.html')
#another page for a single temp
@app.route("/get_one_temp_api")
def temp1():
    #mongo query for 1 temp
    one_temp = mongo.db.temperature.find_one()
    #print(temp_reading)
    return str(one_temp)

#another page for 10 temperatures
@app.route("/get_ten_temps_api")
def temp10():
    temps = ""
    #mongo query for 10 temps
    ten_temps = mongo.db.temperature.find().limit(10)
    #loop to append temperatures to the string
    for temp in ten_temps:
        temps=temps+str(temp)
        print(temps)
    return temps

#final page for recent temps, up to 10
@app.route("/recent_temps")
def recent():
    #mongo query for 10 temps
    temps = mongo.db.temperature.find().limit(10)
    return render_template('temps.html',temps=temps)

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyonepy