Freeriding the Metaverse: Data Collection
================

``` r
options(stringsAsFactors = FALSE)
invisible(Sys.setlocale(category = "LC_ALL", locale = "C"))
set.seed(42)
```

``` r
# install.packages("pacman")
pacman::p_load(magrittr, data.table, stringr, lubridate, # overviewR,
               ggplot2, MetBrewer, knitr, fs, purrr,
               qdapRegex)
```

``` r
STARTDATE <- as.Date("2022-03-23")
ENDDATE   <- as.Date("2022-03-27")
```

# Data

## TWINT Querry

We query data using [TWINT.](https://github.com/twintproject/twint) We
use brands such as Tommy Hilfiger and Forever 21, who opened flagship
stores in decentraland and of whom we know that they posted something
about the MVFW, as a starting point to fine tune our query.

Using the following two queries, I eventually create two objects:

-   **hilfiger**
    `twint -u TommyHilfiger -s "mvfw" --since "2022-02-23" --until "2022-04-24" --lang "en" -o dev/mvfw/data/Hilfigerdata.csv --csv`

-   **forever21**
    `twint -u Forever21 -s "Metaverse Fashion Week" --since "2022-02-23" --until "2022-04-24" --lang "en" -o dev/mvfw/data/Forever21data.csv --csv`

``` r
hilfiger <- read.csv("../data/Hilfigerdata.csv", sep = "\t") %>%
  data.table()
forever21 <- read.csv("../data/Forever21data.csv", sep = "\t") %>% 
  data.table()
```

These two objects illustrate that one should be able to retrieve
relevant data using the search terms `msfw` as well as
`metaverse fashion week`.[^1] I therefore, use these queries but

1.  omit the username specifications and
2.  reduce the time frame to the duration of the MVFW (because it seems
    as if larger querries yield sampled data).

-   **tmp1**
    `twint -s "mvfw" --since "2022-03-24" --until "2022-03-27" --lang "en" -o dev/mvfw/data/MVFWdata1.csv --csv`

-   **tmp2**
    `twint -s "Metaverse Fashion Week" --since "2022-03-24" --until "2022-03-27" --lang "en" -o dev/mvfw/data/MVFWdata2.csv --csv`

``` r
tmp1 <- read.csv("../data/MVFWdata1.csv", sep = "\t") %>% 
  data.table()
tmp2 <- read.csv("../data/MVFWdata2.csv", sep = "\t") %>% 
  data.table()
tmp <- data.table::rbindlist(l = list(tmp1, tmp2))
```

Moving forward, we could apply this strategy to multiple (short) time
periods and `rbind()` the resulting data objects.

## Time Frames

    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-02-23" --until "2022-03-02" --lang "en" -o dev/mvfw/data/timeFrames/tmp1.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-03-02" --until "2022-03-09" --lang "en" -o dev/mvfw/data/timeFrames/tmp2.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-03-09" --until "2022-03-16" --lang "en" -o dev/mvfw/data/timeFrames/tmp3.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-03-16" --until "2022-03-23" --lang "en" -o dev/mvfw/data/timeFrames/tmp4.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-03-23" --until "2022-03-28" --lang "en" -o dev/mvfw/data/timeFrames/tmp5.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-03-28" --until "2022-04-04" --lang "en" -o dev/mvfw/data/timeFrames/tmp6.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-04-04" --until "2022-04-11" --lang "en" -o dev/mvfw/data/timeFrames/tmp7.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-04-11" --until "2022-04-18" --lang "en" -o dev/mvfw/data/timeFrames/tmp8.csv --csv
    twint -s "mvfw OR (Metaverse Fashion Week)" --since "2022-04-18" --until "2022-04-27" --lang "en" -o dev/mvfw/data/timeFrames/tmp9.csv --csv

``` r
data_path    <- "../data/timeFrames/"
file_paths   <- fs::dir_ls(path = data_path, glob = "*.csv")
object_names <- str_replace_all(string = file_paths,
                                pattern = paste0(data_path, "|\\.csv"),
                                replacement = "")
datasets     <- purrr::map(file_paths, read.csv, sep = "\t")
tmp <- data.table::rbindlist(l = datasets)
```

## Brands

Additionally, one can scrape data by brands. To do so, I’ll use the
following query and replace `[username]`.

    twint -u [username] -s "mvfw OR (Metaverse Fashion Week)" --since "2022-02-23" --until "2022-04-24" --lang "en" -o dev/mvfw/data/brands/[username].csv --csv

<!--
=CONCAT("twint -u ", B2, " -s "'mvfw OR (Metaverse Fashion Week)" --since "'2022-02-23" --until "'2022-04-24" --lang "'en" -o dev/mvfw/data/brands/", B2, ".csv --csv")
-->

``` r
data_path   <- "../data/brands/"
file_paths  <- fs::dir_ls(path = data_path, glob = "*.csv")
datasets    <- purrr::map(file_paths, read.csv, sep = "\t")
brands <- data.table::rbindlist(l = datasets)
```

## Refactor

``` r
temp <- data.table::rbindlist(l = list(tmp, brands))
```

``` r
# String clean up 
temp[, tweet := iconv(tweet, "latin1", "ASCII", sub = "")]
temp[, tweet := rm_url(tweet,                    # remove URLs
                      pattern = pastex("@rm_twitter_url", "@rm_url"))]

# subset english sample of UNIQUE tweets
en <- tmp[language == "en"] %>% unique(by = "tweet")

# create distinc ID
en[, doc_id := .I]

# change date & time format
en[, created_at := str_sub(string = created_at,
                           start  = 1,
                           end    = 19) %>% ymd_hms()]
en[, date := ymd(date)]

# store mentions (@....)
en[, customMentions := str_extract_all(string = tweet,
                                       pattern = "@\\S+")]
en[customMentions == "character(0)", 
   customMentions := NA]
en[, nMentions := str_count(string = customMentions, pattern = "@")]
```

    ## Warning in stri_count_regex(string, pattern, opts_regex = opts(pattern)):
    ## argument is not an atomic vector; coercing

``` r
# tag web3 usernames by regex
en[str_detect(string = username,
                pattern = "nfts?|crypt|krypt|meta|block|coin"),
     domain := "web3"]

# tag fashion-related usernames by regex
en[str_detect(string = username,
                pattern = "fashion|beauty"),
     domain := "fashion"]

# tag web3 freeriders
en[username %in% c("Deadfellaz", "gossapegirl", "asian_mint", "canessadcl",     # NAME WEB3 HERE!
                   "ericpi888", "itskac", "antisecretsoci2", "cmnnewsofficial",
                   "cathyhackl", # maybe too much fame to be a free rider?
                   "btctn", "_mannyalves", "maryanadcl", "martinshibuya",
                   "eagle_stephen_", "8sianmom", "tokens_com", "mrbathinape",
                   "michi_todd", "bitpanda", "brytehall", "universelle_io",
                   "kcain1982", "borgetsebastien", "barbarakahn", "diviproject",
                   "ziziverse", "astronotseth", "yannakis_dcl", "xpozd_io",
                   "tangpoko", "thesevens_7", "portionapp", "0xjoules",
                   "teenybod", "celinatech", "enilev", "siddharthakur",
                   "pedroguez__"), 
     domain := "web3"]

# tag web3 x fashion
en[username %in% c("thefabricant", "xrcouture", "auroboros_ltd", "wirelyss",    # NAME WEB3 FASHION HERE!
                   "polygondressing", "the_vogu", "shopcider", "houseofdaw",
                   "neuno_io", "stylexchange_io"), 
     domain := "digital fashion"]

# tag influencers & media
en[username %in% c("thalia", "maghanmcd", "diamondhandbag", "realfaithtribe"   # NAME INFLUENCERS HERE!
                   ), 
     domain := "platform"]

# tag fashion brands
en[username %in% brands[, unique(username)], # NAME BRANDS HERE!
     domain := "brands"]

# tag platform- or ecosystem related users
en[username %in% c("decentraland", "bosonprotocol", "exclusible", "threedium",  # NAME PLATFORMS HERE!
                   "pangeadao", "dragoncityio", "whiterabbitgate"), 
     domain := "platform"]

# manual inspection
en[username %in% c("additionalrules", "media_diamante"),
     domain := "web3"]
```

``` r
# re-arrange data for corpus
data <- en[,
           .(doc_id,
             text = tweet,
             hashtags,
             cashtags,
             domain,
             username,
             mentions,
             customMentions,
             nMentions,
             name,
             place,
             urls,
             photos,
             video,
             geo,
             created_at,
             timezone,
             replies_count,
             retweets_count,
             likes_count,
             language,
             id,
             conversation_id,
             retweet_id)]
```

The data contains 6.731 rows, each representing a tweet. Its columns
represent some IDs, meta information about URLs, retweets, etc. as well
as the tweets itself (from which I removed URLs using
`qdapRegex::rm_url()`).

# Inspection

Here is a list of the 50 users that received the most likes.

``` r
# data[, .(likes = sum(likes_count, na.rm = TRUE)), by = c("username", "domain")][order(-likes)] %>% head(50) %>% kable()
data[is.na(domain), 
     .(likes = sum(likes_count, na.rm = TRUE)),
     by = username][order(-likes)] %>% 
  head(100) %>%
  kable()
```

| username        | likes |
|:----------------|------:|
| deadfellaz      |   822 |
| nikkifuego92    |   106 |
| reuters         |    94 |
| forbes          |    79 |
| nicole29nixon   |    78 |
| andywangnyla    |    70 |
| altavagroup     |    69 |
| ww_ventures     |    67 |
| davidcash888    |    66 |
| move78studio    |    65 |
| qdibs_eth       |    63 |
| realsophiarobot |    63 |
| parzival_kazuto |    61 |
| manadaiquiridcl |    61 |
| madamape        |    61 |
| decentralgames  |    61 |
| degenitamar     |    59 |
| projectmediahq  |    58 |
| dcljasonx       |    58 |
| forbeslife      |    57 |
| mutani_io       |    56 |
| 0xquiksilver    |    55 |
| ellemagazine    |    55 |
| reginaturbina   |    54 |
| jonassft        |    53 |
| bitski          |    53 |
| jtv\_\_\_\_     |    52 |
| lingxing_dcl    |    51 |
| soultrydubs     |    51 |
| dogmandcl       |    50 |
| knownorigin_io  |    50 |
| danitpeleg3d    |    50 |
| voguebusiness   |    49 |
| survive_p2e     |    49 |
| mgh_dao         |    49 |
| serenaelis\_    |    47 |
| koryptostylist  |    47 |
| voguesingapore  |    47 |
| tonydarko_eth   |    46 |
| 4bitanimation   |    46 |
| voguemagazine   |    46 |
| jewdontknow     |    45 |
| labordeolivier  |    44 |
| etherealitylove |    43 |
| djckay          |    43 |
| nat0shisakamoto |    43 |
| bufalomusic     |    42 |
| bonrolledomains |    41 |
| artemismoon23   |    40 |
| dahliajunef     |    40 |
| dcl_events      |    39 |
| strawberrysith  |    39 |
| father_fin      |    39 |
| bootsy_collins  |    37 |
| wrangler        |    37 |
| robertkalinkin  |    36 |
| supermoongirl9  |    36 |
| kevinonearth999 |    35 |
| daitoyoshi      |    35 |
| definitecasheth |    35 |
| secondlife      |    35 |
| theflyingvyse   |    34 |
| java_23\_       |    34 |
| laurochris      |    33 |
| doki3d          |    33 |
| itsoohleila     |    33 |
| moyosorebriggs  |    33 |
| trustswap       |    32 |
| matyeth         |    32 |
| gulnara_guliagg |    31 |
| jadeysunshine   |    31 |
| ashes_ls        |    31 |
| g0dzii          |    31 |
| gjordonz        |    30 |
| lifebeyond      |    30 |
| tomemrich       |    29 |
| stoney_eye      |    29 |
| lowpolymodelsw  |    29 |
| fermion_dcl_eth |    29 |
| dinar_afro      |    28 |
| eriklapaglia    |    28 |
| kinestryio      |    28 |
| imndlabs        |    28 |
| eduasykes       |    28 |
| makelismosbrand |    28 |
| trickstar_dcl   |    28 |
| btschain\_      |    27 |
| alexnomads      |    27 |
| yannycharleston |    27 |
| tribute_brand   |    26 |
| wwd             |    26 |
| oneworldu       |    26 |
| mprincessmaya   |    26 |
| quantumxe487    |    26 |
| cosmicendo      |    26 |
| guardian        |    25 |
| artcebola       |    25 |
| agoracom        |    24 |
| relianne1       |    24 |
| polygonalmind   |    24 |

# To do

-   Identify Brands

-   Identify Influencers

[^1]: Attempts to combine both search terms using `OR` failed.
