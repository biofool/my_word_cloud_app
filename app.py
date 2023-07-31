from flask import Flask, render_template
import json
import os
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    pwd = os.getcwd()
    with open('/Users/kkron/projects/CABW/my_word_cloud_app/static/quotes.json') as json_file:
        data = json.load(json_file)
        keywords = []
        for quote in data['quotes']:
            try:
                keywords.extend(quote['keywords'])
            except KeyError:
                # The 'keywords' field is missing in this quote
                pass

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))

    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

    plt.savefig('/Users/kkron/projects/CABW/my_word_cloud_app/static/wordcloud.png')
    plt.close()
    quotes_json=data['quotes']
    return render_template('index.html', quotes_json=quotes_json)


if __name__ == '__main__':
    app.run(debug=True)
