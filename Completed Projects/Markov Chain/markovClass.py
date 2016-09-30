# 2 stage markov chain class
# Created by Mykhaylo Kuzma - V0.001
import random

class MarkovChain:
	"""
	Fields:	a - str
			b - str
			probAgA - float <1
			probAgB - float <1
			probAindep - float <1
			probBindep - float <1
			length - Natural number

	"""
	def __init__(self, a, b, probAgA, probAgB, probAindep, probBindep,\ 
		length):
		self.a = a
		self.b = b
		self.probAgA = probAgA
		self.probBgA = 1 - probAgA
		self.probAgB = probAgBd
		self.probBgB = 1 - probBgB
		self.probAindep = probAindep
		self.probBindep = probBindep
		self.length = length

	def __repr__(self):
		return "Intakes a string called a, string called b,\
		 prob of a given a, prob of b given a, prob of a given b, \
		 prob of b given b and a number called length,\
		 in order to produce a string of length that follows a Markov\
		 chain. A and B should be single letters, to make a letter\
		  chain."

	# randomProb consumes a float called inputProb, a string InA, 
	# and a string InB
	# to return a selected element from a generated list where inputProb
	# * 100 elements are a, and the rest are b. Weight is assigned by
	# changing the inputted float.
	# The selected element will be random and the process reflects
	# the random selection of A or B given weights.]
	# randomProb: Float Str Str -> Str
	def randomProb(inputProb, InA, InB):
		# probA is probability of event A occuring
		probA = int((inputProb * 100) // 1)
		# probB is the probability of event B occuring (inverse of A)
		probB = 100 - probA

		# Create a list of string InA for probA times
		# 	and a list of string InB for probB times
		# 	These two lists are going to be combined then a random
		# 	part of the combined list will be selected.
		# 	By making two lists and combining, the results
		# 	should reflect a random selection of A and B.
		testList1 = [InA for i in range(0, probA)]
		testList2 = [InB for i in range(0, probB)]

		testList = testList1.append(testList2)

		choice = random.uniform(0, 99)
		return testList[choice]

	# produceChain consumes a markov chain class and returns a string
	# 	that consists of a and b as determined by a markov chain.
	# produceChain: Markov -> Str
	def produceChain(self):
		outStr = ""
		
		for i in range(1,length):
			# if you are beginning the chain, probs are independent
			if len(outStr) == 0:
				outStr.append(randomProb(self.probAindep, self.a, \
					self.b))
			# otherwise, check conditions of previous output
			else:
				initState = outStr[i-1]
				if initState == self.a:
					outStr.append(self.randomProb(self.ProbAgA, \
						self.a, self.b))
				else:
					outStr.append(self.randomProb(self.ProbAgB, \
						self.a, self.b))

		return outStr

	# Print the produced markov chain to the screen
	def printChain(self):
		print(self.produceChain())

test = MarkovChain("a", "b", 0.7, 0.4, 0.5, 0.5, 10)
test.printChain()

