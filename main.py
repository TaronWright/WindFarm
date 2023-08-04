from flask import Flask
from flask import render_template
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
import csv
import folium


app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("Windfarm_Data_LongLat.csv")
    df_dict = df.to_dict(orient="records")
    return render_template("index.html", windfarms = df_dict)

@app.route("/map")
def map():
    m = folium.Map()
    m.save("venv/templates/footprint.html")
    return render_template("footprint.html")