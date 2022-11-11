from otree.api import *
import datetime
import pandas as pd
import numpy as np

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'feed'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Tweets(Page):
    @staticmethod
    def vars_for_template(player: Player):
        tweets = pd.read_csv('feed/static/tweets/randomsample.csv',
                             sep = ';',
                             nrows = 25)

        # reformat date
        tweets['created_at'] = pd.to_datetime(tweets['created_at'], errors='coerce')
        tweets.date = tweets['created_at'].dt.strftime('%d %b')
        tweets['date'] = tweets['date'].str.replace('^0', '', regex = True)

        # highligh hashtags, cashtags, mentions, etc.
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\#[a-zA-Z_]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex = True)
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\$[a-zA-Z_]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex = True)
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\@[a-zA-Z_]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex = True)
        tweets['tweet'] = tweets['tweet'].str.replace(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])',
                                                      r'<span class="text-primary">\g<0></span>', regex = True)

        # make numeric information integers and fill NAs with 0
        tweets['replies_count'] = tweets['replies_count'].fillna(0).astype(int)
        tweets['retweets_count'] = tweets['retweets_count'].fillna(0).astype(int)
        tweets['likes_count'] = tweets['likes_count'].fillna(0).astype(int)

        # make pictures (if any) visible
        tweets['photos'] = tweets['photos'].str.replace("[", '')
        tweets['photos'] = tweets['photos'].str.replace("'", '')
        tweets['photos'] = tweets['photos'].str.replace("]", '')
        tweets['photos'] = tweets['photos'].fillna('')
        tweets['pic_available'] = np.where(tweets['photos'].str.match(pat = 'http'), True, False)

        # create a name icon as a profile pic
        tweets['icon'] = tweets['name'].str[:2]
        tweets['icon'] = tweets['icon'].str.title()

        # create description column for illustrativ purposes
        tweets['description'] = "Hi, this is the author's profile information which needs to be populated with real information."
        return dict(
            tweets=tweets.to_dict('index'),
        )

page_sequence = [Tweets]
