from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('listStation.html')

@app.route('/newStation')
def newEstation():
    return render_template('newStation.html')

@app.route('/priceStation')
def priceStation():
    return render_template('priceStation.html')

if __name__ == '__main__':
    app.run(debug=True)