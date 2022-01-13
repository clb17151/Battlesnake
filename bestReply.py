import Board,moveLogic,copy,random,RouteFinder
from typing import List, Dict


def BRS(alpha:int, beta:int, depth: int, turn:str,board:List[str],snakes: List[Dict],prevMove: str,mySnake:List[Dict]):
  Board.prettyPrint(board)
  print(alpha,beta,depth,turn,prevMove)
  enemies = snakes[:]
  enemies.pop(0)
  newMove = prevMove
  bestMove = prevMove
  deadSnakes = []

  if depth <= 0:
    score = evaluate(board,mySnake,snakes)
    print("Depth < 0, Score is: ",score)
    return score,prevMove
  if turn == "Max":
    moves = generateMoves(board,mySnake,snakes,turn)
    if moves == []:
      print("No moves for Max: ")
      print(alpha,beta,depth,turn,prevMove)
      return float('-inf'),prevMove
    turn = "Min"

    for move in moves:
      print("At Ekans move")
      print("Current move: ",move)
      Board.prettyPrint(board)

      newBoard = board[:]
      copyOfMe = copy.deepcopy(mySnake)
      newBoard,updatedSnake = Board.doMove(move,copyOfMe,newBoard,0)
      print("After move")
      Board.prettyPrint(newBoard)

      snakes.pop(0)
      snakes.insert(0,updatedSnake)
      newBeta = beta * -1
      newAlpha = alpha * -1
      print("Calling BRS at line 40: ")
      print(newBeta,newAlpha,depth-1,turn,move,prevMove)

      v,newMove = BRS(newBeta,newAlpha,depth - 1, turn,newBoard,snakes,move,updatedSnake)
      v = -v
      print("BRS at 45 returned value: ",v,"With move returned: ",newMove)
      print(alpha,beta)
      if v >= beta:
        print("V >= beta at line 48, Returning: ",v,newMove)
        return v,newMove
      alpha = max(alpha,v)
      if alpha == v:
        print("V > alpha at line 52, New best move: ",move)
        bestMove = move

  else:
    moves = []
    Board.prettyPrint(board)
    for e in enemies:
      print(e['head'])
      newMoves = [generateMoves(board,e,snakes,turn)]
      print(newMoves)
      if newMoves == []:
        print("dead snake")
        deadSnakes += e
      else:
        moves += newMoves
    turn = "Max"

    index = 0
    for moveSet in moves:
      for move in moveSet:
        print("Current move: ",move)
        print("For snake: ",enemies[index]['id'])
        Board.prettyPrint(board)

        newBoard = board[:]
        newSnakes = snakes[:]
        currentSnake = copy.deepcopy(enemies[index])
        newBoard,updatedSnake = Board.doMove(move,currentSnake,newBoard,index)
        print("After move")
        Board.prettyPrint(newBoard)

        if not updatedSnake == []:
          newSnakes.pop(index+1)
          newSnakes.insert(index+1,updatedSnake)
     
        newBeta = beta * -1
        newAlpha = alpha * -1
        print("Calling BRS at line 88: ")
        print(newBeta,newAlpha,depth-1,turn,move,prevMove)
        v,newMove = BRS(newBeta,newAlpha,depth-1, turn,newBoard,newSnakes,move,mySnake)
        print("BRS at 89 returned value: ",v,"With move returned: ",newMove)
        print(alpha,beta)

        v = -v
        if v >= beta:
          print("V >= beta at line 94, Returning: ",v,newMove)
          return v,newMove
        alpha = max(alpha,v)
        if alpha == v:
          print("V > alpha at line 98, New best move: ",prevMove)
          bestMove = prevMove
      index += 1
  return alpha,bestMove

 

  

def evaluate(board: List[str],snake: List[Dict],allSnakes: List[Dict]):
  totalScore = 0
  
  distToFood = RouteFinder.findClosestFood(Board.getFood(),snake['head'])[1]

  totalScore += len(board) - distToFood

  myLength = len(snake["body"])

  totalScore += myLength
    
  floodfillScore = Board.floodFill(board,snake["head"]["x"],snake["head"]["y"],snake)
  totalScore += floodfillScore

  if floodfillScore < myLength:
    return float("-inf")
  else:
    totalScore += floodfillScore

  if snake["head"]["x"] == 0 or snake["head"]["x"] == len(board)-1:
    totalScore -5
  if snake["head"]["y"] == 0 or snake["head"]["y"] == len(board)-1:
    totalScore -5

  if snake["head"]["x"] == 1 or snake["head"]["x"] == len(board)-2:
    totalScore -2
  if snake["head"]["y"] == 1 or snake["head"]["y"] == len(board)-2:
    totalScore -2

  if snake["head"]["x"] > len(board)/3 or snake["head"]["x"] < len(board)/3:
    totalScore +10
  if snake["head"]["y"] == len(board)/3 or snake["head"]["y"] < len(board)/3:
    totalScore +10

  totalScore += Board.getNumberOfFreeSquares(board,snake["head"]["x"],snake["head"]["y"])

  for s in allSnakes:
    if not s['id'] == snake['id']:
      if len(s['body']) < myLength:
        totalScore += 10
      else:
        totalScore -= 5

    freeSquares = Board.getNumberOfFreeSquares(board,s['head']['x'],s['head']['y'])
    totalScore += (freeSquares - 4)

  if snake['health'] > 90:
    totalScore += 15
  if snake['health'] > 75:
    totalScore += 5
  if snake['health'] < 50:
    totalScore -= 20
  
  return totalScore

def generateMoves(board:List[str],snake:List[Dict],enemies:List[Dict],turn):
  moves = ["left","up","down","right"]
  random.shuffle(moves)
  moves = moveLogic.avoid_other_snakes(snake["head"],enemies,moves)
  moves = moveLogic.avoid_walls(snake["head"],Board.getWidth(),Board.getHeight(),moves)

  if turn == max:
    moves = moveLogic.checkForHeadCollision(snake,enemies,moves)


  return moves

