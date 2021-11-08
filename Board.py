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
      if not heady == boardHeight and (not board[(boardHeight - (heady+1))][headx] == "sb") and (not board[(boardHeight - (heady+1))][headx] == "sh"):
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
      if not heady == 0 and (not board[(boardHeight - (heady-1))][headx] == "sb") and (not board[(boardHeight - (heady-1))][headx] == "sh"):
        board[(boardHeight - (heady - 1))][headx] = "sh"
        return board
      else:
        return []

    return board

  if move == "left":

    if not headx == 0:
      if board[heady][headx - 1] == "f":
        consumedFood = True

    if not consumedFood and not headx == 0:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[heady][headx-1] = "sh"
      board[heady][headx] = "sb"
    
      if not headx == 0 and (not board[(boardHeight - (heady))][headx-1] == "sb") and (not board[(boardHeight - (heady))][headx - 1] == "sh"):
        board[(boardHeight - heady)][headx - 1] = "sh"
      return board
    else:
      return []


  if move == "right":

    if not headx == boardWidth:
      if board[heady][headx + 1] == "f":
        consumedFood = True

    if not consumedFood and not headx == boardWidth:
      board[(boardHeight  - tail["y"])][tail["x"]] = "x"
      board[(boardHeight  - secondLast["y"])][secondLast["x"]] = "st"
      board[heady][headx+1] = "sh"
      board[heady][headx] = "sb"
      if not headx == boardWidth and (not board[(boardHeight - (heady))][headx+1] == "sb") and (not board[(boardHeight - (heady))][headx + 1] == "sh"):
        board[(boardHeight - heady)][headx + 1] = "sh"
        return board
    else:
      return []    
  

def floodFill(board:List[str],xcord:int,ycord,snake:List[Dict]):

  area = 0
  queue = [[ycord,xcord]]
  visited = []
  while queue:
    n = queue.pop()
    if n not in visited:
      visited.append(n)
      if n[0] == len(board) or n[1] == len(board):
          length = len(board)
      else:
        length = len(board) - 1
      if board[(length-n[0])][n[1]] == "x" or board[(length-n[0])][n[1]] == "f":  
        area += 1
        if n[1] != length and not [n[0],n[1]+1] in visited:
          queue.append([n[0],n[1] + 1])
        if n[1] != 0 and not [n[0],n[1]-1] in visited :
          queue.append([n[0],n[1] - 1])
        if n[0] != length and not [n[0] + 1,n[1]] in visited :
          queue.append([n[0] + 1,n[1]])
        if n[0] != 0 and not [n[0] - 1,n[1]] in visited  :
          queue.append([n[0] - 1,n[1]])
  return area

def resetGameBoard():
  global gameBoard
  gameBoard = []

def getBoard():
  return gameBoard.copy()