from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import json
import numpy as np
from PIL import Image    # to import the image

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

def main(keyWord, nWords, since):

    if keyWord == None:
        title = f'Trump\'s Tweets (since {since})'
        titleCaps =  f'Trump\'s ALL CAPS Tweets (since {since})'
    else:
        title = f'Trump\'s Tweets about {keyWord} since {since})'
        titleCaps =  f'Trump\'s ALL CAPS Tweets about {keyWord} (since {since})'

    # reading json data for cleaned list of words
    with open("project-data/cleaned_words.json", 'r') as f:
        cleaned_words = json.load(f)

    with open("project-data/cleaned_capital_words.json", 'r') as f:
        cleaned_caps = json.load(f)

    trump_mask = np.array(Image.open("profile-templates/trump-side.jpg"))

    print('Word Clouds printing to directory...')

    # Make the figure
    wordcloud = WordCloud(max_words=nWords, prefer_horizontal =0.5, mask=trump_mask,stopwords=stopwords).generate(' '.join(cleaned_words))
    plt.figure(figsize=(40,40))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    #plt.text(300,10, s=title, c='orange', stretch=1000, weight='heavy', size='xx-large', style='oblique', va='center', fontfamily='sans-serif')
    plt.savefig(f'word-clouds/trump-word-cloud-{nWords}-words-{str(keyWord)}.png')
    plt.show()

    # Make the figure
    wordcloud = WordCloud(max_words=nWords, prefer_horizontal =0.5, mask=trump_mask,stopwords=stopwords).generate(' '.join(cleaned_caps))
    plt.figure(figsize=(40,40))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    #plt.text(300,10, s=titleCaps, c='orange', stretch=1000, weight='heavy', size='xx-large', style='oblique', va='center', fontfamily='sans-serif')
    plt.savefig(f'word-clouds/trump-word-cloud-caps-{nWords}-words-{str(keyWord)}.png')
    plt.show()

    print('Word Clouds successfully printed to directory.')
