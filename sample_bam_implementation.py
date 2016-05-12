from bam import bam

#---"static" variables-------------
numRows = 4
numCols = 3

#---main---------------------------
b = bam(numRows, numCols)
print "Row: "+str(b.rowCount)+" Col: "+str(b.colCount)
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
b.printWeightMatrix()

# testing
testData = [1, -1, -1, -1]
epoch = 10

for i in range(epoch):
	print "Epoch "+str(i)
	print "x: "+str(testData)
	
	testDataPrime = b.feedForward(testData)
	print "y: "+str(testDataPrime)
	
	testDataNew = b.feedBackward(testDataPrime)
	print "x': "+str(testDataNew)
	
	print "=================="
	b.computeEnergy(testDataNew, testDataPrime)
	print "Energy: "+str(b.getEnergy())
	print "=================="
	
	testData = testDataNew