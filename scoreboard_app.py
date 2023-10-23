from flask import Flask, render_template, request

from web_scoreboard.database import Match

app = Flask(__name__)


@app.route('/')
def home():
    match = Match()
    return render_template('index.html', match=match)


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test(match):
    print(match)
    print('hello')
    return ("nothing")


if __name__ == '__main__':
    app.run(debug=True)
