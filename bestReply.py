import Board,moveLogic,math,copy,random
from typing import List, Dict


def BRS(alpha:int, beta:int, depth: int, turn:str,board:List[str],snakes: List[Dict],prevMove: str,mySnake:List[Dict]):
  enemies = snakes[:]
  enemies.pop(0)
  newMove = prevMove
  bestMove = prevMove
  deadSnakes = []

  if depth <= 0:
    score = evaluate(board,mySnake,snakes)
    return score,prevMove
  if turn == "Max":
    moves = generateMoves(board,mySnake,snakes,turn)
    if moves == []:
      return float("-inf"),prevMove
    turn = "Min"

    for move in moves:

      newBoard = board[:]
      copyOfMe = copy.deepcopy(mySnake)
      newBoard,updatedSnake = Board.doMove(move,copyOfMe,newBoard,0)
      snakes.pop(0)
      snakes.insert(0,updatedSnake)
      newBeta = beta * -1
      newAlpha = alpha *-1
      v,newMove = BRS(newBeta,newAlpha,depth - 1, turn,newBoard,snakes,move,updatedSnake)
    
      v = -v
      if v >= beta:
        return v,newMove
      alpha = max(alpha,v)
      if alpha == v:
        bestMove = move

  else:
    moves = []
    for e in enemies:
      newMoves = [generateMoves(board,e,snakes,turn)]
      if newMoves == []:
        print("dead snake")
        deadSnakes += e
      else:
        moves += newMoves
    turn = "Max"

    for moveSet in moves:
      index = 0
      for move in moveSet:
        newBoard = board[:]
        newSnakes = snakes[:]
        currentSnake = copy.deepcopy(enemies[index])
        newBoard,updatedSnake = Board.doMove(move,currentSnake,newBoard,index)
        if not updatedSnake == []:
          newSnakes.pop(index+1)
          newSnakes.insert(index+1,updatedSnake)
     
        newBeta = beta * -1
        newAlpha = alpha * -1
        v,newMove = BRS(newBeta,newAlpha,depth-1, turn,newBoard,newSnakes,move,mySnake)
        v = -v
  
        if v >= beta:
          return v,newMove
        alpha = max(alpha,v)
        if alpha == v:
          bestMove = move
      index += 1
  return alpha,bestMove

  

def evaluate(board: List[str],snake: List[Dict],allSnakes: List[Dict]):

  totalScore = 0
    
  floodfillScore = Board.floodFill(board,snake["head"]["x"],snake["head"]["y"],snake)
  floodfillScore = floodfillScore 
  floodfillScore = math.floor(floodfillScore)
  totalScore += floodfillScore

  if snake["head"]["x"] == 0 or snake["head"]["x"] == len(board)-1:
    totalScore -10
  if snake["head"]["y"] == 0 or snake["head"]["y"] == len(board)-1:
    totalScore -10

  if snake["head"]["x"] == 1 or snake["head"]["x"] == len(board)-2:
    totalScore -5
  if snake["head"]["y"] == 1 or snake["head"]["y"] == len(board)-2:
    totalScore -5

  if snake["head"]["x"] > len(board)/3 or snake["head"]["x"] < len(board)/3:
    totalScore +10
  if snake["head"]["y"] == len(board)/3 or snake["head"]["y"] < len(board)/3:
    totalScore +10

  if snake["health"] < 75:
    totalScore -10
  if snake["health"] < 50:
    totalScore -20
  if snake["health"] < 25:
    totalScore -50

  return totalScore

def generateMoves(board:List[str],snake:List[Dict],enemies:List[Dict],turn):

  moves = ["left","up","down","right"]
  random.shuffle(moves)
  moves = moveLogic.avoid_other_snakes(snake["head"],enemies,moves)
  moves = moveLogic.avoid_walls(snake["head"],Board.getWidth(),Board.getHeight(),moves)
  if turn == max:
    moves = moveLogic.checkForHeadCollision(snake,enemies,moves)


  return moves

