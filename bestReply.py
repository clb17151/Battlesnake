import Board,moveLogic,math
from typing import List, Dict


def BRS(alpha:int, beta:int, depth: int, turn:str,board:List[str],snakes: List[Dict],prevMove: str,mySnake:List[Dict]):
  #print(alpha,beta,depth)
  enemies = snakes[:]
  enemies.pop(0)
  newMove = prevMove
  bestMove = ""

  if depth <= 0:
    score = evaluate(board,mySnake,snakes)
    #print("Line 14: ", score,prevMove)
    return score,prevMove

  if turn == "Max":
    moves = generateMoves(board,mySnake,snakes,turn)
    turn = "Min"

    for move in moves:
      #print("Line 22: ", move)
      newBoard = board[:]
      newBoard,updatedSnake = Board.doMove(move,mySnake,newBoard,0)
      snakes.pop(0)
      snakes.insert(0,updatedSnake)
      newBeta = beta * -1
      newAlpha = alpha *-1
      v,newMove = BRS(newBeta,newAlpha,depth - 1, turn,newBoard,snakes,move,updatedSnake)
      v = -v

      if v >= beta:
        #print("Line 32: ", v,newMove)
        return v,newMove
      #print("Line 34: ", alpha,v)
      alpha = max(alpha,v)
      if alpha == v:
        #print("Line 38:",alpha,beta,v,move)
        bestMove = move

  else:
    moves = []
    for e in enemies:
      moves += [generateMoves(board,e,snakes,turn)]
    turn = "Max"

    for moveSet in moves:
      index = 0
      for move in moveSet:
        #print("Line 50: ",move)
        newBoard = board[:]
        newBoard,updatedSnake = Board.doMove(move,enemies[index],newBoard,index)
        snakes.pop(index+1)
        snakes.insert(index+1,updatedSnake)

        newBeta = beta * -1
        newAlpha = alpha * -1
        v,newMove = BRS(newBeta,newAlpha,depth-1, turn,newBoard,snakes,move,mySnake)
        v = -v
    
        if v >= beta:
          #print("Line 61: ",v,newMove)
          return v,newMove
        #print("Line 63: ", alpha,v)
        alpha = max(alpha,v)
        if alpha == v:
          #print("Line 66:",alpha,beta,v,move)
          bestMove = move
      index += 1

  #print("Line 70: ", alpha,bestMove)
  return alpha,bestMove

  

def evaluate(board: List[str],snake: List[Dict],allSnakes: List[Dict]):
  totalScore = 0
    
  floodfillScore = Board.floodFill(board,snake["head"]["x"],snake["head"]["y"],snake)
  floodfillScore = floodfillScore 
  floodfillScore = math.floor(floodfillScore)
  print("Flood score: ", floodfillScore)
  totalScore += floodfillScore

  if(snake["head"]["x"] == 0 or snake["head"]["x"] == len(board) - 1):
    totalScore += 15
    
  if(snake["head"]["y"] == 0 or snake["head"]["y"] == len(board) - 1):
      totalScore += 15

  if(snake["head"]["x"] == 1 or snake["head"]["x"] == len(board) - 2):
    totalScore += 10
    
  if(snake["head"]["y"] == 1 or snake["head"]["y"] == len(board) - 2):
    totalScore += 10

  if(snake["head"]["x"] > 3 and snake["head"]["x"] < len(board) - 3):
    totalScore -= 15


  if(snake["head"]["y"] > 3 and snake["head"]["y"] < len(board) - 3):
    totalScore -= 15
    
  return totalScore

def generateMoves(board:List[str],snake:List[Dict],enemies:List[Dict],turn):
    
  moves = ["left","up","down","right"]
  moves = moveLogic.avoid_other_snakes(snake["head"],enemies,moves)
  moves = moveLogic.avoid_walls(snake["head"],len(board),len(board),moves)
  if turn == max:
    moves = moveLogic.checkForHeadCollision(snake,enemies,moves)

  return moves

