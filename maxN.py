import moveLogic, Board, itertools, copy
from typing import List, Dict

def maxn(board:List[str], depth:int,snakes: List[Dict],snakeIndex: int):

  newDepth = depth
  newIndex = snakeIndex

  print(depth,len(snakes),snakeIndex)

  if (snakeIndex == len(snakes)-1):
    newDepth -= 1
    newIndex = -1

  if depth == 0 or len(snakes) <= 1:
    print("Return here")
    return evaluate(board,snakes)

  possibleMoves = nextPossibleMoves(board,snakes)
  childNodes = []

  for moves in possibleMoves:
    newBoard = copy.deepcopy(board)
    newBoard,moveSet,updatedSnakes = Board.simulateMoves(moves,snakes,newBoard)
    childNodes.append([newBoard,moveSet,updatedSnakes])

  best = maxn(childNodes[0][0],newDepth,childNodes[0][2],(newIndex + 1))

  for child in childNodes[1:]:
    current = maxn(child[0],newDepth,child[2],(newIndex + 1))
    if(current[newIndex] > best[newIndex]):
      best = current

  return best

    

def nextPossibleMoves(board: List[str],snakes:List[Dict]):
  moveList = [] 
  for s in snakes:
    moves = ["left","up","down","right"]
    moves = moveLogic.avoid_other_snakes(s["head"],snakes,moves)
    moves = moveLogic.avoid_walls(s["head"],Board.getWidth(),Board.getHeight(),moves)

    if moves == []:
      moveList.append("trapped")
    else:
      moveList.append(moves)
  
  if len(snakes) == 4:
    moveTuples = [x for x in itertools.product(moveList[0],moveList[1],moveList[2],moveList[3])]
  elif len(snakes) == 3:
    moveTuples =  [x for x in itertools.product(moveList[0],moveList[1],moveList[2])]
  elif len(snakes) == 2:
    moveTuples = [x for x in  itertools.product(moveList[0],moveList[1])]
  return moveTuples

  branchFactor = 0
  for m in moveTuples:
    branchFactor += 1
  
  print(branchFactor)

def evaluate(board: List[str],snakes: List[Dict]):

  scores = []
  for s in snakes:
    floodfillScore = Board.floodFill(board,s["head"]["x"],s["head"]["y"],s)
    scores.append(floodfillScore)

  return scores





