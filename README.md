# Reddit Weekly

## A small application that sends you a weekly digest of your fav subreddits

### How to run

First, install the requirements.

`pip install -r requirements.txt`

After installation, set following environment variables. 

`CLIENT_ID` = This is your `client_id` for your reddit application.

`CLIENT_SECRET` = This is your `client_secret` for your reddit application.

`USER_AGENT` = This is the unique user agent that reddit requires for each app.

`EMAIL` = The email address where you want to receive the message.

`MAILGUN_URL` = The URL for your Mailgun account. 

`MAILGUN_KEY` = Your API key from Mailgun.

`MAILGUN_FROM` = The from address you want displayed on the email.
