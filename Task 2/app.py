from flask import Flask, request, render_template
from aggregator import parse


app = Flask(__name__)


@app.route('/convert_curreny/', methods=['GET'])
def convert_func():
    user_currency = request.args.get('currency')
    user_amount = request.args.get('amount')
    for i in parse():
        if user_currency.upper() == i['Код літерний']:
            result = i['Офіційний курс'] / i['Кількість одиниць валюти'] * float(user_amount)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run('0.0.0.0')