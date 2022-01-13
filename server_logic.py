import random, RouteFinder, Board,moveLogic,bestReply
from typing import Dict



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
    Board.resetGameBoard()
    Board.resetFood()

    height = data["board"]["height"]
    width = data["board"]["width"]
    snakes = data["board"]["snakes"]
    food = data["board"]["food"]
    my_head = data["you"]["head"]

    for snake in snakes:
      if snake["id"] == data["you"]["id"]:
        mySnake = snake

    Board.initialiseBoard(width, height)
    Board.fillGameBoard(snakes, food, height)


    food = RouteFinder.findClosestFood(food, my_head)[0]
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = moveLogic.avoid_other_snakes(my_head, snakes, possible_moves)
    possible_moves = moveLogic.avoid_walls(my_head, width, height, possible_moves)
    possible_moves = moveLogic.checkForHeadCollision(mySnake,snakes,possible_moves,Board.getBoard())


    index = 0
    for s in snakes:
      if s["id"] == data["you"]["id"]:
        snakes.pop(index)
      index += 1       
    snakes.insert(0,mySnake)
    path = RouteFinder.bfsForFood(food, my_head, possible_moves)


    pinf = float('inf')
    ninf = float('-inf')
    boardCopy = Board.getBoard()[:]
    move = random.choice(possible_moves)


    if data['turn'] > 5:
      if len (possible_moves) > 1:
        result = (bestReply.BRS(ninf,pinf,2,"Max",boardCopy,snakes,"initial",mySnake))
  
        if result[1] in possible_moves:
          print(result)
          move = result[1]
        else:
          print("Broken")
          print(result)
          print(possible_moves)
          move = random.choice(possible_moves)

    if data["you"]["health"] < 25:
      if path != []:
        move = getMove(my_head, path[1])
      if (not move in possible_moves):
        move = random.choice(possible_moves)
        

    print(
        f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
    )


    return move