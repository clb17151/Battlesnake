import moveLogic, Board, itertools,copy
from typing import List, Dict


def maxn(board:List[str], depth:int,snakes: List[Dict],snakeIndex: int ):
 
  if snakeIndex == len(snakes)-1:
    snakeIndex = 0
    depth -= 1

  if depth == 0 or len(snakes) <= 1:
    return evaluate(board,snakes)

  possibleMoves = nextPossibleMoves(board,snakes)

  childNodes = []
  oldBoard = copy.deepcopy(Board.getBoard())

  for moves in possibleMoves:
    Board.setBoard(oldBoard)
    newBoard = copy.deepcopy(Board.getBoard())
    newBoard,moveSet = Board.simulateMoves(moves,snakes,newBoard)
    childNodes.append(newBoard)


  best = maxn(childNodes[0],depth,snakes,snakeIndex+1)

  for child in childNodes[1:]:
    current = maxn(child,depth,snakes,snakeIndex+1)
    if current[snakeIndex] > best[snakeIndex]:
      best = current 
  return best

      

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
  
  return moveTuples

def evaluate(board: List[str],snakes: List[Dict]):

  for s in snakes:
    floodfillScore = Board.floodFill(board,s["head"]["x"],s["head"]["y"],s)
  return [5,5]
