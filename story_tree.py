# story story 

class Node(object):
	"""docstring for Node"""
	def __init__(self, item):
		self.cargo = item # story string

		# want this to be empty at first and then add things
		# dynamically. If a direction doesn't exist in this 
		# dictionary we can check for that and prevent the 
		# user from going that way or kill them
		self.directions = {}

class StoryTree(object):
	"""docstring for StoryTree"""
	def __init__(self):
		self.root = None # set root as nothing to begin with
	
	def insert(self, string):
		if not self.root: # if no root...
			self.root = Node(string) # set first string in story file to be root
		else:
			current = self.root

			# parse out direction from beginning of paragraph
			colon = string.find(':') # gets position of colon
			direction = string[:colon] # get direction that bit of the story happens in
			story = string[colon+1:] # get the actual story

			while current: # loop while still on a node
				if len(current.directions) == 0: # check if dictionary of directions is empty

					# if it is, add the direction and the appropriate story
					# branching from it to the tree and end insertion
					current.directions[direction] = Node(story)
					return
				else:

					# traverse the tree
					# NOTE: currently pulling the first direction because it's assumed
					# there are no other directions in the dictionary for now
					next_direction = current.directions.keys()[0]

					# set new current to be the next story bit
					current = current.directions[next_direction]

	def step_next(self,node,direction):
		if node.directions.has_key(direction.upper()):
			return node.directions[direction.upper()]
		else:
			return "YOU HAVE DIED A HORRIBLE DEATH, AND NO ONE WILL REMEMBER YOU!"
		
			
