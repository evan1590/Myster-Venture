import nltk
from nltk.corpus import wordnet as WN

import string

from story_tree import *

DIRECTIONS = ['right', 'left', 'straight', 'back']

# preorder traversal to check the contents of
# the tree. TESTING ONLY
def check_tree(node):

	if node:
		print node.cargo

		for child in node.directions.keys():
			print "\nDIRECTION: "+child
			check_tree(node.directions[child])

# use wordnet and Synsets to figure out
# commands the user is typing
def main():

	with open("story.txt", 'r') as story_file:
		story = story_file.read()

	story = [s.strip() for s in story.splitlines()]

	game_tree = StoryTree()

	# populate tree here
	for step in story:
		game_tree.insert(step)

	# prints out the tree's content
	# FOR TESTING PURPOSES
	# check_tree(game_tree.root)


	atEnd = False

	intro = """ Will you survive? HINT: Probably not... """

	print intro 
	
	currentNode = game_tree.root

	while (not atEnd):

		if isinstance(currentNode, str):
			print currentNode
			atEnd = True

		else:
			print currentNode.cargo
			print

			command = raw_input("What will you do? : ")

			print

			# strip out all punctuation REALLY fast
			# translate() uses raw string operations in C 
			# using a lookup table 
			command = command.translate(string.maketrans("",""), string.punctuation)

			# keeps track of each word of the command and
			# all of their respective Synsets
			commandDict = {}

			# direction user will move
			directionToMove = ""

			# Creates a Thesaurus of words in the command string
			# ------- takes a long time -------
			for word in command.lower().split():

				# check if word in dictionary
				if not commandDict.has_key(word):

					# generate synsets for the next word in the command
					synsets = WN.synsets(word)
					
					# get the lemmas for the Synsets generated
					for lemma in synsets:

						# iterate through DIRECTIONS
						for direction in DIRECTIONS:

							# check if direction in DIRECTIONS matches a word in
							# the generated lemmas
							if direction in synsets[0].lemma_names:

								# if it does, then it's a direction and that's the direction
								# the user wants to go
								directionToMove = direction
								break

					# insert the synsets of the word if synsets exist
					# for that word
					if len(synsets) > 0:
						commandDict[word] = WN.synsets(word)


			# once we get Thesaurus, want to get 
			# directions from the synsets

			# move down the tree
			currentNode = game_tree.step_next(currentNode, directionToMove)

if __name__ == '__main__':
	main()