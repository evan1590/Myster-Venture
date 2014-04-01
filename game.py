import nltk
from nltk.corpus import wordnet as WN

import string

# use wordnet and Synsets to figure out
# commands the user is typing
def main():

	atEnd = False

	intro = """ Will you survive? HINT: Probably not... """

	while (not atEnd):
		command = raw_input("What will you do? : ")

		# strip out all punctuation REALLY fast
		# translate() uses raw string operations in C 
		# using a lookup table 
		command = command.translate(string.maketrans("",""), string.punctuation)

		commandDict = {}

		# Creates a Thesaurus of words in the command string
		# takes a long time
		for word in command.lower().split():
			if not commandDict.has_key(word):
				synsets = WN.synsets(word)

				if len(synsets) > 0:
					commandDict[word] = WN.synsets(word)

		# once we get Thesaurus, want to get 
		# directions from the synsets

if __name__ == '__main__':
	main()