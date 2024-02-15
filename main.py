from flask import render_template, Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/list_prof/<val>')
def listProf(val):
    list_prof = ['Инженер-исследователь', 'Инженер-строитель', 'Пилот', 'Метеоролог', 'Инженер по жизниобеспечению',
                 'Инженер по радиоционной защите', 'Врач', 'Экзобиолог']
    return render_template('base.html', list_prof=list_prof, val=val)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
