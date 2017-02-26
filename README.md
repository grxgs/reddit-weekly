# Reddit Weekly

## A small application that sends you a weekly digest of your fav subreddits

### How to run

#### Installation

First, install the requirements.

`pip install -r requirements.txt`

#### Configuration

After installation, set following environment variables. 

`CLIENT_ID` = This is your `client_id` for your reddit application.

`CLIENT_SECRET` = This is your `client_secret` for your reddit application.

`USER_AGENT` = This is the unique user agent that reddit requires for each app.

`EMAIL` = The email address where you want to receive the message.

`MAILGUN_URL` = The URL for your Mailgun account. 

`MAILGUN_KEY` = Your API key from Mailgun.

`MAILGUN_FROM` = The from address you want displayed on the email.

In the main.py file, there is a list called `subreddits`. Enter in the names 
of the subreddits that you want to receive the digest for. 

*Note:* The subreddit configuration will most likely move to a file in the future.

#### Running

To run the app, type in the following. 

`python3 main.py`

You should see message indicating which subreddit is being checked. Once complete, check your email. 
To get the most use out of this, I recommend adding it to your crontab on a server so you can 
customize when you want to receive these digests. 
