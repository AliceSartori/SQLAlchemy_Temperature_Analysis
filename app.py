import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
#
# # Save reference to the table. Class called passenger.
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h1> Alice Sartori Flask project routes</h1>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    date_precipitations = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date < '2017-08-23').filter(
    Measurement.date > '2016-08-24').order_by(Measurement.date).all()

    date= []
    prcp=[]
    for data_point in date_precipitations:
        date.append(data_point[0])
        prcp.append(data_point[1])

    dict2return={'date':date, 'prcp':prcp}
        
    return(jsonify(dict2return))

@app.route("/api/v1.0/station")
def station():
    stations=session.query(Measurement.station).all()
    unique_stations=set(stations)

    list_stations = []
    for station in unique_stations:
        list_stations.append(station[0])
    dict2return= {'stations':list_stations}
    return jsonify(dict2return)


@app.route("/api/v1.0/tobs")
def tobs():
    date_tobs = session.query(Measurement.date, Measurement.prcp, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date < '2017-08-23').filter(
    Measurement.date > '2016-08-24').order_by(Measurement.date).all()

    #dates and temperature
    date=[]
    temperature = []

    for data in date_tobs:
        date.append(data[0])
        temperature.append(data[2])

    #dictionary to return:
    dict2return={'date':date, 'temperature':temperature}

    return(jsonify(dict2return))


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>")
def start(start):
    print(start)
    date_interval = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
    func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    print(date_interval)
    #
    # print(date_interval)
    # TMIN= []
    # TAVG= []
    # TMAX=
    #
    for data in date_interval:
        TMIN = data[0]
        TAVG  = data[1]
        TMAX = data[2]
    # #
    # #dictionary to return:
    dict2return={'TMIN':TMIN, 'TAVG':TAVG, 'TMAX':TMAX}
    #
    return(jsonify(dict2return))



@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    print(start)
    date_interval = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
    func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    for data in date_interval:
        TMIN = data[0]
        TAVG  = data[1]
        TMAX = data[2]
    # #
    # #dictionary to return:
    dict2return={'TMIN':TMIN, 'TAVG':TAVG, 'TMAX':TMAX}
    #
    return(jsonify(dict2return))


if __name__ == '__main__':
    app.run(debug=True)
