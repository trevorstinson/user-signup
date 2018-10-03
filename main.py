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

        username_error = ''
        email_error = ''
        password_error = ''
        verify_error = ''

        if validate.is_empty(username):
            username_error = "Please enter a username"
        if validate.is_empty(password):
            password_error = "Please enter a password"
        if validate.is_empty(verify):
            password_error = "Please enter and verify a password"
            verify_error = "Please verify your password"

        if username_error or email_error or password_error or verify_error:
            return render_template('signup_form.html', title = "User Signup",
                username = username, email = email,
                username_error = username_error,
                email_error = email_error,
                password_error = password_error,
                verify_error = verify_error)
        
        return render_template('welcome.html', title="Welcome, " + username,
                username=username)



    return render_template('signup_form.html', title="User Signup",
        username=username, email=email)

app.run()
