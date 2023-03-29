import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
url = 'https://edition.cnn.com/2023/03/29/world/climate-change-photography-paul-nicklen-cristina-mittermeier-c2e-spc-intl-scn-climate/index.html'
article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Article Title: {article.title}')
print(f'Article Author: {article.authors}')
print(f'Article Publish Date: {article.publish_date}')
print(f'Article Summary: {article.summary}')


# sentiment analysis
analysis = TextBlob(article.text)
print(f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')






