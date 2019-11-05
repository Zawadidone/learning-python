from requests import get
from json import loads
from sqlite3 import connect
from flask import Flask, request, render_template, flash
from wtforms import validators, SubmitField, StringField
from flask_wtf import FlaskForm


db = "db-stations.sqlite3"
api_token = ""
api_url_base = 'https://gateway.apiportal.ns.nl'
headers = {
    'Ocp-Apim-Subscription-Key': api_token,
}

app = Flask(__name__)
app.secret_key = "SECRET_KEY"


class NSForm(FlaskForm):
    """
    Station FlaksForum
    """
    station = StringField("Station name", [validators.DataRequired()], render_kw={"placeholder": "Enter station"})
    submit = SubmitField("Search")


def ns_api_call(host, request_uri, header, station_code):
    """
    This function makes API calls to the NS API portal to send back the travel times of stations in the Netherlands
    :param (str) host: the host of the API server
    :param (str) request_uri: the request uri of the HTTP request
    :param (dict) header: the header of the HTTP request (contains the API token)
    :param (code) station_code: the NS station code of the station name
    :return (dict) or (NoneType): the JSON response of the NS API or None if the API is not working
    """

    params = {
        'maxJourneys': '20',
        'lang': 'en',
        'station': station_code,
    }

    # Because the API can sometimes fall, 5 attempts are made
    for i in range(0, 5):
        response = get(host + request_uri, params=params, headers=header)
        if response.status_code == 200:  # if status is 200 return API response
            response_api = loads(response._content)
            return response_api
    return None


def select_station(conn, station_name):
    """
    This function executes a SQL statement to a SQLite3 database which provides station code base on a station name
    :param (class) conn: SQLite3 connection object
    :param (str) station_name: station name
    :return (tuple) or (NoneType): the station code of the station name or a NoneType if the database is not working
    """
    try:
        c = conn.cursor()
        c.execute(f"SELECT code FROM stations WHERE name = '{station_name}' COLLATE NOCASE LIMIT 1")

        row = c.fetchone()
        return row[0]
    except Exception as e:
        return None


@app.route('/', methods=['GET', 'POST'])
def main():
    """
    This function is responsible for the main flask view '/', it accepts GET/POST requests.
    :return (str) or (NoneType): the page in a string or NoneType, because the flash function doesn't returns a value
    """
    form = NSForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        conn = connect(db)
        result_form = request.form['station']
        station_code = select_station(conn, result_form)
        conn.close()
        if station_code:
            departures = ns_api_call(api_url_base, "/reisinformatie-api/api/v2/departures", headers, station_code)
            if departures:
                return render_template("index.html", form=form, departures=departures['payload']['departures'])
            else:
                flash(message="De NS API is slow, try again ...")
        else:
            flash("The station doesn't exist")
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
