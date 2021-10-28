from typing import List, Dict

def simulateMove(my_head : Dict[str,int], possible_moves : List[str]):
  newPositions = []
  for move in possible_moves:
    if(move == "up"):
      xCoOrd = my_head["x"] 
      yCoOrd = my_head["y"] + 1
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "down"):
      xCoOrd = my_head["x"] 
      yCoOrd = my_head["y"] - 1
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "left"):
      xCoOrd = my_head["x"] - 1
      yCoOrd = my_head["y"] 
      newPos = {
        "x": xCoOrd,
        "y": yCoOrd
      }
      newPositions.append(newPos)
    if(move == "right"):
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
  count = 0
  while queue and count < 100: 
    count += 1
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


