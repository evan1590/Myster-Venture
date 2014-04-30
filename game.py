import nltk
from nltk.corpus import wordnet as WN

import random
import string
import os

from story_tree import *

INVENTORY = {
				'weapons': []
			}

DIRECTION_KEY = ['right', 'left', 'straight', 'back', 'explore']

CAMPUS = {
			'A': ["", [0, {'C': 'meadows'}, {'B': 'clark'}, 0, 0]],         # Young
			'B': ["", [0, {'D': 'chase'}, {'E': 'meneely'}, 0, 0]],     # Clark
			'C': ["", [{'D': 'chase'}, 0, {'N': 'power plant'}, {'A': 'young'}, 0]], # Meadows
			'D': ["", [{'B': 'clark'}, {'C': 'meadows'}, {'E': 'meneely'}, 0, 1], 
			     [
			        "Rancid Food", 
			        "Thursday's chicken turned into Saturday's chicken salad", 
			        "Mark's pots and pans", 
			        "Maria", 
			        "Cooking utensils"
			     ]
			     ],     # Chase
			'E': ["", [0, 0, {'G': 'dimple'}, {'D': 'chase'}, 0]],         # Meneely/Watson Courtyard
			#'F': ("", ['M','G']),         # Mary Lyon
			'G': ["", [0, {'I': 'chapel'}, {'J': 'library'}, {'E': 'meneely'}, 0]],     # Dimple
			#'H': ("", ['G']),             # Emerson Dining
			'I': ["", [0, 0, 0, 0, 0]],             # Chapel
			'J': ["", [0, 0, {'K': 'library'}, {'G': 'dimple'}, 0]],     # Library
			'K': ["", [{'O': 'whale'}, 0, 0, {'J': 'library'}, 0]],         # New SC
			#'L': ("", ['K','J']),         # Old SC
			#'M': ("", ['F','G']),         # Park Hall
			'N': ["", [{'J': 'library'}, {'K': 'new sc'}, 0, 0, 1], 
				 [
				 	"Chainsaw",
				 	"Screwdriver",
				 	"Keys",
				 	"Empty toolbox",
				 	"Gas",
				 	"Trashbags"
				 ]
				 ],     # Power Plant
			'O': ["", []]                 # WHALE
		 }

DIRECTIONS = {
			  'right': ['right'],
			  'left': ['left'], 
			  'straight': ['straight', 'forward'], 
			  'back': ['back', 'backwards'],
			  'explore': ['explore', 'look around']
			  }

# print graph node by node
# TESTING ONLY
def print_graph():
	i = 0
	for node in CAMPUS.keys():
		print "NODE: "+str(i)
		print CAMPUS[node][0]
		print
		i += 1

def populate_graph():

	# loop through each line and insert into
	# graph where appropriate
	os.chdir('stories/')
	directoryContents = os.listdir('./') # get titles of the text files

	for f in directoryContents:
		
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

	populate_graph()

	generate_direction_thesaurus()

	atEnd = False

	intro = """ Will you survive? HINT: Probably not... """

	print intro 
	
	currentNode = 'A'

	while (not atEnd):

		print CAMPUS[currentNode][0]
		print

		if CAMPUS[currentNode][1] == []:
			atEnd = True

		else:
			validDirection = False

			while (not validDirection):
				command = raw_input("What will you do? : ")

				print

				# strip out all punctuation REALLY fast
				# translate() uses raw string operations in C 
				# using a lookup table 
				command = command.translate(string.maketrans("",""), string.punctuation)

				# direction user will move
				directionToMove = ""
			
				for word in command.lower().split():
					hasDirection = False

					for direct in DIRECTIONS.keys():
						if word in DIRECTIONS[direct]:
							directionToMove = direct
							hasDirection = True
							validDirection = True

					if hasDirection:
						break

				if not validDirection:
					print "Please enter a valid direction to move in (either LEFT, RIGHT, STRAIGHT, or BACK)"

			# traverse the graph
			for direct in range(len(DIRECTION_KEY)):
				if directionToMove == DIRECTION_KEY[direct]:

					# if type in 'explore' and can explore
					if directionToMove == 'explore' and CAMPUS[currentNode][1][direct] == 1:
						
						# randomly choose a weapon or object
						objects = CAMPUS[currentNode][2]
						weapon = random.choice(objects)
						INVENTORY['weapons'].append(weapon)

						print "You just found a " + weapon

					else:
						currentNode = CAMPUS[currentNode][1][direct]

			if currentNode == 0 or (currentNode == 'E' or currentNode == 'I'):
				if currentNode != 0:
					print CAMPUS[currentNode][0]
				print "YOU HAVE DIED"
				atEnd = True
			else:
				# get the node to go to next
				currentNode = currentNode.keys()[0]

if __name__ == '__main__':
	main()