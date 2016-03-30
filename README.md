# tfa_prototype

## Setup:

1. Clone this project and cd into project directory.
2. Confirm what version of python you have installed (run the command `python --version`); if not 3.4, download python3 from python.org
3. Create python virtualenvironment:
  1. cd into project directory and run:
`virtualenv -p /usr/local/bin/python3 env`
  2. this creates the projects virtual environment in a folder called 'env'
4. Activate the environment by running `source env/bin/activate` at the same level as your env directory
5. Install project requirements by running `pip install -r requirements.txt`
6. Start the django server by running `python manage.py runserver`

## Testing TFA behavior

With your django server running, visit `localhost:8000/books/` a view that will show a list of books but which specifically requires two-factor auth signin.

### Testing one-time-use tokens with Google Authenticator (or another QR code-based token generator)
When prompted to do so, login with username: test_otp and password: password.

Select the option to setup Token Generator.
<insert image here>

You'll see a QR code like this
<insert image here>

Scan the code with an app like Google Authenticator to link your account with the app and enter the 6-digit token that should show up on the screen.

Once setup is completed, visit /logout to log the user out, then attempt to visit /books/ to prompt a login.

After entering the username and password it will prompt you for the token from your token generator.
<insert image here>

You should see a list of books!

### Testing SMS code authentication
When prompted to do so, login with username: test_sms and password: password.

Select the option to setup authentication with Text message.

Enter your phone number (include the +1 country code).

A fake SMS backend is setup in the project, codes will be logged to the output viewable in the shell where you ran `python manage.py runserver`.

To confirm behavior, visit /logout, attemtp to visit /books/ and complete the login process as the sms user.
