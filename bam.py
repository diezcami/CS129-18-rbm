from collections import defaultdict
import random as rand
import numpy as np
import math as m

class Bam:
	def __init__(self, n, p, random=False):
		self.energy = self.mean = 0.0
		self.stdev = 0.1
		
		self.row_count = n
		self.col_count = p
		self.weight_matrix = self.make_new_weight_matrix(random)
		
	def feed_forward(self, input, stochastic=True):
		result = ( np.mat(input) * np.mat(self.weight_matrix) ).tolist()[0]
		if stochastic:
			result = map(lambda x: 1 if self.logistic(x) > self.random_gaussian() else -1, result)
		else:
			result = map(lambda x: 1 if x>0 else -1, result)
		return result
	
	def feed_backward(self, output, stochastic=True):
		result = ( np.mat(output) * np.mat(zip(*self.weight_matrix)) ).tolist()[0]
		if stochastic:
			result = map(lambda x: 1 if self.logistic(x) > self.random_gaussian() else -1, result)
		else:
			result = map(lambda x: 1 if x>0 else -1, result)
		return result
		
	# note: the source code of sir happy originally said
	#   weight_matrix[r][c]input.at(r) * input.at(c)
	#   it was clarified na dapat output yung isa
	def compute_energy(self, input, output):
		e = 0.0
		for r in range(len(input)):
			for c in range(len(output)):
				e += self.weight_matrix[r][c] * input[r] * output[c]
		self.energy = -1 * e
	
	def train(self, input, output):
		new_weight_matrix = np.mat(self.weight_matrix)
		for pair in zip(input, output):
			m2 = np.mat(zip(pair[0])) * np.mat(pair[1])
			new_weight_matrix += m2
		self.weight_matrix = new_weight_matrix.tolist()
		
	def logistic(self, x):
		return float("inf") if x==0 else 1.0/(1.0-(m.exp(-x)))

	def random_gaussian(self):
		return np.random.normal(self.mean, self.stdev)
	
	def make_new_weight_matrix(self, random=False):
		if not random:
			return [ [0.0]*self.col_count for i in range(self.row_count) ]
		else:
			return [ [rand.randrange(-1, 1) for i in range(self.col_count)] for j in range(self.row_count)]
	
	def print_weight_matrix(self):
		print np.mat(self.weight_matrix)
		
	def get_energy(self):
		return self.energy