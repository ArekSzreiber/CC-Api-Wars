from flask import Flask, render_template, session, escape, request, url_for, redirect
from validation import validator as val
from security import hashing as hashing
from data import data_handler as data

app = Flask(__name__)

app.secret_key = b'\x12\x06\x97O\x8aaw\xadW\x18\xa7\x08%n\x7f\x1a_\xb6\xe03\xf3\xe4\x9f'

@app.route('/', methods=['GET'])
def route_index():
    print(session.get('error_message'))
    username = session.get('username')
    error_message = session.get('error_message', None)
    session.pop('error_message', None)
    return render_template('index.html',
                           username=username,
                           error_message=error_message)



@app.route('/login', methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        # wez z formularza login i haslo
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



if __name__ == '__main__':
    app.run(debug=True,
            port=1234)
