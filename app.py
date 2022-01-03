from flask import Flask, jsonify

app = Flask(__name__)

gdp = {
    "2019": 19.092,
    "2018": 18.688,
    "2017": 18.144,
    "2016": 17.731,
    "2015": 17.432,
    "2014": 16.912,
    "2013": 16.495,
    "2012": 16.197,
    "2011": 15.841,
    "2010": 15.599 
}

debt = {
    "2019": 22.719,
    "2018": 21.516,
    "2017": 20.245,
    "2016": 19.573,
    "2015": 18.151,
    "2014": 17.824,
    "2013": 16.738,
    "2012": 16.066,
    "2011": 14.790,
    "2010": 13.562 
}

def get_econ(year):
    result = [] 

    econs = {
        "year": year,
        "gdp": gdp[year],
        "debt": debt[year]
    }

    result.append(econs)

    return result

@app.route("/")
def index():
    return "Welcome to the Econ API."

@app.route("/econ/<year>")
def econ_route(year):
    result = jsonify(get_econ(year))
    return result

if __name__ == "__main__":
    app.run()
