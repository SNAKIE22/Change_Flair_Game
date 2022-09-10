import praw

from flair_game import Game

reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
    username="",
    password=""
)

print(reddit.user.me())

subreddit = ""

trigger = ['cake']

reply = ['cat', 'dog', 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin', '麻瓜']

flair_css_dic = {
    "Gryffindor": "gryffindor",
    "Hufflepuff": "hufflepuff",
    "麻瓜": "muggle",
    "Ravenclaw": "ravenclaw",
    "Slytherin": "slytherin",
    "cat": "user1",
    "dog": "user2",

}

game = Game()


game.play(trigger, reply, reddit, subreddit, flair_css_dic)

