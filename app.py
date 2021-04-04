from flask import Flask, render_template
import data
from random import random, choice, sample

app = Flask(__name__)
app.debug = False

@app.route('/')
def index():
    random_keys = sample(list(data.tours), 6)
    six_tours = {}
    for k in random_keys:
        six_tours[k] = data.tours[k]    # creates new random dict with 6 unic dictionaries
    return render_template('index.html', six_tours=six_tours, departures=data.departures)


@app.route('/departures/<departure_name>/')
def render_departures(departure_name):
    napravlenie = data.departures[departure_name] # Выводит направление Из city_name по ключу
    price_list = []
    nights_list =[]
    hotels_dep = {k: d for k, d in data.tours.items() if d['departure'] == departure_name and d['price'] != 0}
    count_hotels = len(hotels_dep)
    for key, value in hotels_dep.items():
        price_list.append(int(value['price']))
        nights_list.append(int(value['nights']))
    min_nights = min(nights_list)
    max_nights = max(nights_list)
    min_price = min(price_list)
    max_price = max(price_list)
    return render_template('departure.html', hotels_dep=hotels_dep, departures=data.departures,
                           departure_name=departure_name, napravlenie=napravlenie, count_hotels=count_hotels,
                           min_nights=min_nights, max_nights=max_nights, min_price=min_price, max_price=max_price)


@app.route('/tours/<tour_id>/')
def render_tours(tour_id):
    show_tour = data.tours[int(tour_id)]
    return render_template('tour.html', show_tour=show_tour, departures=data.departures)


# @app.route('/data/')
# def print_all_tours():
#     print(data.tours.values())
#     return render_template('data.html', data=data.tours)


# @app.route('/data/departures/<departure_name>/')
# def print_departure_tours(departure_name):
#     # departure_name=departure_name
#     # if value['departure']==departure_name
#     data_dep = {k : d for k, d in data.tours.items() if d['departure'] == departure_name}
#     return render_template('data_departure.html', data=data_dep)


# @app.route('/data/tours/<tour_id>/')
# def print_tour_id(tour_id):
#     return render_template('data_tours.html', data=data.tours, tour_id=int(tour_id))


@app.errorhandler(404)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error), 404
    #return render_template('index.html')
    #return index()
    #except KeyError:
        #return flask.abort(404)

app.run(debug=False)