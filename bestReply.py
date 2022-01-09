import Board,moveLogic,math
from typing import List, Dict


def BRS(alpha:int, beta:int, depth: int, turn:str,board:List[str],snakes: List[Dict],bestMove: str,mySnake:List[Dict]):
  enemies = snakes[:]
  enemies.pop(0)

  if depth <= 0:
    score = evaluate(board,mySnake,snakes)
    return score,bestMove

  if turn == "Max":
    moves = generateMoves(board,mySnake,snakes,turn)
    turn = "Min"

    for move in moves:
      newBoard = board[:]
      newBoard,updatedSnake = Board.doMove(move,mySnake,newBoard,0)
      snakes.pop(0)
      snakes.insert(0,updatedSnake)
      newBeta = beta * -1
      newAlpha = alpha *-1
      v,bestMove = BRS(newBeta,newAlpha,depth - 1, turn,newBoard,snakes,move,updatedSnake)
      v = -(v)

      if v >= beta:
        return v,bestMove
      alpha = max(alpha,v)

  else:
    moves = []
    for e in enemies:
      moves += [generateMoves(board,e,snakes,turn)]
    turn = "Max"

    for moveSet in moves:
      index = 0
      for move in moveSet:
        newBoard = board[:]
        newBoard,updatedSnake = Board.doMove(move,enemies[index],newBoard,index)
        snakes.pop(index+1)
        snakes.insert(index+1,updatedSnake)

        newBeta = beta * -1
        newAlpha = alpha * -1
        v,bestMove = BRS(newBeta,newAlpha,depth-1, turn,newBoard,snakes,move,mySnake)
        v = -(v)
    
        if v >= beta:
          return v,bestMove
        alpha = max(alpha,v)
      index += 1
  
  return alpha,bestMove

  

def evaluate(board: List[str],snake: List[Dict],allSnakes: List[Dict]):
  totalScore = 0
    
  floodfillScore = Board.floodFill(board,snake["head"]["x"],snake["head"]["y"],snake)
  floodfillScore = floodfillScore 
  floodfillScore = math.floor(floodfillScore)
  totalScore += floodfillScore

  if(snake["head"]["x"] == 0 or snake["head"]["x"] == len(board) - 1):
    totalScore -= 15
    
  if(snake["head"]["y"] == 0 or snake["head"]["y"] == len(board) - 1):
      totalScore -= 15

  if(snake["head"]["x"] > 3 and snake["head"]["x"] < len(board) - 1):
    totalScore += 15
  

  if(snake["head"]["y"] > 3 and snake["head"]["y"] < len(board) - 1):
    totalScore += 15
    
  return totalScore

def generateMoves(board:List[str],snake:List[Dict],enemies:List[Dict],turn):
    
  moves = ["left","up","down","right"]
  moves = moveLogic.avoid_other_snakes(snake["head"],enemies,moves)
  moves = moveLogic.avoid_walls(snake["head"],len(board),len(board),moves)
  if turn == max:
    moves = moveLogic.checkForHeadCollision(snake,enemies,moves)

  return moves

