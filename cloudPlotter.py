from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import json
import numpy as np
from PIL import Image    # to import the image

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

def main():

    # reading json data for cleaned list of words
    with open("project-data/cleaned_words.json", 'r') as f:
        cleaned_words = json.load(f)

    with open("project-data/cleaned_capital_words.json", 'r') as f:
        cleaned_caps = json.load(f)


    trump_mask = np.array(Image.open("profile-templates/trump-side.jpg"))

    print('Word Clouds printing to directory...')

    # Make the figure
    wordcloud = WordCloud(max_words=3000, prefer_horizontal =0.5, mask=trump_mask,stopwords=stopwords).generate(' '.join(cleaned_words))
    plt.figure(figsize=(40,40))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig('project-data/trump-word-cloud.png')

    trump_mask = np.array(Image.open("profile-templates/trump-side.jpg"))

    # Make the figure
    wordcloud = WordCloud(max_words=300, prefer_horizontal =0.5, mask=trump_mask,stopwords=stopwords).generate(' '.join(cleaned_caps))
    plt.figure(figsize=(40,40))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig('project-data/trump-word-cloud-caps.png')

    print('Word Clouds successfully printed to directory.')
