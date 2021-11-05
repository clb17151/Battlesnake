from typing import List, Dict

gameBoard = []
height = 0
width = 0

def initialiseBoard(boardWidth: int, boardHeight: int):
  global height,width
  width = boardWidth
  height = boardHeight
  for i in range(boardWidth ):
      gameBoard.append([])
      for j in range(boardHeight ):
        gameBoard[i].append("x")


def fillGameBoard(snakes: List[Dict],food: List[Dict],boardHeight: int):
  global gameBoard
  
  for snake in snakes:
      headx = (snake["head"]["x"]) 
      heady = (boardHeight - 1) - (snake["head"]["y"]) 
      gameBoard[heady][headx] = "sh"
      for bodyPiece in snake["body"][1:]:
          bodyx = bodyPiece["x"] 
          bodyy = (boardHeight - 1) - bodyPiece["y"] 
          if gameBoard[bodyy][bodyx] == "x":
              gameBoard[bodyy][bodyx] = "sb"
              if snake["body"][-1]["x"] == bodyPiece["x"] and snake["body"][-1]["y"] == bodyPiece["y"]:
                gameBoard[bodyy][bodyx] = "st"
  for f in food:
    foodx = f["x"]
    foody = (boardHeight - 1) - f["y"]
    gameBoard[foody][foodx] = "f"


def nextState(snakes: List[Dict],myMoves: List[str]):
  possibleEnemeySnakeMoves = ["Left","Right","Up","Down"]
  boardCopy = gameBoard.copy()
  for snake in snakes:
    simulateMove("Up",snake,boardCopy)
    if snake["name"] == "ekans":
      """
      here we are going to deal with updating the board for my moves
      """

    else:
      """
      here we are going to deal with updating the board for enemey snake moves
      """

def simulateMove(move: str,snake: List[Dict],board: List[str]):
  global height,width

  boardHeight = height - 1
  boardWidth = width - 1

  headx = snake["head"]["x"]
  heady = snake["head"]["y"]
  tail = snake["body"][-1]
  secondLast = snake["body"][-2]
  consumedFood = False
  if move == "up":
    if  board[(boardHeight  - heady )][headx] == "f":
      consumedFood = True
    
    if not consumedFood:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[boardHeight - heady  ][headx] = "sb"
      if not heady == boardHeight:
        board[(boardHeight - (heady + 1))][headx] = "sh"
        return board
      else:
        return []

  if move == "down":
    if  board[(boardHeight - heady )][headx] == "f":
      consumedFood = True
    
    if not consumedFood:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[(boardHeight - heady)][headx] = "sb"
      if not heady == 0:
        board[(boardHeight - (heady - 1))][headx] = "sh"
        return board
      else:
        return []

    return board

  if move == "left":

    if board[heady][headx - 1] == "f":
      consumedFood = True

    if not consumedFood:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[heady][headx-1] = "sh"
      board[heady][headx] = "sb"
    
    if not headx == 0:
      board[(boardHeight - heady)][headx - 1] = "sh"
      return board
    else:
      return []
  if move == "right":

    if board[heady][headx + 1] == "f":
          consumedFood = True
    if not consumedFood:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[heady][headx+1] = "sh"
      board[heady][headx] = "sb"
      if not headx == boardWidth:
        board[(boardHeight - heady)][headx + 1] = "sh"
        return board
      else:
        return []    
  

def resetGameBoard():
  global gameBoard
  gameBoard = []

def getBoard():
  return gameBoard.copy()