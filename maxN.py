import moveLogic, Board, itertools,copy
from typing import List, Dict


def maxn(board:List[str], depth:int,snakes: List[Dict],snakeIndex: int ):
 
  if snakeIndex == 3:
    snakeIndex = -1
    depth -= 1

  if depth == 0:
    return evaluate(board,snakes)

  possibleMoves = nextPossibleMoves(board,snakes)

  bestScore = 0
  childNodes = []
  oldBoard = copy.deepcopy(Board.getBoard())

  for moves in possibleMoves:
    Board.setBoard(oldBoard)
    newBoard = Board.getBoard()[:]
    newBoard = Board.simulateMoves(moves,snakes,newBoard)
    childNodes.append(newBoard)

  for c in childNodes:
    print(c)      
      
  """
  for child in childNodes:
   
    evals = maxn(child,depth,snakes,snakeIndex+1)
    if evals[snakeIndex] > bestScore:
      bestVector = evals
      bestScore = evals[snakeIndex]
  """

  return 0
      
      

def nextPossibleMoves(board: List[str],snakes:List[Dict]):
  moveList = [] 
  for s in snakes:
    moves = ["left","up","down","right"]
    moves = moveLogic.avoid_other_snakes(s["head"],snakes,moves)
    moves = moveLogic.avoid_walls(s["head"],Board.getWidth(),Board.getHeight(),moves)
    moveList.append(moves)
  
  if len(snakes) == 4:
    moveTuples = [x for x in itertools.product(moveList[0],moveList[1],moveList[2],moveList[3])]
  elif len(snakes) == 3:
    moveTuples =  [x for x in itertools.product(moveList[0],moveList[1],moveList[2])]
  elif len(snakes) == 2:
    moveTuples = [x for x in  itertools.product(moveList[0],moveList[1])]
  
  branchFactor = 0
  for m in moveTuples:
    branchFactor += 1

  print (branchFactor)
  
  return moveTuples

def evaluate(board: List[str],snakes: List[Dict]):
  return [5,5,5,5]





