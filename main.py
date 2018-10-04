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

        # Check for verify_error first
        # This allows other errors to override it so that
        # user doesn't waste time matching these two fields
        # before knowing the other password criteria
        if validate.is_empty(verify):
            password_error = "Please reenter your password"
            verify_error = "Please verify your password"
        if validate.does_not_match(password, verify):
            password_error = "Please reenter password"
            verify_error = "Verification must match"

        if validate.is_out_of_range(username):
            username_error = "Username must be 3-20 characters"
        if validate.is_out_of_range(password):
            password_error = "Password must be 3-20 characters"
            verify_error = ''

        if validate.contains_space(username):
            username_error = "Username cannot contain spaces"
        if validate.contains_space(password):
            password_error = "Password cannot contain spaces"

        if validate.is_empty(username):
            username_error = "Please enter a username"
        if validate.is_empty(password):
            password_error = "Please enter a password"

        if email:
            if validate.is_not_email(email):
                email_error = "Please use a valid email address"

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
