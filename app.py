from flask import Flask, render_template, session, request, url_for, make_response, redirect, jsonify
from validation import validator as val
from security import hashing as hashing
from data import data_handler as data
from data import api_connection as api
from utility import utility as util
from os import environ

app = Flask(__name__)

app.secret_key = environ.get('SECRET_KEY')


@app.route('/planets/page/<int:page>', methods=['GET'])
@app.route('/planets/', methods=['GET'])
def route_planets(page=1):  # show_planets v planets_view
    username = session.get('username', None)
    error_message = session.pop('error_message', None)
    planets = api.get_planets(page)
    util.format_big_numbers(planets['results'])
    next_page = api.get_page_nr(planets.get('next', None))
    previous_page = api.get_page_nr(planets.get('previous', None))
    return render_template('index.html',
                           username=username,
                           error_message=error_message,
                           planets=planets,
                           headers=api.planets_header,
                           next_page=next_page,
                           previous_page=previous_page,
                           )


@app.route('/', methods=['GET'])
def route_index():
    return redirect('planets/page/1')


@app.route('/login', methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not val.is_login_data_valid(username, password):
            session['error_message'] = "Username or password are not valid"
        else:
            if not data.check_user_existence(username):
                session['error_message'] = "User does not exist"
                return redirect(url_for('route_index'))
            hashed_password = data.get_user_password(username)
            if hashing.verify_password(password, hashed_password):
                session['username'] = username
            else:
                session['error_message'] = "Username and password does not match"
    return redirect(url_for('route_index'))


@app.route('/logout')
def route_logout():
    session.pop('username', None)
    return redirect(url_for('route_index'))


@app.route('/registration', methods=['POST'])
def route_registration():
    username = request.form['username']
    plain_text_password = request.form['password']

    if not val.is_login_data_valid(username, plain_text_password):
        session['error_message'] = "Username or password are not valid"
        return redirect(url_for('route_index'))
    hashed_password = hashing.hash_password(plain_text_password)
    try:
        data.save_new_user(username, hashed_password)
    except Exception as e:
        print(e)
        session['error_message'] = "Creating new user has failed"
    return redirect(url_for('route_index'))


@app.route('/vote', methods=['POST'])
def save_vote():
    print(request.form)
    planet_id = request.form.get('planet_id')
    planet_name = request.form.get('planet_name')
    data.save_vote(planet_id, planet_name, 2)
    return make_response(jsonify(request.form))


if __name__ == '__main__':
    app.run(debug=True)
