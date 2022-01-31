import logging
import os

from flask import Flask
from flask import request

import server_logic

app = Flask(__name__)


@app.get("/")
def handle_info():
    """
    This function is called when you register your Battlesnake on play.battlesnake.com
    See https://docs.battlesnake.com/guides/getting-started#step-4-register-your-battlesnake

    It controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    print("INFO")
    return {
        "apiversion": "1",
        "author": "ekans",
        "color": "#800080",
        "head": "safe",
        "tail": "small-rattle",
    }


@app.post("/start")
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


@app.post("/move")
def handle_move():
    """
    This function is called on every turn of a game. It's how your snake decides where to move.
    Valid moves are "up", "down", "left", or "right".
    """
    data = request.get_json()

    # TODO - look at the server_logic.py file to see how we decide what move to return!
    move = server_logic.choose_move(data)

    return {"move": move}


@app.post("/end")
def end():
    """
    This function is called when a game your snake was in ends.
    It's purely for informational purposes, you don't have to make any decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    f = open("gameHistory.txt", "a")
    f.write("\n")
    
    if data["board"]["snakes"] == []:    
      f.write(f"Tie")
      f.write("\n")
      f.write(f"{data['turn']}")
      f.write("\n")
      f.write(f"{data['game']['id']} ")
      f.write("\n")
      f.close()
      return "ok"

    finalsnake = data["board"]["snakes"][0]
    if finalsnake['id'] == data['you']['id'] :
        f.write(f"Win")
        f.write("\n")
        f.write(f"{data['turn']}")
        f.write("\n")
        f.write(f"{data['game']['id']} ")
    else:
        f.write(f"Loss")
        f.write("\n")
        f.write(f"{data['turn']}")
        f.write("\n")
        f.write(f"{data['game']['id']} ")
    f.write("\n")
    f.close()
    return "ok"


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
