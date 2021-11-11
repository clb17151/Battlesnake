import moveLogic, Board, math, moveLogic
from typing import List, Dict


def maxn(board:List[str], depth:int,snakes: List[Dict],snakeIndex: int ):
 
  if snakeIndex == 3:
    snakeIndex = -1
    depth -= 1

  if depth == 0:
    return evaluate(board,snakes)

  childNodes = nextStates(board,snakes)

  bestScore = 0
  for child in childNodes:
    evals = maxn(child,depth,snakes,snakeIndex+1)
    if evals[snakeIndex] > bestScore:
      bestVector = evals
      bestScore = evals[snakeIndex]

  return bestVector
      
      

def nextStates(board: List[str],snakes:List[Dict]):
  snakeAndMove = {}
  moveList = []  
  for s in snakes:
    moves = ["left","up","down","right"]
    moves = moveLogic.avoid_other_snakes(s["head"],snakes,moves)
    moves = moveLogic.avoid_walls(s["head"],Board.getWidth(),Board.getHeight(),moves)
    moveList.append(moves)

  
    
  

def evaluate(board: List[str],snakes: List[Dict]):
  return [5,5,5,5]

def chance(board: List[str], depth: int):
  return 0




