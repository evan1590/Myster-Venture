# story story 

class Node(object):
	"""Creates a Node with item(cargo) and a link (left, right, straight = next) and
	   another link (back = parent)

	Attributes:
	    item: Value
	"""
	def __init__(self, item, right=None, left=None, straight=None, back=None):
		self.cargo = item
		self.right = right
		self.left = left
		self.straight = straight
		self.back = back

class StoryTree(object):
	"""docstring for StoryTree"""
	def __init__(self, root):
		self.root = root
		

