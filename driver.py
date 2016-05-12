import cv2
from bam import *
from process import *

num_rows = 135000
num_cols = 60

# Part 1
def supervised_daydreaming (image, b):
    print "Hello"

# Part 2
def unsupervised_daydreaming (image, b):
    bp = get_bipolar_vector(image)
    # wag muna stochastic as stochastic causes errors
        
    epoch = 10
        
    for i in range(epoch):
        # bp is the testData
        bp_prime = b.feed_forward(bp, False)
        bp_new = b.feed_backward(bp_prime, False)
        
        print "=================="
        b.compute_energy(bp_new, bp_prime)
        print "Energy: "+str(b.get_energy())
        print "=================="
        bp = bp_new


if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)
    b = Bam(num_rows, num_cols, True)
    
    for image in images:
        # Comment out whichever won't be used
        # supervised_daydreaming(image)
        unsupervised_daydreaming(image, b)