import random, RouteFinder, Board
from typing import List, Dict
"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_other_snakes(my_head: Dict[str, int], enemy_snake: List[dict],
                       possible_moves: List[str]):
    for s in enemy_snake:
        current_snake = s["body"][:-1]
        for snake_body in current_snake:
            if my_head["x"] == snake_body["x"] + 1 and my_head[
                    "y"] == snake_body["y"] and "left" in possible_moves:
                possible_moves.remove("left")
            elif my_head["x"] == snake_body["x"] - 1 and my_head[
                    "y"] == snake_body["y"] and "right" in possible_moves:
                possible_moves.remove("right")
            elif my_head["y"] == snake_body["y"] + 1 and my_head[
                    "x"] == snake_body["x"] and "down" in possible_moves:
                possible_moves.remove("down")
            elif my_head["y"] == snake_body["y"] - 1 and my_head[
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


def getMove(head: Dict[str, int], coOrd: Dict[str, int]):
    if head["x"] == (coOrd["x"] + 1):
        return "left"
    if head["x"] == (coOrd["x"] - 1):
        return "right"
    if head["y"] == (coOrd["y"] + 1):
        return "down"
    if head["y"] == (coOrd["y"] - 1):
        return "up"
    return "error"


def choose_move(data: dict) -> str:

    height = data["board"]["height"]
    width = data["board"]["width"]
    snakes = data["board"]["snakes"]
    food = data["board"]["food"]
    my_head = data["you"]["head"]

    Board.initialiseBoard(width, height)
    Board.fillGameBoard(snakes, food, height)

    food = RouteFinder.findClosestFood(food, my_head)
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = avoid_other_snakes(my_head, snakes, possible_moves)
    possible_moves = avoid_walls(my_head, width, height, possible_moves)
    path = RouteFinder.bfsForFood(food, my_head, possible_moves)

    if path != []:
        move = getMove(my_head, path[1])
        if (not move in possible_moves):
            move = random.choice(possible_moves)
    else:
        move = random.choice(possible_moves)
    """gmBoardCopy = Board.getBoard()
    newBoard = gmBoardCopy[:]
    print(gmBoardCopy)
    newBoard = (Board.simulateMoveForMe(random.choice(possible_moves),snakes[0],newBoard,height,width))
    print(newBoard)"""

    print(
        f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
    )
    Board.resetGameBoard()
    return move
