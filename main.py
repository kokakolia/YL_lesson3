from flask import render_template, Flask, url_for

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('base.html', name=title)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
