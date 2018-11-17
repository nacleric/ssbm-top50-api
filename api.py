from flask import Flask, jsonify
from melee import print_player
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route('/api/<player>')
def get_player(player):
    h2h_stats = print_player(player)
    return jsonify(smasher=player,
    				matchups=h2h_stats) 

if __name__ == '__main__':
    app.run(debug=True)
