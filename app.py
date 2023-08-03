from flask import Flask, render_template
import json
import os
from wordcloud import WordCloud
from flask import url_for
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt

app = Flask(__name__)
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Define the path to the quotes.json file within the static directory
quotes_path = os.path.join(static_dir, 'osensei_memoirs_quotes_8_words_escaped_pretty.json')


@app.route('/')
def index():
    with open(quotes_path) as json_file:
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
    wordcloud_path = os.path.join(static_dir, 'wordcloud.png')

    plt.savefig(wordcloud_path)
    plt.close()
    quotes_json=data['quotes']
    return render_template('index.html', quotes_json=quotes_json)


if __name__ == '__main__':
    app.run(debug=True)
