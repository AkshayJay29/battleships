import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Helper to initialize the board
def generate_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

# Helper to place ships
def place_ships(board, num_ships):
    ships = []
    size = len(board)
    while len(ships) < num_ships:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in ships:  # Avoid duplicate placements
            ships.append((x, y))
    return ships

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_game", methods=["POST"])
def start_game():
    data = request.json
    grid_size = int(data.get("gridSize", 5))
    num_ships = int(data.get("numShips", 3))

    # Initialize game state
    board = generate_board(grid_size)
    ships = place_ships(board, num_ships)
    return jsonify({
        "gridSize": grid_size,
        "ships": len(ships),
    })

@app.route("/guess", methods=["POST"])
def guess():
    data = request.json
    x, y = int(data["x"]), int(data["y"])
    grid_size = int(data["gridSize"])
    ships = data["ships"]

    if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
        return jsonify({"result": "invalid", "message": "Guess is off the grid!"})

    guess = (x, y)
    if guess in ships:
        ships.remove(guess)
        return jsonify({"result": "hit", "shipsLeft": len(ships)})
    else:
        return jsonify({"result": "miss", "shipsLeft": len(ships)})

if __name__ == "__main__":
    app.run(debug=True)
