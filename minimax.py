import moveLogic, Board, math
from typing import List, Dict,Queue


def expectiminimax(board: List[str],depth: int,possibleMoves: List[str],snake: List[Dict]):

  boardCopy = board[:]
  bestMove = None

  if depth == 0 :
    return bestMove,evaluate(board)

  #Dont think board == [] should be here as wouldnt represent win / loss
  elif possibleMoves == [] or board == []:
    return bestMove,0
  else:
    value = -math.inf
    for m in possibleMoves:
      boardCopy = Board.simulateMove(m,snake,boardCopy)
      chanceV = chance(boardCopy,depth-1)
      if chanceV > value:
        value = chanceV
        bestMove = m
  return bestMove,value



def evaluate(board: List[str]):
  if board == []:
    return 0

def chance(board: List[str], depth: int):
  return 0




