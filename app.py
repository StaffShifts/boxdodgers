from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mode')
def mode():
    return render_template('mode.html')

@app.route('/game/<difficulty>')
def game(difficulty):
    return render_template('game.html', difficulty=difficulty)

if __name__ == '__main__':
    app.run(debug=True)
