from random import sample

import data

import flask

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    random_keys = sample(list(data.tours), 6)
    six_tours = {}
    for k in random_keys:
        six_tours[k] = data.tours[k]    # creates new random dict with 6 unical dictionaries
    return render_template('index.html',
                           six_tours=six_tours,
                           departures=data.departures,
                           data=data)


@app.route('/departures/<departure_name>/')
def render_departures(departure_name):
    try:
        str(departure_name) not in data.departures.keys()
    except KeyError:
        return flask.abort(404)
    departure = data.departures[departure_name]  # Выводит направление Из city_name по ключу
    price_list = []
    nights_list = []
    tours_dep = {tour_id: values for tour_id, values in data.tours.items() if values['departure'] == departure_name}
    count_tours = len(tours_dep)
    for key, value in tours_dep.items():
        price_list.append(int(value['price']))
        nights_list.append(int(value['nights']))
    min_nights = min(nights_list)
    max_nights = max(nights_list)
    min_price = min(price_list)
    max_price = max(price_list)
    return render_template('departure.html',
                           tours_dep=tours_dep,
                           data=data,
                           departures=data.departures,
                           departure=departure,
                           departure_name=departure_name,
                           count_tours=count_tours,
                           min_nights=min_nights,
                           max_nights=max_nights,
                           min_price=min_price,
                           max_price=max_price)


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id):
    show_tour = data.tours.get(tour_id)
    if show_tour is None:
        return flask.abort(404)
    return render_template('tour.html',
                           show_tour=show_tour,
                           departures=data.departures,
                           data=data)


@app.errorhandler(404)
@app.errorhandler(KeyError)
def render_server_error(error):
    return "Что-то не так, такой страницы нет, попробуй другое:\n{}".format(error), 404


if __name__ == '__main__':
    app.run(debug=False)
