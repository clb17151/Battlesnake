from typing import List, Dict
import copy

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



def simulateMoves(moves:List[str],snakes:List[Dict],board:List[Dict]):
  global height,width
  gameBoard = board[:]

  index = 0
  for m in moves:
    consumedFood = False
    snakeIndexAtCollision = -1

    currentSnake = snakes[index]
    tail = currentSnake["body"][-1]
    secondLast = currentSnake["body"][-2]
    headx = currentSnake["head"]["x"]
    heady = currentSnake["head"]["y"]
    #print("Movelist: ",moves)
    #print("Printing at move: ",m)
    #print(currentSnake)

    if m == "up":
      if not heady == height - 1:
          if gameBoard[(height  - heady )-1][headx] == "f":
            consumedFood = True
          if not consumedFood:
            gameBoard[((height  - tail["y"]) - 1)][tail["x"]] = "x"
            gameBoard[(height  - secondLast["y"]) - 1][secondLast["x"]] = "st"
            gameBoard[(height - heady) - 1 ][headx] = "sb"
          if (not heady == (height - 1)) and (not gameBoard[((height - heady) - 1)][headx] == "sb") and (not gameBoard[(height - heady - 1)][headx] == "sh"):
            gameBoard[(height - heady) - 1 ][headx] = "sh"
          else:
            gameBoard[(height - heady) - 2][headx] = "sh"
            snakeIndexAtCollision = index


    if m == "down":
      if not heady == 0:
        if  gameBoard[(height - (heady) )][headx] == "f":
          consumedFood = True
        
        if not consumedFood and not heady == 0:
          gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
          gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
          gameBoard[(height - heady) - 1][headx] = "sb"
        if not heady == 0 and (not gameBoard[(height - (heady))][headx] == "sb") and (not gameBoard[(height - (heady))][headx] == "sh"):
          gameBoard[(height - heady)][headx] = "sh"
        else:
          gameBoard[(height - heady)][headx] = "sh"
          snakeIndexAtCollision = index


    if m == "left":

      if not headx == 0:
        if gameBoard[heady][headx - 1] == "f":
          consumedFood = True

      if not consumedFood and not headx == 0:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[((height - heady) -1)][headx-1] = "sh"
        gameBoard[((height - heady) -1)][headx] = "sb"
      
      if not headx == 0 and (not gameBoard[(height - (heady))-1][headx-1] == "sb") and (not gameBoard[(height - (heady))-1][headx - 1] == "sh"):
        gameBoard[(height - heady)-1][headx - 1] = "sh"
      else:
        gameBoard[(height - heady)-1][headx - 1] = "sh"
        snakeIndexAtCollision = index



    if m == "right":

      if not headx == width - 1:
        if gameBoard[heady][headx + 1] == "f":
          gameBoard = True

      if not consumedFood and not headx == width - 1:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[((height - heady) -1)][headx+1] = "sh"
        gameBoard[((height - heady) -1)][headx] = "sb"
      if not headx == width - 1 and (not gameBoard[(height - (heady))-1][headx+1] == "sb") and (not gameBoard[(height - (heady))-1][headx + 1] == "sh"):
        gameBoard[(height - heady)-1][headx + 1] = "sh"
      else:
        gameBoard[(height - heady)-1][headx + 1] = "sh"
        snakeIndexAtCollision = index



    index += 1
    #print(gameBoard)
  return gameBoard,snakeIndexAtCollision


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
  return gameBoard

def getHeight():
  global width
  return height

def getWidth():
  global width
  return width

def setBoard(board:List[str]):
  global gameBoard
  gameBoard = copy.deepcopy(board)