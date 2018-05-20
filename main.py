import praw
import os
import configparser
config = configparser.ConfigParser()
config.read('auth.ini') #All my usernames and passwords for the api

reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent=config.get('auth', 'reddit_user_agent'),
                     username=config.get('auth', 'reddit_username'))

print("Posting as: ", reddit.user.me())
SUBREDDIT = config.get('auth', 'reddit_subreddit')
LIMIT = config.get('auth', 'reddit_limit')

#If the call_all_posts text file dosn't exist, create it and initilize the enpty list.
if not os.path.isfile("turf_replys.txt"):
    turf_replys = []
#If the file does exist import the contents into a list
else:
    with open("turf_replys.txt", "r") as f:
        turf_replys = f.read()
        turf_replys = turf_replys.split("\n")
        turf_replys = list(filter(None, turf_replys))
bot_list = ['agree-with-you', 'Defiantly_Not_A_Bot', 'CommonMisspellingBot', 'WhoaItsAFactorial', 'FatFingerHelperBot', ' anti-gif-bot', 'LimbRetrieval-Bot']
turf_copy_pasta = "First, take a big step back... And literally, F-CK YOUR OWN FACE! I don't know what kind of pan-pacific bullshit power play you're trying to pull here, but r/StarVStheForcesofEvil is my territory. So whatever you're thinking, you'd better think again! Otherwise I'm gonna have to head down there and I will rain down in a Godly f-cking firestorm upon you! You're gonna have to call the f-cking United Nations and get a f-cking binding resolution to keep me from f-cking destroying you. I'm talking about a scorched earth, motherf-cker! I will massacre you! I WILL f-ck YOU UP!"
def reply_bot(debug=False):
    subreddit = reddit.subreddit(SUBREDDIT)
    comment_stream = subreddit.stream.comments()
    for comment in comment_stream:
        if comment.author in bot_list and comment.id not in turf_replys:
            comment.reply(turf_copy_pasta)
            if debug == True:
                print('Comment Replied to: ' + str(comment.id))
            turf_replys.append(comment.id)


def update_files(turf_replys):
    with open("turf_replys.txt", "w") as f:
        for x in turf_replys:
            f.write(x + "\n")
try:
    while True:
        reply_bot(True)
except KeyboardInterrupt:
    update_files(turf_replys)
    print('Interrupted')
