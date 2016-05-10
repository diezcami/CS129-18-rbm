import random as rand
import numpy as np
import math as m

class bam:
	def __init__(self, n, p, random=False):
		self.energy = self.mean = 0.0
		self.stdev = 0.1
		
		self.rowCount = n
		self.colCount = p
		self.weightMatrix = self.makeNewWeightMatrix(random)
		
	def feedForward(self, input, stochastic=True):
		result = ( np.mat(input) * np.mat(self.weightMatrix) ).tolist()[0]
		if stochastic:
			result = map(lambda x: 1 if self.logistic(x) > self.randomGaussian() else -1, result)
		else:
			result = map(lambda x: 1 if x>0 else -1, result)
		return result
	
	def feedBackward(self, output, stochastic=True):
		result = ( np.mat(output) * np.mat(zip(*self.weightMatrix)) ).tolist()[0]
		if stochastic:
			result = map(lambda x: 1 if self.logistic(x) > self.randomGaussian() else -1, result)
		else:
			result = map(lambda x: 1 if x>0 else -1, result)
		return result
		
	# note: the source code of sir happy originally said
	#   weightMatrix[r][c]input.at(r) * input.at(c)
	#   it was clarified na dapat output yung isa
	def computeEnergy(self, input, output):
		e = 0.0
		for r in range(len(input)):
			for c in range(len(output)):
				e += self.weightMatrix[r][c] * input[r] * output[c]
		self.energy = -1 * e
	
	def train(self, input, output):
		newWeightMatrix = np.mat(self.weightMatrix)
		for pair in zip(input, output):
			m2 = np.mat(zip(pair[0])) * np.mat(pair[1])
			newWeightMatrix += m2
		self.weightMatrix = newWeightMatrix.tolist()
		
	def logistic(self, x):
		return float("inf") if x==0 else 1.0/(1.0-(m.exp(-x)))

	def randomGaussian(self):
		return np.random.normal(self.mean, self.stdev)
	
	def makeNewWeightMatrix(self, random=False):
		if not random:
			return [ [0.0]*self.colCount for i in range(self.rowCount) ]
		else:
			return [ [rand.randrange(-1, 1) for i in range(self.colCount)] for j in range(self.rowCount)]
	
	def printWeightMatrix(self):
		print np.mat(self.weightMatrix)
		
	def getEnergy(self):
		return self.energy