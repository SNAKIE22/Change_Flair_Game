import random


class Game:
    def __init__(self):
        self.user = ""
        self.read_users()
        self.read_trigger_times()

    def play(self, trigger, reply, reddit, subreddit, flair_css_dic):
        """ trigger= trigger words list,
        reply= reply words list,
        reddit= PRAW OAuth information,
        subreddit = particular subreddit to play the game,
        flair_css_dic= {reply word: flair_css_class}"""
        sub = reddit.subreddit(subreddit)
        for comment in sub.stream.comments():
            contents = comment.body
            for item in trigger:
                if item in contents.lower():
                    # mathing succeeded
                    print(f"Matching content: {contents}......")
                    self.update_trigger_times()
                    author = comment.author
                    self.user = author.name
                    # check if the user played before
                    if self.user not in self.replied_users:
                        reply_content = f'{random.choice(reply)}'
                        # change flair according to the reply
                        sub.flair.set(self.user, css_class=flair_css_dic[reply_content])
                        # return comment to the author
                        comment.reply(
                            body=f"恭喜,可爱的{self.user},您已经成为 {reply_content} 的一员,已为您颁发学院flair! ")
                        print(f"已为 {self.user} 颁发 {reply_content} 学院flair! ")
                        self.update_succeed_users()
                        self.read_users()
                    else:  # user has been assigned flair before
                        comment.reply(body="你在召唤我吗？每个人只有一次机会哦！")
                        print("no no , not again")  # feed back

    def read_users(self):
        with open("users_name.txt", mode="r") as file:
            self.replied_users = file.read()

    def read_trigger_times(self):
        with open("trigger_times.txt", mode="r") as file:
            self.game_triggered_times = int(file.read())

    def update_succeed_users(self):
        with open("users_name.txt", mode="a") as file:
            file.write(f"\n{self.user}")

    def update_trigger_times(self):
        self.game_triggered_times += 1
        with open("trigger_times.txt", mode="w") as file:
            file.write(str(self.game_triggered_times))

