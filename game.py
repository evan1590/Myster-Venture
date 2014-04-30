import nltk
from nltk.corpus import wordnet as WN

import string
import os

from story_tree import *

DIRECTION_KEY = ['right', 'left', 'straight', 'back']

CAMPUS = {
			'A': ["", [0, 'C', 'B', 0]],         # Young
			'B': ["", [0,'D','E', 0]],     # Clark
			'C': ["", ['D', 0,'N','A']], # Meadows
			'D': ["", ['B','C','E', 0]],     # Chase
			'E': ["", [0, 0, 'G', 'D']],         # Meneely/Watson Courtyard
			#'F': ("", ['M','G']),         # Mary Lyon
			'G': ["", [0,'I','J', 'E']],     # Dimple
			#'H': ("", ['G']),             # Emerson Dining
			'I': ["", [0, 0, 0, 0]],             # Chapel
			'J': ["", [0, 0, 'K','G']],     # Library
			'K': ["", [0, 0, 0, 'J']],         # New SC
			#'L': ("", ['K','J']),         # Old SC
			#'M': ("", ['F','G']),         # Park Hall
			'N': ["", ['J','k', 0, 0]],     # Power Plant
			'O': ["", []]                 # WHALE
		 }

DIRECTIONS = {'right':['right'],
			  'left':['left'], 
			  'straight':['straight', 'forward'], 
			  'back':['back', 'backwards']
			  }

# preorder traversal to check the contents of
# the tree. TESTING ONLY
def check_tree(node):

	if node:
		print node.cargo

		for child in node.directions.keys():
			print "\nDIRECTION: "+child
			check_tree(node.directions[child])

def populate_graph():
	# loop through each line and insert into
	# graph where appropriate
	os.chdir('stories/')
	directoryContents = os.listdir('./') # get titles of the text files
	print directoryContents

	for f in directoryContents:
		print f
		with open(f, 'r') as story_file:
			story = story_file.read()

			# parse out direction from beginning of paragraph
			colon = story.find(':') # gets position of colon
			node = story[:colon] # get direction that bit of the story happens in
			story = story[colon+1:] # get the actual story

			CAMPUS[node][0] = story

# generates all of the synonyms for the 4 directions
# in our DIRECTIONS dictionary
def generate_direction_thesaurus():

	# for each directions
	for direction in DIRECTIONS.keys():

		# get synset of the directions
		syns = WN.synsets(direction)

		# for all of the synsets of that direction
		for syn in syns:

			# append the results to the previous array value in the dictionary
			DIRECTIONS[direction] = DIRECTIONS[direction] + syn.lemma_names

		# get rid of duplicates
		DIRECTIONS[direction] = list(set(DIRECTIONS[direction]))

# use wordnet and Synsets to figure out
# commands the user is typing
def main():

	# with open("story.txt", 'r') as story_file:
	# 	story = story_file.read()

	# story = [s.strip() for s in story.splitlines()]

	# game_tree = StoryTree()

	# # populate tree here
	# for step in story:
	# 	game_tree.insert(step)

	populate_graph()
	i = 0
	for node in CAMPUS.keys():
		print "NODE: "+str(i)
		print CAMPUS[node][0]
		print
		i += 1
	# prints out the tree's content
	# FOR TESTING PURPOSES
	# check_tree(game_tree.root)

	generate_direction_thesaurus()

	atEnd = False

	intro = """ Will you survive? HINT: Probably not... """

	print intro 
	
	currentNode = 'A'

	while (not atEnd):

		print currentNode

		print CAMPUS[currentNode][0]
		print

		if CAMPUS[currentNode] == []:
			atEnd = True
		else:

			# if isinstance(currentNode, str):
			# 	print currentNode
			# 	atEnd = True

			# else:
			# 	print currentNode.cargo
			# 	print

			command = raw_input("What will you do? : ")

			print

			# strip out all punctuation REALLY fast
			# translate() uses raw string operations in C 
			# using a lookup table 
			command = command.translate(string.maketrans("",""), string.punctuation)

			# keeps track of each word of the command and
			# all of their respective Synsets
			# commandDict = {}

			# direction user will move
			directionToMove = ""

			# Creates a Thesaurus of words in the command string
			# ------- takes a long time -------
			for word in command.lower().split():
				hasDirection = False

				for direct in DIRECTIONS.keys():
					if word in DIRECTIONS[direct]:
						directionToMove = direct
						hasDirection = True

				if hasDirection:
					break

			# traverse the graph
			for direct in range(len(DIRECTION_KEY)):
				if directionToMove == DIRECTION_KEY[direct]:
					currentNode = CAMPUS[currentNode][1][direct]


if __name__ == '__main__':
	main()