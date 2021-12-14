from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./Hotels.json').read())
data=jData["Hotels"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "RESTful Webservice Started. Request data with proper URL"

# Returns JSON which containes all hotels
@app.route('/gethotels/')
def hotels_all():
    return render_template("index.html",items=data)

# Returns hotels JSON which matches the id
@app.route('/gethotel/<string:id>/')
def hotels_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the hotels JSON with particualr food type
@app.route('/gethotel/type/<int:rating>/')
def hotels_by_type(rating=''):
    myList=[]
    for elements in data:
        if elements["rating"]== rating:
            myList.append(elements)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True)