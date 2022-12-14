from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    QUESTIONNAIRE_TEMPLATE = "questionnaire/T_Questionnaire.html"
    PAPERCUPS_TEMPLATE = __name__ + '/T_PAPERCUPS.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completed_survey = models.BooleanField(doc="indicates whether a participant has completed the survey.",
                                           initial=False,
                                           blank=True)

# Brand Equity Bruner et al. 2012 p. 153
    brand_equity_1 = models.IntegerField(
        doc="What kind of attitude did you have about Estrava?",
        label="What kind of attitude did you have about Estrava?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False,
    )

    brand_equity_2 = models.IntegerField(
        doc="What kind of image did Estrava have?",
        label="What kind of image did Estrava have?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_equity_3 = models.IntegerField(
        doc="How would you rate the quality delivered by Estrava?",
        label="How would you rate the quality delivered by Estrava?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_equity_4 = models.IntegerField(
        doc="Would you have been willing to pay more for products from Estrava than for other companiesâ€™ products?",
        label="Would you have been willing to pay more for products from Estrava than for other companiesâ€™ products?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Brand Clarity Bruner et al. 2012 p. 159
    brand_clarity_1 = models.IntegerField(
        doc="To what extent do you think the characteristics of Estrava are coherent?",
        label="The characteristics of Estrava are coherent.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_clarity_2 = models.IntegerField(
        doc="To what extent do you view Estrava as an integrated brand?",
        label="Estrava is an integrated brand.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_clarity_3 = models.IntegerField(
        doc="To what extent does Estrava give you a concrete image about what this brand is like?",
        label="Estrava gives me a concrete image about what the brand is like.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_clarity_4 = models.IntegerField(
        doc="To what extent do you think it is easy to explain your impression of Estrava to other people?",
        label="It is easy to explain my impression of Estrava to other people.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    brand_clarity_5 = models.IntegerField(
        doc="To what extent do you easily categorize what Estrava is?",
        label="I easily categorize what Estrava is.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)


# Risk 1 Bruner et al. 2012 p. 159
    risk_1 = models.IntegerField(
        doc="Getting a product from Estrava is risky.",
        label="Getting a product from Estrava is risky.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    risk_2 = models.IntegerField(
        doc="A product from Estrava can lead to bad results.",
        label="A product from Estrava can lead to bad results.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    risk_3 = models.IntegerField(
        doc="A product from Estrava has uncertain results.",
        label="A product from Estrava has uncertain results.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    risk_4 = models.IntegerField(
        doc="Getting a product from Estrava makes me feel anxious.",
        label="Getting a product from Estrava makes me feel anxious.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    risk_5 = models.IntegerField(
        doc="Getting a product from Estrava would cause me to worry.",
        label="Getting a product from Estrava would cause me to worry.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Trustworthiness Bruner et al 2019 p. 471
# Using the items below, please describe Estrava.
    trust_1 = models.IntegerField(
        doc="Dishonest",
        label="Dishonest",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_2 = models.IntegerField(
        doc="Insincere",
        label="Insincere",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_3 = models.IntegerField(
        doc="Manipulative",
        label="Manipulative",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    trust_4 = models.IntegerField(
        doc="Not trustworthy",
        label="Not trustworthy",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Information pollution (close to Bruner et al. 2019 p.333)
    pollution_1 = models.IntegerField(
        doc="The feed contained too many items related to topics that are unrelated to fashion.",
        label="The feed contained too many items related to topics that are unrelated to fashion.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    pollution_2_r = models.IntegerField(
        doc="In the feed, the number of tweets related to fashion was too large.",
        label="In the feed, the number of tweets related to fashion was too large.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    pollution_3 = models.IntegerField(
        doc="In the feed, there was an overabundance of tweets unrelated to fashion.",
        label="In the feed, there was an overabundance of tweets unrelated to fashion.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Persuasivness Bruner et al. 2019 p. 302
# Estravas tweets were...

    persuasive_1 = models.IntegerField(
        doc="persuasive",
        label="Persuasive",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    persuasive_2 = models.IntegerField(
        doc="effective",
        label="Effective",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    persuasive_3 = models.IntegerField(
        doc="compelling",
        label="Compelling",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    persuasive_4 = models.IntegerField(
        doc="convincing",
        label="Convincing",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Prestige (Ko, Castello & Taylor 2019)
    prestige_1 = models.IntegerField(
        doc="Estrava is a symbol of prestige.",
        label="Estrava is a symbol of prestige.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    prestige_2 = models.IntegerField(
        doc="Estrava is a premium brand.",
        label="Estrava is a premium brand.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    prestige_3 = models.IntegerField(
        doc="Estrava is a high-end brand.",
        label="Estrava is a high-end brand.",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

# Interest in Web3
    NFT_ownership = models.BooleanField(
        label='Do you own an NFT?',
        choices=[
            [True, "Yes"],
            [False, "No"]
        ])

    web3_interest = models.BooleanField(
        label='Are you interested in Web3 (e.g. crypto currencies, NFTs, Metaverse)?',
        choices=[
            [True, "Yes"],
            [False, "No"]
        ])

# Interest in Fashion
    fashion_interest_1 = models.IntegerField(
        label='I am usually the first to know the latest fashion trends.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    fashion_interest_2 = models.IntegerField(
        label='I read the fashion news regularly and try to keep my wardrobe up-to-date with fashion trends.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    fashion_interest_3 = models.IntegerField(
        label='My friends regard me as a good source of fashion advice.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    fashion_interest_4 = models.IntegerField(
        label='I usually try to be different from others by wearing fashionable clothing.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)



# Demographics
    age = models.IntegerField(label="Please enter your age",
                              min=18,
                              max=99)

    gender = models.IntegerField(
        label="Please select your gender.",
        choices=[
            [1, "Female"],
            [2, "Male"],
            [3, "Diverse"],
        ]
    )

    education = models.IntegerField(
        label="What is the highest level of education you achieved?",
        choices=[
            [1, "Some high school"],
            [2, "High school diploma or G.E.D."],
            [3, "Some college"],
            [4, "Associate's degree"],
            [5, "Bachelor's degree"],
            [6, "Master's degree"],
            [7, "Other"],
            [8, "Doctorate"],
        ]
    )

    income = models.IntegerField(
        label="What is your total household income per year?",
        blank=True,
        choices=[
            [1, "Less than $10,000"],
            [2, "$10,000 to $19,999"],
            [3, "$20,000 to $34,999"],
            [4, "$35,000 to $49,999"],
            [5, "$50,000 to $74,999"],
            [6, "$75,000 to $99,999"],
            [7, "$100,000 to $149,999"],
            [8, "$150,000 or more"],
        ]
    )

# completed the survey
    completed_survey = models.BooleanField(
        doc="True as soon as participants submit Feedback page",
        initial=False,
        blank=True
    )

# PAGES
class Brand_Equity(Page):
    form_model = "player"
    form_fields = ["brand_equity_1", "brand_equity_2", "brand_equity_3", "brand_equity_4"]


class Brand_Clarity(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["brand_clarity_1", "brand_clarity_2", "brand_clarity_3", "brand_clarity_4", "brand_clarity_5"]
        random.shuffle(form_fields)
        return form_fields

class Risk(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["risk_1", "risk_2", "risk_3", "risk_4",
                       "risk_5"]
        random.shuffle(form_fields)
        return form_fields


class Trust(Page):
    form_model = "player"
    form_fields = ["trust_1", "trust_2", "trust_3", "trust_4"]


class Prestige(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["prestige_1", "prestige_2", "prestige_3"]
        random.shuffle(form_fields)
        return form_fields


class Persuasion(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["persuasive_1", "persuasive_2", "persuasive_3", "persuasive_4"]
        random.shuffle(form_fields)
        return form_fields


class Pollution(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["pollution_1", "pollution_2_r", "pollution_3"]
        random.shuffle(form_fields)
        return form_fields


class Web3(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["NFT_ownership", "web3_interest"]
        random.shuffle(form_fields)
        return form_fields


class Fashion(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["fashion_interest_1", "fashion_interest_2", "fashion_interest_3", "fashion_interest_4"]
        random.shuffle(form_fields)
        return form_fields


class Demographics(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "income"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.finished = True
        player.completed_survey = player.participant.finished

class Debriefing(Page):
    pass


page_sequence = [Brand_Equity, Brand_Clarity, Prestige, Trust, Risk, Persuasion, Pollution,
                 Fashion, Web3, Demographics, Debriefing]
