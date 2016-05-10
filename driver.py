import cv2
from bam import *
from process import *

numRows = 135000
numCols = 60

if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)
    b = bam(numRows, numCols, True)
    
    for image in images:
        bp = get_bipolar_vector(image)
        # wag muna stochastic as stochastic causes errors
        
        epoch = 10
        
        for i in range(epoch):
            # bp is the testData
            bp_prime = b.feedForward(bp, False)
            bp_new = b.feedBackward(bp_prime, False)
            
            print "=================="
            b.computeEnergy(bp_new, bp_prime)
            print "Energy: "+str(b.getEnergy())
            print "=================="
            bp = bp_new