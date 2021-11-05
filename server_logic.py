import random, RouteFinder, Board,moveLogic
from typing import Dict
"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""



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
    possible_moves = moveLogic.avoid_other_snakes(my_head, snakes, possible_moves)
    possible_moves = moveLogic.avoid_walls(my_head, width, height, possible_moves)
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
