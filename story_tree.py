# story story 

class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.cargo = item
		self.directions = {
			# 'right': right,
			# 'left': left,
			# 'straight': straight,
			# 'back': back
		}

class StoryTree(object):
	"""docstring for StoryTree"""
	def __init__(self):
		self.root = None
	
	def insert(self, string):
		if not root:
			self.root = Node(string)
		else:
			current = self.root

			# parse out direction from beginning of paragraph
			colon = string.find(':')
			direction = string[:colon].lower()
			story = string[colon+1:]

			while current:
				if is_empty(current.directions):
					current.directions[direction] = Node(story)
					return
				else:
					next_direction = current.directions.keys()[0]
					current = current.directions[next_direction]

	def step_next(self, direction):
		pass
