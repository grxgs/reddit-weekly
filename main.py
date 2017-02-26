import pprint
import praw
import calculateSubreddit as cs
import mailgun as mg
import os

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
user_agent = os.environ['USER_AGENT']
email = os.environ['EMAIL']

# subreddits we want information on
subreddits = ['python', 'arduino', 'raspberry_pi', 'programming', 
                'entrepreneur', 'learnpython', 'learnprogramming', 
                'coding', 'commandline', 'webdev']


# Create our reddit client
reddit = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent)

message = ""

for sr in subreddits:
    submissions = []
    print("Getting submissions for " + sr + "." + "\n")
    subreddit = reddit.subreddit(sr)
    for sub in subreddit.top('week'):
        entries = {}
        entries['title'] = sub.title
        entries['url'] = sub.url
        entries['num_of_comments'] = sub.num_comments
        entries['score'] = sub.score
        entries['subreddit'] = subreddit.display_name
        submissions.append(entries)

    topComments = cs.mostComments(submissions)
    topPosts = cs.topTen(submissions)

    # print("These are the top 10 commented posts for " + sr + "\n")
    message += "\n" + "\n" + "Top 10 Commented Posts for " + sr + "\n" + "\n"
    for i in range(0, 11):
        title = topComments[i]['title']
        score = str(topComments[i]['score'])
        subreddit_name = topComments[i]['subreddit']
        comments = str(topComments[i]['num_of_comments'])
        url = topComments[i]['url']

        message += "Title: " + title + "\n"
        message += "URL: " + url + "\n"
        message += "Score: " + score + "\t" + "Comments: " + comments + "\n" + "\n"

    # since cs.topTen will always only return 10 results
    # we can just interate over the returned list
    #print("These are the top 10 upvoted posts for" + sr + "\n")
    message += "Top 10 Upvoted Posts for " + sr + "\n" + "\n"
    for post in topPosts:
        title = post['title']
        score = str(post['score'])
        comments = str(post['num_of_comments'])
        url = post['url']
        message += "Title: " + title + "\n"
        message += "URL: " + url + "\n"
        message += "Score: " + score + "\t" + "Comments: " + comments + "\n" + "\n"

mg.sendMessage(email, message)
