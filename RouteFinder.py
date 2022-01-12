from typing import List, Dict
import Board

def simulateMove(my_head : Dict[str,int], possible_moves : List[str]):
  newPositions = []
  for move in possible_moves:
    if(move == "up" and my_head["y"] < Board.getHeight() ):
      xCoOrd = my_head["x"] 
      yCoOrd = my_head["y"] + 1
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "down" and my_head["y"] > 0):
      xCoOrd = my_head["x"] 
      yCoOrd = my_head["y"] - 1
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "left" and my_head["x"] > 0):
      xCoOrd = my_head["x"] - 1
      yCoOrd = my_head["y"] 
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "right" and my_head["x"] < Board.getWidth()):
      xCoOrd = my_head["x"] +1
      yCoOrd = my_head["y"] 
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
  
  return newPositions

def findClosestFood(food: List, head: Dict[str,int]):
  closestFood = food[0]
  smallestDistance = 200

  for f in food:
    newDistance = (abs((f["x"] - head["x"]))) + ( abs((f["y"] - head["y"])))

    if newDistance < smallestDistance:
      smallestDistance = newDistance
      closestFood = f
      
  return closestFood

def bfsForFood(foodCoOrd: Dict[str,int], head: Dict[str,int],possible_moves:List[str]):
  queue = [[head]]
  visited = []
  while queue : 
    path = queue.pop(0)
    currentCoOrd = path[-1]
    if(currentCoOrd == foodCoOrd):
      return path
    else:
      newPositions = simulateMove(currentCoOrd,possible_moves)
      for pos in newPositions:
        if(not pos in visited):
          visited.append(pos)
          newList = list(path)
          newList.append(pos)
          queue.append(newList)
  return []    

def dfsForFood(foodCoOrd: Dict[str,int], node: Dict[str,int],possible_moves:List[str]):

  queue = [[node]]
  visited = []
  while queue: 
    path = queue.pop(0)
    currentCoOrd = path[-1]
    if(currentCoOrd == foodCoOrd):
      return path
    else:
      newPositions = simulateMove(currentCoOrd,possible_moves)
      neighbours = []
      for pos in newPositions:
        if(not pos in visited):
          visited.append(pos)
          newList = list(path)
          newList.append(pos)
          neighbours.append(newList)
      queue = neighbours + queue

  return [] 
