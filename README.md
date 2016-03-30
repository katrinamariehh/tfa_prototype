# tfa_prototype

This app is a proof-of-concept implementation of the Django Two-Factor Authentication library.  It uses Django 1.7.11 and Python 3.4.4.

***

# Running this project

## Setup

1. Clone this project and cd into project directory.
2. Confirm what version of python you have installed (run the command `python --version`); if not 3.4, download python3 from python.org
3. Create the python virtualenvironment by running `virtualenv -p /usr/local/bin/python3 env` in your project directory
4. Activate the environment by running `source env/bin/activate` at the same level as the env directory created by the above command
5. Install project requirements by running `pip install -r requirements.txt`
6. Start the django server by running `python manage.py runserver`

***

## Testing TFA behavior

With your django server running, visit `localhost:8000/books/` a view that will show a list of books but which specifically requires two-factor auth signin.

### Testing one-time-use tokens with Google Authenticator (or another QR code-based token generator)
When prompted to do so, login with username: test_otp and password: password.

You should see a message that you need to enable two-factor authentication.

![two-factor auth message](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/permission_denied.png)

Next you will get a prompt to start the two-factor auth setup wizard.

![begin wizard](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/begin_wizard.png)

Select the option to setup a Token generator.

![select token generator](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/select_token_generator.png)

You'll see a QR code to scan with an app like Google Authenticator, this will link your account with the app.  When prompted, enter the 6-digit token that should show up in your app.

Once setup is completed, visit /logout to log the user out, then attempt to visit /books/ to prompt a login.

After entering the username and password it will prompt you for the token from your token generator.

![enter token](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/enter_token_from_generator.png)

You should see a list of books!

### Testing SMS code authentication
When prompted to do so, login with username: test_sms and password: password.

Select the option to setup authentication with Text message.

![select text message](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/select_text_message.png)

Enter your phone number (include the +1 country code).

![enter phone number] (https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/enter_phone_number.png)

A fake SMS backend is setup in the project, codes will be logged to the output viewable in the shell where you ran `python manage.py runserver`.

![log output](https://raw.githubusercontent.com/katrinamariehh/tfa_prototype/master/screenshots/log_output.png)

After entering your phone number it will prompt you to enter the code logged in the server shell.

To confirm behavior, visit /logout, attempt to visit /books/ and complete the login process as the test_sms user.


# Continued work and testing

Right now I am only using two options for two-factor authentication (text message or token generator) and I did not build out the project to send actual text messages.  The Django Two-Factor Authentication project has settings for using Twilio for text messages and phone calls for authentication as well as setup documentation for [Yubikeys](https://www.yubico.com/products/yubikey-hardware/yubikey4/).  

Additionally, I'm using the built-in Django user authentication backend so it is only setup to allow users to log in to the django admin site; this means that any additional users created to test with must be created as staff users.  To access the admin to make more users run the `python manage.py createsuperuser` command in your project and follow the instructions to make a new superuser.  You shoudl be able to login as that user at /admin.  Once you are logged in, admin tool easily lets you create users by selecting Add next to Users under the Authentication and Authorization heading.  Make sure to mark any new users as staff users or the login process will not work properly.
