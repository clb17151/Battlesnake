import random, RouteFinder, Board,moveLogic, maxN, time, copy
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

    height = data["board"]["height"]
    width = data["board"]["width"]
    snakes = data["board"]["snakes"]
    food = data["board"]["food"]
    my_head = data["you"]["head"]


 
    gameBoard = Board.initialiseBoard(width, height)
    gameBoard = Board.fillGameBoard(snakes, food, height,gameBoard)
    possible_moves = ["up", "down", "left", "right"]
    food = RouteFinder.findClosestFood(food, my_head)
    possible_moves = moveLogic.avoid_other_snakes(my_head, snakes, possible_moves)
    possible_moves = moveLogic.avoid_walls(my_head, width, height, possible_moves)
    for snake in snakes:
      if snake["id"] == data["you"]["id"]:
        mySnake = snake

    if data["turn"] > 5:
      start = time.time()

  

      index = 0
      for s in snakes:
        if s["id"] == data["you"]["id"]:
          snakes.pop(index)
        index += 1       
      snakes.insert(0,mySnake)

      boardCopy =copy.deepcopy(gameBoard)
      print (maxN.maxn(boardCopy,1,snakes,0))
      path = RouteFinder.bfsForFood(food, my_head, possible_moves)
      end = time.time()
      print("The time for thinking is: ", end - start)

      if path != []:
          move = getMove(my_head, path[1])
          if (not move in possible_moves):
              move = random.choice(possible_moves)

        
      else:
          move = random.choice(possible_moves)
    else:
      move = random.choice(possible_moves)


    print(
        f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
    )
    return move