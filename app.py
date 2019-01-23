from flask import Flask, render_template, session, escape, request, url_for, redirect
from validation import validator as val
from security import hashing as hashing
from data import data_handler as data

app = Flask(__name__)

app.secret_key = b'\x12\x06\x97O\x8aaw\xadW\x18\xa7\x08%n\x7f\x1a_\xb6\xe03\xf3\xe4\x9f'

@app.route('/', methods=['GET'])
def route_index():
    username = session.get('username', False)
    return render_template('index.html', username=escape(username))

@app.route('/login', methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        session['username'] = request.form.get('username', None)
        return redirect(url_for('route_index'))
    else:
        return render_template('login.html', username=escape(session.get('username', False)))


@app.route('/logout')
def route_logout():
    session.pop('username', None)
    return redirect(url_for('route_index'))

@app.route('/registration', methods=['POST'])
def route_registration():
    username = request.form['username']
    plain_text_password = request.form['password']
    if not val.is_login_data_valid(username, plain_text_password):
        return redirect(url_for('route_index'))
    hashed_password = hashing.hash_password(plain_text_password)
    try:
        data.save_new_user(username, hashed_password)
    except Exception as e:
        print(e)
    # todo modal z info, że udało/nieudało się zarejestrować
    return redirect(url_for('route_index'))



if __name__ == '__main__':
    app.run(debug=True,
            port=1234)
