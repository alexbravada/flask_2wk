from flask import Flask, render_template
import data


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    print('здесь будет главная')
    return render_template('index.html', departure=data.departures)


@app.route('/departures/<departure>/')
def render_departures(departure):
    print('здесь будет направление')
    return render_template('departure.html')


@app.route('/tours/<tour_id>/')
def render_tours(tour_id):
    print('здесь будет тур')
    return render_template('tour.html')


@app.route('/data/')
def print_all_tours():
    print(data.tours.values())
    return render_template('data.html', data=data.tours)


@app.route('/data/departures/<departure_name>/')
def print_departure_tours(departure_name):
    # departure_name=departure_name
    # if value['departure']==departure_name
    data_dep = {k : d for k, d in data.tours.items() if d['departure'] == departure_name}
    return render_template('data_departure.html', data=data_dep)


@app.route('/data/tours/<tour_id>/')
def print_tour_id(tour_id):
    return render_template('data_tours.html', data=data.tours, tour_id=int(tour_id))


@app.errorhandler(404)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error), 404

app.run(debug=True)