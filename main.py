import tkinter as tk
from textblob import TextBlob
from newspaper import Article


root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

title_label = tk.Label(root, text="Title")
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#F0F0F0')
title.pack()

author_label = tk.Label(root, text="Author")
author_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#F0F0F0')
author.pack()

publish_date_label = tk.Label(root, text="Publish Date")
publish_date_label.pack()

publish_date = tk.Text(root, height=1, width=140)
publish_date.config(state='disabled', bg='#F0F0F0')
publish_date.pack()

summary_label = tk.Label(root, text="Summary")
summary_label.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#F0F0F0')
summary.pack()

sentiment_label = tk.Label(root, text="Sentiment")
sentiment_label.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#F0F0F0')
sentiment.pack()

url_label = tk.Label(root, text="URL")
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.config(state='normal', bg='#F0F0F0')
url_text.pack()


def summarize():
    url = url_text.get('1.0', 'end-1c')
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    title.delete('1.0', tk.END)
    title.insert(tk.END, article.title)
    title.config(state='disabled')

    author.config(state='normal')
    author.delete('1.0', tk.END)
    author.insert(tk.END, article.authors)
    author.config(state='disabled')

    publish_date.config(state='normal')
    publish_date.delete('1.0', tk.END)
    publish_date.insert(tk.END, article.publish_date)
    publish_date.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', tk.END)
    summary.insert(tk.END, article.summary)
    summary.config(state='disabled')

    analysis = TextBlob(article.text)
    sentiment.config(state='normal')
    sentiment.delete('1.0', tk.END)
    sentiment.insert(tk.END,
                     f'{"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')
    sentiment.config(state='disabled')


btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
