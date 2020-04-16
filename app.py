from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

#like example in class
app= Flask(__name__)

app.config["MONGO_URI"]= 'mongodb://localhost:27017/mars_app'
mongo= PyMongo(app)



client= pymongo.MongoClient(conn)

@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars= mongo.db.mars
    mars_data= scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)
