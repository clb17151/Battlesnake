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



"""def simulateMoves(moves:List[str],snakes:List[Dict],board:List[str]):
  global height,width
  gameBoard = copy.deepcopy(board)
  index = 0
  for m in moves:
    consumedFood = False
    currentSnake = snakes[index]
    tail = currentSnake["body"][-1]
    secondLast = currentSnake["body"][-2]
    headx = currentSnake["head"]["x"]
    heady = currentSnake["head"]["y"]
    updatedSnakes = snakes[:]


    if m == "up":
      if not heady == height - 1:
          if gameBoard[(height  - heady )-1][headx] == "f":
            consumedFood = True
          if not consumedFood:
            gameBoard[((height  - tail["y"]) - 1)][tail["x"]] = "x"
            gameBoard[(height  - secondLast["y"]) - 1][secondLast["x"]] = "st"
            gameBoard[(height - heady) - 1 ][headx] = "sb"
          if (not heady == (height - 1)):
            gameBoard[(height - heady) - 2 ][headx] = "sh"
      updatedSnakes = updateSnakes(gameBoard,snakes,m,index,consumedFood)


    if m == "down":
      if not heady == 0:
        if  gameBoard[(height - (heady) )][headx] == "f":
          consumedFood = True
        
        if not consumedFood and not heady == 0:
          gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
          gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
          gameBoard[(height - heady) - 1][headx] = "sb"
        if not heady == 0:
          gameBoard[(height - heady)][headx] = "sh"

      updatedSnakes = updateSnakes(gameBoard,snakes,m,index,consumedFood)

    if m == "left":
      if not headx == 0:
        if gameBoard[heady][headx - 1] == "f":
          consumedFood = True
      if not consumedFood and not headx == 0:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[((height - heady) -1)][headx-1] = "sh"
        gameBoard[((height - heady) -1)][headx] = "sb"
      
      if not headx == 0:
        gameBoard[(height - heady)-1][headx - 1] = "sh"
      updatedSnakes = updateSnakes(gameBoard,snakes,m,index,consumedFood)


    if m == "right":
      if not headx == width - 1:
        if gameBoard[heady][headx + 1] == "f":
          consumedFood = True
      if not consumedFood and not headx == width - 1:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[((height - heady) -1)][headx+1] = "sh"
        gameBoard[((height - heady) -1)][headx] = "sb"
      if not headx == width - 1:
        gameBoard[(height - heady)-1][headx + 1] = "sh"
      updatedSnakes = updateSnakes(gameBoard,snakes,m,index,consumedFood)
      
    index += 1
  return gameBoard,moves,updatedSnakes
"""
def updateSnakes(board:List[str],snake:List[Dict],move:str,index:int,consumedFood:bool):
  global height,width
  updatedSnake = copy.copy(snake)
  secondLast = updatedSnake["body"][-2]
  headx = updatedSnake["head"]["x"]
  heady = updatedSnake["head"]["y"]
  if move == "up" and heady != len(board)-1:
      newHead = {"x":headx,"y":heady+1}
  elif move == "down" and heady != 0:
      newHead = {"x":headx,"y":heady-1}

  elif move == "left" and headx != 0:
    newHead = {"x":headx - 1,"y":heady}

  elif move == "right" and headx != len(board)-1:
    newHead = {"x":headx + 1, "y":heady}

  else:
    return []

  if not consumedFood:
    updatedSnake["head"] = newHead
    updatedSnake["body"].insert(0,newHead)
    updatedSnake["body"].pop(-1)

  else: 
    updatedSnake["head"] = newHead
    updatedSnake["body"].insert(0,newHead)
    updatedSnake["body"].pop(-1)
    updatedSnake["body"].insert(-1,secondLast)
  
  length = len(updatedSnake["body"])
  updatedSnake["length"] = length
  return updatedSnake

    
def doMove(move:str,snake:List[Dict],board:List[str],index:int):

  global height,width
  gameBoard = copy.deepcopy(board)
  consumedFood = False
  tail = snake["body"][-1]
  secondLast = snake["body"][-2]
  headx = snake["head"]["x"]
  heady = snake["head"]["y"]
  updatedSnake = []


  if move == "up":
    if not heady == height - 1:
      if gameBoard[(height  - heady )-2][headx] == "f":
        consumedFood = True
      if not consumedFood:
        gameBoard[((height  - tail["y"]) - 1)][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"]) - 1][secondLast["x"]] = "st"
        gameBoard[(height - heady) - 1 ][headx] = "sb"
        gameBoard[(height - heady) - 2 ][headx] = "sh"
      updatedSnake = updateSnakes(gameBoard,snake,move,index,consumedFood)


  if move == "down":
    if not heady == 0:
      if  gameBoard[(height - (heady) )][headx] == "f":
        consumedFood = True
      if not consumedFood and not heady == 0:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[(height - heady) - 1][headx] = "sb"
        gameBoard[(height - heady)][headx] = "sh"
      updatedSnake = updateSnakes(gameBoard,snake,move,index,consumedFood)


  if move == "left":
    if not headx == 0:

      if gameBoard[heady][headx - 1] == "f":
        consumedFood = True
    if not consumedFood:
      gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
      gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
      gameBoard[((height - heady) -1)][headx-1] = "sh"
      gameBoard[((height - heady) -1)][headx] = "sb"
    updatedSnake = updateSnakes(gameBoard,snake,move,index,consumedFood)


  if move == "right":

    if not headx == width - 1:
      if gameBoard[heady][headx + 1] == "f":
        consumedFood = True
      if not consumedFood:
        gameBoard[(height  - tail["y"])-1][tail["x"]] = "x"
        gameBoard[(height  - secondLast["y"])-1][secondLast["x"]] = "st"
        gameBoard[((height - heady) -1)][headx+1] = "sh"
        gameBoard[((height - heady) -1)][headx] = "sb"
      updatedSnake = updateSnakes(gameBoard,snake,move,index,consumedFood)


  return gameBoard,updatedSnake



def floodFill(board:List[str],xcord:int,ycord,snake:List[Dict]):
  global height,width
  area = 0
  length = width
  queue = []
  if ycord != (length - 1):
    queue.append([ycord+1,xcord])
  if ycord != 0:
    queue.append([ycord-1,xcord])
  if xcord != (length - 1):
    queue.append([ycord,xcord+1])
  if xcord != 0:
    queue.append([ycord,xcord-1])

  visited = []
  while queue:
    n = queue.pop()
    if n not in visited:
      visited.append(n)

      if board[((length-n[0]) - 1)][n[1]] == "x" or board[((length-n[0]) - 1)][n[1]] == "f":  
        area += 1

      #Deals with adding Right square
      if n[1] != (length - 1) and not [n[0],n[1]+1] in visited and (board[((length-n[0]) - 1)][n[1]+1] == "x" or board[((length-n[0]) - 1)][n[1]+1] == "f"):
        queue.append([n[0],n[1] + 1])

      #Deals with adding Left square
      if n[1] != 0 and not [n[0],n[1]-1] in visited and (board[((length-n[0]) - 1)][n[1]-1] == "x" or board[((length-n[0]) - 1)][n[1]-1] == "f"):
        queue.append([n[0],n[1] - 1])

      #Deals with adding Up square
      if n[0] != (length - 1) and not [n[0] + 1,n[1]] in visited and (board[((length-n[0]) - 1)][n[1]] == "x" or board[((length-n[0]) - 1)][n[1]] == "f"):
        queue.append([n[0] + 1,n[1]])

      #Deals with adding Down square
      if n[0] != 0 and not [n[0] - 1,n[1]] in visited and (board[((length-n[0]) - 1)][n[1]] == "x" or board[((length-n[0]) - 1)][n[1]] == "f"):
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

def prettyPrint(board:List[str]):
  print("\n")
  for r in board:
    print(r)
    
def printToFile(board:List[str]):
  #Placeholder
  f = open("prettyPrint.txt", "a")
  f.write("\n")
  for r in board:
    f.write("\n")
    for k in r:
      f.write(k)

  f.close()   