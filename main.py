from flask import Flask, request, redirect, render_template
import validate

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        username = ''
        email = ''
        password = ''
        verify = ''

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        if username:
             return render_template('welcome.html', title="Welcome, " + username,
                username=username)

    return render_template('signup_form.html', title="User Signup",
        username=username, email=email)

app.run()
