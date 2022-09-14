library(tidytext)
library(dplyr)
library(tidyverse)
library(wordcloud)

metaverseUnnested <- read.csv(file = "studentProject/metaverseUnnested.csv")
metaverseUnnested <- metaverseUnnested[!metaverseUnnested$word %in% c("discord", "nifty", "tout", "nifty"),]

metaverseUnnested %>%
  count(word) %>%
  with(wordcloud(word, n, max.words = 200, colors="turquoise4"))
metaverseUnnested <-  inner_join(metaverseUnnested, get_sentiments("afinn"), by = "word")
tweetPolarity <- aggregate(value ~ ...1, metaverseUnnested, mean)

metaverseUnnested$date <- as.Date(as.character(metaverseUnnested$date), "%d/%m/%Y")
date_sentiment <- aggregate(value ~ date, metaverseUnnested, mean)
tweets <-  inner_join(metaverseUnnested, tweetPolarity, by = "...1")

ggplot(date_sentiment, aes(x = date, y = value)) +
  geom_smooth(method="loess", size=1, se=T, span = .5) +
  geom_hline(yintercept=0, color = "grey") + #plot a grey line at 0, i.e. neutral sentiment
  ylab("Avg. Sentiment") +  #set a name to the y-axis
  xlab("Date") + #set name to x-axis
  ggtitle("Sentiment of Tweets over time") +
  geom_vline(xintercept = as.numeric(as.Date("2022-03-24")), linetype=4) +
  geom_vline(xintercept = as.numeric(as.Date("2022-03-27")), linetype=4) 

beforeEvent <- metaverseUnnested[metaverseUnnested$date <= "2022-03-23", ]
duringEvent <- metaverseUnnested[metaverseUnnested$date >= "2022-03-24" & metaverseUnnested$date <= "2022-03-27", ]
afterEvent <- metaverseUnnested[metaverseUnnested$date >= "2022-03-25", ]

#sentiment for BEFORE event
sentiment_beforeEvent <- beforeEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  ungroup()

library(ggplot2)
sentiment_beforeEvent %>%
  group_by(sentiment) %>%
  top_n(10) %>%
  ungroup() %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill = sentiment)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~sentiment, scales = "free_y") +
  labs(y = "Contribution to sentiment",
       x = NULL) +
  coord_flip()

install.packages("reshape2")
library(reshape2)

dev.new(width = 1000, height = 1000, unit = "px")
sentiment_beforeEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("red", "green"),
                   max.words = 10000)

sentiment_beforeEvent %>%
  group_by(sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(polarity = positive - negative) %>%
  filter(abs(polarity)<10) %>%
  ggplot(aes(polarity)) +
  geom_density(alpha = 0.3) +
  geom_vline(xintercept=0, linetype="dashed", color = "red")+
  ggtitle("Polarity tweets before the Event")

#sentiment for DURING event
sentiment_duringEvent <- duringEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  ungroup()

library(ggplot2)
sentiment_duringEvent %>%
  group_by(sentiment) %>%
  top_n(10) %>%
  ungroup() %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill = sentiment)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~sentiment, scales = "free_y") +
  labs(y = "Contribution to sentiment",
       x = NULL) +
  coord_flip()

install.packages("reshape2")
library(reshape2)

dev.new(width = 1000, height = 1000, unit = "px")
sentiment_duringEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("red", "green"),
                   max.words = 10000)

library(tidyr)
sentiment_duringEvent %>%
  group_by(sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(polarity = positive - negative) %>%
  filter(abs(polarity)<10) %>%
  ggplot(aes(polarity)) +
  geom_density(alpha = 0.3) +
  geom_vline(xintercept=0, linetype="dashed", color = "red")+
  ggtitle("Polarity tweets during the Event")

#sentiment for AFTER event
sentiment_afterEvent <- afterEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  ungroup()

library(ggplot2)
sentiment_afterEvent %>%
  group_by(sentiment) %>%
  top_n(10) %>%
  ungroup() %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n, fill = sentiment)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~sentiment, scales = "free_y") +
  labs(y = "Contribution to sentiment",
       x = NULL) +
  coord_flip()

install.packages("reshape2")
library(reshape2)

dev.new(width = 1000, height = 1000, unit = "px")
sentiment_afterEvent %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("red", "green"),
                   max.words = 10000)

library(tidyr)
sentiment_afterEvent %>%
  group_by(sentiment) %>%
  spread(sentiment, n, fill = 0) %>%
  mutate(polarity = positive - negative) %>%
  filter(abs(polarity)<10) %>%
  ggplot(aes(polarity)) +
  geom_density(alpha = 0.3) +
  geom_vline(xintercept=0, linetype="dashed", color = "red")+
  ggtitle("Polarity tweets after the Event")

