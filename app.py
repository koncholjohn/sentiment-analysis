from flask import Flask, render_template, request
from nlp.analyzer import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    text = request.form['text']

    result = analyze_sentiment(text)

    return render_template(
        'result.html',
        text=text,
        result=result
    )

if __name__ == '__main__':
    app.run(debug=True)