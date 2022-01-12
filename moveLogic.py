from typing import Dict,List


def avoid_other_snakes(my_head: Dict[str, int], enemy_snake: List[dict],
                       possible_moves: List[str]):

    for s in enemy_snake:
      current_snake = s["body"][:-1]
      for snake_body in current_snake:
          if my_head["x"] == snake_body["x"] + 1 and my_head[
                  "y"] == snake_body["y"] and "left" in possible_moves:
              possible_moves.remove("left")
          if my_head["x"] == snake_body["x"] - 1 and my_head[
                  "y"] == snake_body["y"] and "right" in possible_moves:
              possible_moves.remove("right")
          if my_head["y"] == snake_body["y"] + 1 and my_head[
                  "x"] == snake_body["x"] and "down" in possible_moves:
              possible_moves.remove("down")
          if my_head["y"] == snake_body["y"] - 1 and my_head[
                  "x"] == snake_body["x"] and "up" in possible_moves:
              possible_moves.remove("up")
    return possible_moves


def avoid_walls(my_head: Dict[str, int], width: int, height: int,
                possible_moves: List[str]):
    if my_head["x"] == width - 1 and "right" in possible_moves:
        possible_moves.remove("right")
    if my_head["x"] == 0 and "left" in possible_moves:
        possible_moves.remove("left")
    if my_head["y"] == 0 and "down" in possible_moves:
        possible_moves.remove("down")
    if my_head["y"] == height - 1 and "up" in possible_moves:
        possible_moves.remove("up")
    return possible_moves

def checkForHeadCollision(my_snake: List[Dict],snakes:List[dict],possible_moves: List[str],board:List[str]):
  newMoves = possible_moves[:]
  for s in snakes:

    if "left" in newMoves:
      if (s["head"]["y"] - 1 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] or s["head"]["y"] == my_snake["head"]["y"]) and ((s["head"]["x"] == my_snake["head"]["x"]-2) or my_snake["head"]["x"] - 1 == s["head"]["x"]):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("left")

    if "right" in newMoves: 
      if (s["head"]["y"] - 1 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] or s["head"]["y"] == my_snake["head"]["y"] ) and ((s["head"]["x"] == my_snake["head"]["x"]+2) or my_snake["head"]["x"] + 1 == s["head"]["x"]):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("right")

    if "down" in newMoves:
      if (s["head"]["y"] + 2 == my_snake["head"]["y"] or s["head"]["y"] + 1 == my_snake["head"]["y"] ) and ((s["head"]["x"] == my_snake["head"]["x"]+1) or my_snake["head"]["x"]-1 == s["head"]["x"] or my_snake["head"]["x"] == s["head"]["x"]):

        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("down")

    if "up" in newMoves:
      if (s["head"]["y"] - 2 == my_snake["head"]["y"] or s["head"]["y"] - 1 == my_snake["head"]["y"]) and ((s["head"]["x"] == my_snake["head"]["x"]+1) or my_snake["head"]["x"]-1 == s["head"]["x"] or my_snake["head"]["x"] == s["head"]["x"] ):
        if(len(my_snake["body"]) <= len(s["body"])):
          newMoves.remove("up")

  if newMoves == []:
    return possible_moves

  return newMoves
