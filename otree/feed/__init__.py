from otree.api import *
import datetime
import pandas as pd
import numpy as np
import itertools


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'feed'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    RULES_TEMPLATE = "feed/T_Rules.html"
    PRIVACY_TEMPLATE = "feed/T_Privacy.html"
    TWEET_TEMPLATE = "feed/T_Tweet.html"
    ATTENTION_TEMPLATE = "feed/T_Attention_Check.html"
    TOPICS_TEMPLATE = "feed/T_Trending_Topics.html"
    PAPERCUPS_TEMPLATE = __name__ + '/T_PAPERCUPS.html'

    FEED_LENGTH = list(range(*{'start':0,'stop':41,'step':1}.values()))
    TWEET_LENGTH = list(range(*{'start':0,'stop':41,'step':1}.values()))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField(doc='indicates the treatment a player is randomly assigned to')
    privacy_time = models.FloatField(doc="counts the number of seconds the privacy statement was opened", blank=True)
    liked_item_attention = models.BooleanField(doc="indicates whether a participant passes the attention check", blank=True)

    mc_1 = models.IntegerField(
        label="Estrava is internationally recognized as a leading global luxury fashion brand.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    mc_2 = models.IntegerField(
        label="I imagine myself to spend some spare time checking out Estrava's recent Twitter feed. ",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    # create like count fields
    for i in C.FEED_LENGTH:
        locals()['liked_item_' + str(i)] = models.BooleanField(initial=False, blank=True)
    del i

    # create reply text fields
    for i in C.FEED_LENGTH:
        locals()['reply_to_item_' + str(i)] = models.LongStringField(blank=True)
    del i

    # # create affective fields
    # for i in C.TWEET_LENGTH:
    #     locals()['affective' + str(i)] = models.IntegerField(
    #         label=str(i),
    #         doc="Affective".format(i),
    #         widget=widgets.RadioSelect,
    #         choices=[1, 2, 3, 4, 5, 6, 7],
    #         blank=False
    #     )
    # del i
    #
    # # create fashion relatedness fields
    # for i in C.TWEET_LENGTH:
    #     locals()['fashion' + str(i)] = models.IntegerField(
    #         label=str(i),
    #         doc="Fashion-related".format(i),
    #         widget=widgets.RadioSelect,
    #         choices=[1, 2, 3, 4, 5, 6, 7],
    #         blank=False
    #     )
    # del i
    #
    # # create urgency fields
    # for i in C.TWEET_LENGTH:
    #     locals()['urgent' + str(i)] = models.IntegerField(
    #         label=str(i),
    #         doc="urgent".format(i),
    #         widget=widgets.RadioSelect,
    #         choices=[1, 2, 3, 4, 5, 6, 7],
    #         blank=False
    #     )
    # del i
    #
    # # create financial fields
    # for i in C.TWEET_LENGTH:
    #     locals()['financial' + str(i)] = models.IntegerField(
    #         label=str(i),
    #         doc="financial".format(i),
    #         widget=widgets.RadioSelect,
    #         choices=[1, 2, 3, 4, 5, 6, 7],
    #         blank=False
    #     )
    # del i



# FUNCTIONS -----
def creating_session(subsession):
    shuffle = itertools.cycle(['clean', 'polluted'])
    for player in subsession.get_players():
        player.treatment = next(shuffle)


# PAGES
class A_Intro(Page):
    form_model = "player"
    form_fields = ["privacy_time"]


class B_Instructions(Page):
    form_model = "player"
    form_fields = ["mc_1", "mc_2"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        # read data
        # fashion = pd.read_csv('feed/static/tweets/brands_tweets.csv', sep=';')
        fashion = pd.read_csv('feed/static/tweets/zegna_tweets.csv', sep=';')
        web3 = pd.read_csv('feed/static/tweets/spam_tweets.csv', sep=';')

        # shuffle
        if player.treatment == 'clean':
            fashion = fashion.sample(frac=1)
            web3 = web3.sample(frac=0.25)
        else:
            fashion = fashion.sample(frac=0.25)
            web3 = web3.sample(frac=1)

        # rbind and shuffle again
        tweets = pd.concat([fashion, web3]).reset_index(drop=True)
        tweets = tweets.sample(frac=1)

        # create ID
        tweets['index'] = range(1, len(tweets) + 1)

        # reformat date
        tweets['datetime'] = pd.to_datetime(tweets['datetime'], errors='coerce')
        tweets.date = tweets['datetime'].dt.strftime('%d %b').str.replace(' ', '. ')
        tweets['date'] = tweets['date'].str.replace('^0', '', regex=True)

        # highlight hashtags, cashtags, mentions, etc.
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\#[a-zA-Z0-9_]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex=True)
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\$[a-zA-Z0-9_\.]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex=True)
        tweets['tweet'] = tweets['tweet'].str.replace(r'\B(\@[a-zA-Z0-9_]+\b)',
                                                      r'<span class="text-primary">\g<0></span>', regex=True)
        # remove the href below, if you don't want them to leave your page
        tweets['tweet'] = tweets['tweet'].str.replace(
            r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])',
            # r'<a class="text-primary" href="\g<0>" target="_blank">\g<0></a>', regex=True)
            r'<a class="text-primary">\g<0></a>', regex=True)

        # make numeric information integers and fill NAs with 0
        tweets['replies'] = tweets['replies'].fillna(0).astype(int)
        tweets['retweets'] = tweets['retweets'].fillna(0).astype(int)
        tweets['likes'] = tweets['likes'].fillna(0).astype(int)

        # make pictures (if any) visible
        tweets['media'] = tweets['media'].str.replace("[", '')
        tweets['media'] = tweets['media'].str.replace("'", '')
        tweets['media'] = tweets['media'].str.replace("]", '')
        tweets['media'] = tweets['media'].str.replace("and.*", '')
        tweets['media'] = tweets['media'].fillna('')
        tweets['pic_available'] = np.where(tweets['media'].str.match(pat='http'), True, False)

        # make profile pictures (if any) visible
        tweets['profile_pic_available'] = np.where(tweets['user_image'].isnull(), False, True)


        # create a name icon as a profile pic
        tweets['icon'] = tweets['username'].str[:2]
        tweets['icon'] = tweets['icon'].str.title()

        tweets['user_followers'] = tweets['user_followers'].map('{:,.0f}'.format).str.replace(',', '.')

        # create form field stuff
        # tweets['fashion']   = 'fashion' + tweets['doc'].astype(str)
        # tweets['affective'] = 'affective' + tweets['doc'].astype(str)
        # tweets['urgent']    = 'urgent' + tweets['doc'].astype(str)
        # tweets['financial']    = 'financial' + tweets['doc'].astype(str)

        # create row ID
        tweets['row'] = range(1, len(tweets) + 1)

        # create description column for illustrativ purposes
        # tweets[
        #     'description'] = "Hi, this is the author's profile information which needs to be populated with real information."
        player.participant.tweets = tweets

class C_Tweets(Page):
    form_model = "player"
    form_fields = ['attention_check']

    @staticmethod
    def get_form_fields(player: Player):
        items = player.participant.tweets['doc'].values.tolist()
        items.insert(0, 0)
        return ['fashion' + str(n) for n in items] + \
               ['affective' + str(n) for n in items] + \
               ['urgent' + str(n) for n in items] + \
               ['financial' + str(n) for n in items]

    @staticmethod
    def vars_for_template(player: Player):
        temp = player.participant.tweets.to_dict('index')
        return dict(
            tweets=temp,
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            rows=len(player.participant.tweets)
        )


class C_Feed(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        items = player.participant.tweets['doc_id'].values.tolist()
        items.insert(0, 0)
        return ['liked_item_' + str(n) for n in items] + \
               ['reply_to_item_' + str(n) for n in items]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            tweets=player.participant.tweets.to_dict('index'),
        )

page_sequence = [A_Intro, B_Instructions,
                C_Feed]
