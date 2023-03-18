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

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completed_survey = models.BooleanField(doc="indicates whether a participant has completed the survey.",
                                           initial=False,
                                           blank=True)

    # manipulation checks
    mc_3 = models.IntegerField(
        label="How many tweets other than Estrava do you think were present in the feed?",
        blank=True,
        choices=[
            [0, "0%"],
            [1, "10%"],
            [2, "20%"],
            [3, "30%"],
            [4, "40%"],
            [5, "50%"],
            [6, "60%"],
            [7, "70%"],
            [8, "80%"],
            [9, "90%"],
            [10, "100%"],
        ]
    )

    mc_4 = models.IntegerField(
        label="How many tweets other than Estrava did you notice in the feed?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    mc_5 = models.IntegerField(
        label="There was a tweet that depicted fruits. What fruits were they?",
        blank=True,
        choices=[
            [1, "Oranges"],
            [2, "Apples"],
            [3, "Lemons"],
            [4, "Bananas"],
        ]
    )

# Open Text Fields
    otf_1 = models.LongStringField(
        doc="What were the first thoughts and feelings that came to your mind when you were scrolling through the entire feed?",
        lable="What were the first thoughts and feelings that came to your mind when you were scrolling through the entire feed?",
        blank=False)

    otf_2 = models.LongStringField(
        doc="Please describe as detailed as you can your Twitter experience considering all tweets of the entire feed, given that you only wanted to find out Estrava’s recent updates. What did you like and dislike about your experience following the recent Estrava posts?",
        lable="Please describe as detailed as you can your Twitter experience considering all tweets of the entire feed, given that you only wanted to find out Estrava’s recent updates. What did you like and dislike about your experience following the recent Estrava posts?",
        blank=False)

# # Brand Contamination
#     brand_contamination_1_r = models.IntegerField(
#         label='Overall, scrolling through this feed reinforced my perception of Estrava as a luxury brand.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_contamination_2 = models.IntegerField(
#         label='The feed contained too many items related to topics that diminished the significance of Estrava.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_contamination_3_r = models.IntegerField(
#         label='Scrolling through this feed positively impacted my experience of Estrava.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_contamination_4 = models.IntegerField(
#         label='The feed lowered my perception of Estrava as there was an overabundance of tweets unrelated to it.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_contamination_5 = models.IntegerField(
#         label="Looking at the other's tweets lowered my perception of the luxury brand Estrava.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)

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

# # Information pollution (close to Bruner et al. 2019 p.333)
#     pollution_1 = models.IntegerField(
#         doc="The feed contained too many items related to topics that are unrelated to fashion.",
#         label="The feed contained too many items related to topics that are unrelated to fashion.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     pollution_2_r = models.IntegerField(
#         doc="In the feed, the number of tweets related to fashion was too large.",
#         label="In the feed, the number of tweets related to fashion was too large.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     pollution_3 = models.IntegerField(
#         doc="In the feed, there was an overabundance of tweets unrelated to fashion.",
#         label="In the feed, there was an overabundance of tweets unrelated to fashion.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#
# # Risk 1 Bruner et al. 2012 p. 159
#     risk_1 = models.IntegerField(
#         doc="Getting a product from Estrava is risky.",
#         label="Getting a product from Estrava is risky.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     risk_2 = models.IntegerField(
#         doc="A product from Estrava can lead to bad results.",
#         label="A product from Estrava can lead to bad results.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     risk_3 = models.IntegerField(
#         doc="A product from Estrava has uncertain results.",
#         label="A product from Estrava has uncertain results.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     risk_4 = models.IntegerField(
#         doc="Getting a product from Estrava makes me feel anxious.",
#         label="Getting a product from Estrava makes me feel anxious.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     risk_5 = models.IntegerField(
#         doc="Getting a product from Estrava would cause me to worry.",
#         label="Getting a product from Estrava would cause me to worry.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Brand Clarity Bruner et al. 2012 p. 159
#     brand_clarity_1 = models.IntegerField(
#         doc="To what extent do you think the characteristics of Estrava are coherent?",
#         label="The characteristics of Estrava are coherent.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_clarity_2 = models.IntegerField(
#         doc="To what extent do you view Estrava as an integrated brand?",
#         label="Estrava is an integrated brand.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_clarity_3 = models.IntegerField(
#         doc="To what extent does Estrava give you a concrete image about what this brand is like?",
#         label="Estrava gives me a concrete image about what the brand is like.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_clarity_4 = models.IntegerField(
#         doc="To what extent do you think it is easy to explain your impression of Estrava to other people?",
#         label="It is easy to explain my impression of Estrava to other people.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_clarity_5 = models.IntegerField(
#         doc="To what extent do you easily categorize what Estrava is?",
#         label="I easily categorize what Estrava is.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Prestige (Ko, Castello & Taylor 2019)
#     prestige_1 = models.IntegerField(
#         doc="Estrava is a symbol of prestige.",
#         label="Estrava is a symbol of prestige.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     prestige_2 = models.IntegerField(
#         doc="Estrava is a premium brand.",
#         label="Estrava is a premium brand.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     prestige_3 = models.IntegerField(
#         doc="Estrava is a high-end brand.",
#         label="Estrava is a high-end brand.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#
# # Brand innovativeness (Shams et al. 2015)
#     brand_innovativeness_1 = models.IntegerField(
#         label='Estrava sets itself apart from the rest when it comes to luxury fashion.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_innovativeness_2 = models.IntegerField(
#         label='With regard to luxury fashion, Estrava is dynamic.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_innovativeness_3 = models.IntegerField(
#         label='Estrava luxury fashion makes me feel “wow!”.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_innovativeness_4 = models.IntegerField(
#         label='Estrava is an innovative brand when it comes to luxury fashion.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_innovativeness_5 = models.IntegerField(
#         label='Estrava makes new luxury fashion with superior design.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_innovativeness_6 = models.IntegerField(
#         label='With regard to luxury fashion, Estrava generates new ideas.',
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Functional Value (Hennigs et al., 2012)
#     functional_value_1 = models.IntegerField(
#         label="I feel like Estrava offers a superior product quality.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     functional_value_2_r = models.IntegerField(
#         label="I feel like Estrava does not meet my quality standards and will thus, never enter into my purchase consideration.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     functional_value_3 = models.IntegerField(
#         label="I feel like Estrava puts emphasis on quality assurance over prestige.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#
#
# # Financial Value (Hennigs et al., 2012)
#     financial_value_1 = models.IntegerField(
#         label="Estrava luxury products are inevitably very expensive.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     financial_value_2 = models.IntegerField(
#         label="Few people own an Estrava luxury product.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     financial_value_3 = models.IntegerField(
#         label="Truly Estrava luxury products cannot be mass-produced.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     financial_value_4 = models.IntegerField(
#         label="An Estrava luxury product cannot be sold in supermarkets.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Individual Value (Hennigs et al., 2012)
#     individual_value_1 = models.IntegerField(
#         label="Browsing the feed, I felt like I would derive self-satisfaction from buying Estrava products.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     individual_value_2 = models.IntegerField(
#         label="Browsing the feed, I felt like purchasing Estrava clothing would make me feel good.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     individual_value_3 = models.IntegerField(
#         label="Browsing the feed, I felt like wearing Estrava clothing would give me a lot of pleasure.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     individual_value_4 = models.IntegerField(
#         label="Browsing the feed, I felt like Estrava products would be the perfect gift that I would buy to treat myself.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Social Value (Hennigs et al., 2012)
#     social_value_1 = models.IntegerField(
#         label="I feel like strangers would have a high opinion of me wearing Estrava.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     social_value_2 = models.IntegerField(
#         label="From now on, I pay attention to what types of people buy Estrava products.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     social_value_3 = models.IntegerField(
#         label="If I were to buy an Estrava product, I would worry about what others would think of me.",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)

# # Brand Equity Bruner et al. 2012 p. 153
#     brand_equity_1 = models.IntegerField(
#         doc="What kind of attitude did you have about Estrava?",
#         label="What kind of attitude did you have about Estrava?",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False,
#     )
#
#     brand_equity_2 = models.IntegerField(
#         doc="What kind of image did Estrava have?",
#         label="What kind of image did Estrava have?",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_equity_3 = models.IntegerField(
#         doc="How would you rate the quality delivered by Estrava?",
#         label="How would you rate the quality delivered by Estrava?",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     brand_equity_4 = models.IntegerField(
#         doc="Would you have been willing to pay more for products from Estrava than for other companies’ products?",
#         label="Would you have been willing to pay more for products from Estrava than for other companies’ products?",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
# # Persuasivness Bruner et al. 2019 p. 302
# # Estravas tweets were...
#
#     persuasive_1 = models.IntegerField(
#         doc="persuasive",
#         label="Persuasive",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     persuasive_2 = models.IntegerField(
#         doc="effective",
#         label="Effective",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     persuasive_3 = models.IntegerField(
#         doc="compelling",
#         label="Compelling",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)
#
#     persuasive_4 = models.IntegerField(
#         doc="convincing",
#         label="Convincing",
#         widget=widgets.RadioSelect,
#         choices=[1, 2, 3, 4, 5, 6, 7],
#         blank=False)

# Controls
    control_fashion = models.IntegerField(
        label='I have a strong interest in fashion, fashion trends and fashion advice.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    control_luxury = models.IntegerField(
        label='I have a strong interest in luxury brands and luxury fashion.',
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7],
        blank=False)

    control_web3 = models.IntegerField(
        label='I have a strong interest in blockchains, cryptocurrencies, NFTs or the metaverse.',
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
            [3, "Other"],
            [4, "Prefer not to say"],
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

# Attention Checks
    ac_1 = models.IntegerField(
        label="What was the name of the brand in the feed in this study?",
        blank=True,
        choices=[
            [1, "Evolene"],
            [2, "Estrava"],
            [3, "Exogen"],
            [4, "Elena"],
        ]
    )

    ac_2 = models.IntegerField(
        label="What is the home-country of this brand?",
        blank=True,
        choices=[
            [1, "Germany"],
            [2, "Italy"],
            [3, "France"],
            [4, "USA"],
        ]
    )



# completed the survey
    completed_survey = models.BooleanField(
        doc="True as soon as participants submit Feedback page",
        initial=False,
        blank=True
    )





# PAGES
class Manipulation_Check(Page):
    form_model = "player"
    form_fields = ["mc_3", "mc_4"]


class Open_Text_Fields(Page):
    form_model = "player"
    form_fields = ["otf_1", "otf_2"]


# class Brand_Contamination(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["brand_contamination_1_r", "brand_contamination_2", "brand_contamination_3_r",
#                        "brand_contamination_4", "brand_contamination_5"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Pollution(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["pollution_1", "pollution_2_r", "pollution_3"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Risk(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["risk_1", "risk_2", "risk_3", "risk_4", "risk_5"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Brand_Clarity(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["brand_clarity_1", "brand_clarity_2", "brand_clarity_3", "brand_clarity_4", "brand_clarity_5"]
#         random.shuffle(form_fields)
#         return form_fields


class Trust(Page):
    form_model = "player"
    form_fields = ["trust_1", "trust_2", "trust_3", "trust_4"]


# class Prestige(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["prestige_1", "prestige_2", "prestige_3"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Brand_Innovativeness(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["brand_innovativeness_1", "brand_innovativeness_2", "brand_innovativeness_3",
#                        "brand_innovativeness_4", "brand_innovativeness_5", "brand_innovativeness_6"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Functional_Value(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["functional_value_1", "functional_value_2_r", "functional_value_3"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Financial_Value(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["financial_value_1", "financial_value_2", "financial_value_3", "financial_value_4"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Individual_Value(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["individual_value_1", "individual_value_2", "individual_value_3",
#                        "individual_value_4"]
#         random.shuffle(form_fields)
#         return form_fields
#
#
# class Social_Value(Page):
#     form_model = "player"
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["social_value_1", "social_value_2", "social_value_3"]
#         random.shuffle(form_fields)
#         return form_fields


class Controls(Page):
    form_model = "player"
    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ["control_luxury", "control_fashion", "control_web3"]
        random.shuffle(form_fields)
        return form_fields


class Attention_Check(Page):
    form_model = "player"
    form_fields = ["ac_1", "ac_2"]


class Demographics(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "income"]
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.finished = True
        player.completed_survey = player.participant.finished

class Debriefing(Page):
    pass


page_sequence = [Manipulation_Check,
                 Open_Text_Fields,
                 # Brand_Contamination,
                 Trust,
                 # Pollution, Risk, Brand_Clarity, Prestige,
                 # Brand_Innovativeness, Functional_Value, Financial_Value, Individual_Value, Social_Value,
                 Controls, Attention_Check, Demographics, Debriefing]


# class Brand_Equity(Page):
#     form_model = "player"
#     form_fields = ["brand_equity_1", "brand_equity_2", "brand_equity_3", "brand_equity_4"]
#
# class Persuasion(Page):
#     form_model = "player"
#
#     @staticmethod
#     def get_form_fields(player: Player):
#         form_fields = ["persuasive_1", "persuasive_2", "persuasive_3", "persuasive_4"]
#         random.shuffle(form_fields)
#         return form_fields
