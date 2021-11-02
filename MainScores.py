from flask import Flask
app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        file = open('Scores.txt', 'r')
        score = file.read()
        return '<html>' \
               '<head>' \
               '<title>Scores Game</title>' \
               '</head>' \
               '<body>' \
               '<h1>' \
               '<div style="padding: 10px; display:inline-block">The score is :</div>' \
               '<div style="padding: 5px; display:inline-block" id="score">' + score + '</div>' \
                '</h1>' \
            '</body>' \
            '</html>'

    except BaseException as e:
        return '<html>' \
               '<head>' \
               '<title>Scores Game</title>' \
               '</head>' \
               '<body>' \
               '<h1>' \
               '<div style="padding: 10px; display:inline-block"> The score is </div>' \
               '<div style="padding: 10px; display:inline-block; color:red" id="score">{ERROR}</div>' \
               '</h1>' \
                '</body>' \
                '</html>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)