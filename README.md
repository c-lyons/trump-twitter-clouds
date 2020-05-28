# Trump Twitter Clouds

Returns world clouds of Trump tweets (does not include retweets). User can opt to select all words in a tweet, or select only capitalised tweets and can give option keyWord to filter by tweets containing user specified word.

User can also provide nWords which defined max number of words in word cloud. User can also provide 'since' variable to change start date.

Word clouds are printed to the screen and also to the *word-clouds* folder in the directory. A csv file of the final data-frame collected is also created in the project-data directory, along with JSON formatted lists of words used for plotting the clouds.

Note: Currently latest tweets are limited to May 2020.

        Keyword Arguments:

        keyWord {str} -- (Optional) Word to filter tweets by. Will select tweets only containing given word. Must be single word, not list or multiple words (e.g. can pass 'fake' but not 'fake news') (default: {None})
        nWords {int} -- Max words to show in word cloud. (default: {300})
        since {str} -- Start date for filtering tweets: format is YYYY-MM-DD. (default: {'2017-01-20'})
        getCaps {bool} -- Decides whether to print clouds based on words from full tweets or to limit word cloud words to only the words CAPITALISED RANDOMLY in Trump's tweets.

Arguments can be passed as flags when running from your terminal.

Run --help flag to get helper function.

## Example

For example, to get a word cloud of all capital words in Trump's tweets about Obama since 2012, run the following:

>python3 trumpTweets.py --keyWord 'Obama' --since '2012-01-01' --getCaps True

## Changing the Template

The template used can be found in the profile-templates. To change this, replace the below image (*trump-side.jpg*) with a silhouette style image, as shown below. The black parts of the image define the boundaries where the [WordCloud python module](https://amueller.github.io/word_cloud/) will plot the words in the word cloud.

<p align="center">
  <img src=profile-templates/trump-side.jpg width=40%>
</p>

## Examples

*Tweets about Clinton during Presidency:*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-clinton-since-2017-01-20.png width="100%">
</p>

*Tweets about Russia during Presidency:*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-russia-since-2017-01-20.png
.png width="100%">
</p>

*ALL CAPS Tweets since start of Presidency:*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-None-since-2017-01-20-CAPS.png width="100%">
</p>

*Tweets about China during Presidency:*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-china-since-2017-01-20.png width="100%">
</p>

*ALL CAPS Tweets about Obama since 2012:*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-Obama-since-2012-01-01-CAPS.png width="100%">
</p>

*ALL CAPS Tweets about 'News':*

<p align="center">
  <img src=examples/trump-word-cloud-300-words-news-since-2017-01-20-CAPS.png width="100%">
</p>

*Tweets about 'Mueller' during Presidency:*
<p align="center">
  <img src=examples/trump-word-cloud-300-words-mueller-since-2017-01-20.png width="100%">
</p>