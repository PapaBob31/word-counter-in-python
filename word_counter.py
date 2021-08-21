# words counter: a python script that counts all the words in a sentence
run = True


class word_counter:
	def __init__(self):
		"""class variables"""

		# contains all the characters that usually seperate words in a sentence 
		self.ignore = [" ", ","]
		self.input = ""
		self.count = []
		self.counter = []

	def input_sentence(self):
		self.input = input("enter a sentence and I'll count the number of words in it\nType 'Q' or 'q' to exit\n")
		self.input = self.input.strip()

	def word_count(self):
		# loops through all the letters in a sentence
		for word in self.input:
			if word not in self.ignore:
				self.count.append(word)

			# if letter is in self.ignore and self.count is not an empty list, self.count will be added to self.counter
			# and the letter will be skipped
			if word in self.ignore:
				if self.count:
					self.counter.append(self.count)
					self.count = []

		# after exiting the for loop
		# and self.count is not empty, add self.count to self.counter
		if self.count != []:
			self.counter.append(self.count)
			self.count = []

	def no_of_words(self):
		no = len(self.counter)
		if no <= 1:
			word = " word!"
		if no >  1:
			word = " words!"
		no = str(no)
		print("The sentence above contains " + no + word)
		self.count = []
		self.counter = []


counter = word_counter()

while run:
	counter.input_sentence()
	if counter.input == "q" or counter.input == "Q":
		break
	counter.word_count()
	counter.no_of_words()

# the end
