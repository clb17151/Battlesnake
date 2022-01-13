"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python tests.py -v


"""
import unittest
import moveLogic,Board,bestReply


class AvoidHeadCollisions(unittest.TestCase):
    def test_head_collision_right(self):
   
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'], 
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'sh'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'], 
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'], 
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}], 'head': {'x': 10, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["up","down","left"], result_moves)


    def test_head_collision_left(self):
   
        # Arrange
        board = [
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'sh', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 8}], 'head': {'x':6, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["up","down","right"], result_moves)

    def test_head_collision_down(self):
        # Arrange
        board = [
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'st', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y': 7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["up","right"], result_moves)

    def test_head_collision_up(self):
      # Arrange
      board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'], 
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x'], 
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x'], 
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'st', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
      
      my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y':7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

      snakes =[{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y':7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x':8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]


      possible_moves = ["up", "down", "left", "right"]

      # Act
      result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

      # Assert
      self.assertEqual(["down","left"], result_moves)

    def test_head_collision_bigger_snake(self):
      # Arrange
        board = [
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'sh', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
          ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
          ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10},{'x':9,'y':10}], 'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10},{'x':9,'y':10}], 'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 8}], 'head': {'x':6, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["up","down","left","right"], result_moves)


    def test_head_collision_up2(self):
  
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x'], 
        ['x', 'x', 'x', 'x', 'sh', 'sb', 'x'],
        ['x', 'x', 'sb', 'sb', 'x', 'sb', 'x'],
        ['x', 'x', 'sb', 'sb', 'sh', 'sb', 'x'], 
        ['x', 'x', 'st', 'x', 'x', 'sb', 'x'], 
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 4, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}], 'head': {'x': 4, 'y': 3}, 'length': 6, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 4, 'y': 6}, {'x': 3, 'y': 3}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}], 'head': {'x': 4, 'y': 3}, 'length': 6, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 4, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}], 'head': {'x': 4, 'y': 5}, 'length': 8, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["down","left","right"], result_moves)


    def test_eval(self):
   
        # Arrange
        board = [
        ['x',  'x', 'x',  'x', 'x',  'x', 'x', 'x', 'x', 'x', 'x'], 
        ['x', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sh', 'sb', 'x'],
        ['x', 'sh',  'x',  'x',  'x',  'x',  'x',  'sb', 'x', 'sb', 'x'],
        ['x',  'x',  'x',  'x',  'x',  'x',  'x',  'sb', 'x', 'sb', 'x'], 
        ['x',  'x',  'x',  'x',  'x',  'x',  'st', 'sb', 'x', 'sb', 'x'], 
        ['f',  'x',  'x',  'x',  'x',  'x',  'x',  'x',  'st', 'sb', 'x'],
        ['sb', 'sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 1, 'y': 4}, {'x': 2, 'y': 4}], 'head': {'x': 1, 'y': 0}, 'length': 8, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 1, 'y': 4}], 'head': {'x': 1, 'y': 0}, 'length': 8, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 1, 'y': 8}, {'x': 1, 'y': 9}, {'x': 2, 'y': 9}, {'x': 3, 'y': 9}, {'x': 4, 'y': 9}, {'x': 5, 'y': 9}, {'x': 6, 'y': 9}, {'x': 7, 'y': 9}, {'x': 7, 'y': 8}, {'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}], 'head': {'x': 1, 'y': 8}, 'length': 13, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 8, 'y': 9}, {'x': 9, 'y': 9}, {'x': 9, 'y': 8}, {'x': 9, 'y': 7}, {'x': 9, 'y': 6}, {'x': 9, 'y': 5}, {'x': 8, 'y': 5}], 'head': {'x': 8, 'y': 9}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

  
        food = [{"x":0,"y":5}]
        Board.initialiseBoard(11, 11)
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        result = (bestReply.BRS(ninf,pinf,4,"Max",board,snakes,"initial",my_snake))

        
        # Assert
        self.assertEqual(0,result)

if __name__ == "__main__":
    unittest.main()
