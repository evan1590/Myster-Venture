# story story 

class Node(object):
	"""docstring for Node"""
	def __init__(self, item, right=None, left=None, straight=None, back=None):
		self.cargo = item
		self.directions = {
			'right': right,
			'left': left,
			'straight': straight,
			'back': back
		}

class StoryTree(object):
	"""docstring for StoryTree"""
	def __init__(self, root):
		self.root = root
	
	def insert(self, string):
		
