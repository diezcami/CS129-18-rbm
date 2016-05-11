<<<<<<< HEAD
from bam import bam
=======
from bam import *
>>>>>>> c5203d1b542efcd72e2c006884b4873c6f41e330

#---"static" variables-------------
num_rows = 4
num_cols = 3

#---main---------------------------
<<<<<<< HEAD
b = bam(numRows, numCols)
print "Row: "+str(b.rowCount)+" Col: "+str(b.colCount)
=======
b = Bam(num_rows, num_cols)
print "Row: "+str(b.row_count)+" Col: "+str(b.col_count)
>>>>>>> c5203d1b542efcd72e2c006884b4873c6f41e330
input = []
output = []

# prepare inputs
input.append( [1, -1, 1, 1] )
input.append( [1, -1, -1, 1] )
input.append( [1, 1, -1, 1] )

# prepare outputs
output.append( [1, -1, -1] )
output.append( [1, 1, -1] )
output.append( [1, -1, 1] )

# training
b.train(input, output)
print "weight matrix:"
b.print_weight_matrix()

# testing
test_data = [1, -1, -1, -1]
epoch = 10

for i in range(epoch):
	print "Epoch "+str(i)
	print "x: "+str(test_data)
	
	test_data_prime = b.feed_forward(test_data)
	print "y: "+str(test_data_prime)
	
	test_data_new = b.feed_backward(test_data_prime)
	print "x': "+str(test_data_new)
	
	print "=================="
	b.compute_energy(test_data_new, test_data_prime)
	print "Energy: "+str(b.get_energy())
	print "=================="
	
	test_data = test_data_new