from flask import Flask
from melee import print_player
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route('/api/<player>')
def get_player(player):
    return print_player(player)

if __name__ == '__main__':
    app.run(debug=True)
