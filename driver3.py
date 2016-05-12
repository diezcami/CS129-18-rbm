import cv2
import time
from bam import *
from process import *

num_rows = 135000
num_cols = 60

# gets the euclidean distance between two vectors a and b
def distance(a, b):
    dist = 0.0
    for pair in zip(a, b):
        dist+=((pair[0]-pair[1])*(pair[0]-pair[1]))
    return m.sqrt(dist)
    
if __name__ == '__main__':
    start_time = time.time()
    images = load_images_from_folder (INPUT_DIR)
    
    # True indicates if a random weight matrix will be initialized.
    b = bam(num_rows, num_cols)
    label_of_apple = [1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1]
    
    for image in images:
        bp = get_bipolar_vector(image)
        # wag muna stochastic as stochastic causes errors
		
        convert_to_image(bp, 'img 1')
		
        total_differences = 0
        total_distance = 0.0
        iter_count = 1
        max_iter_count = 10
        
        inputs_to_train = [bp]
        outputs_to_train = [label_of_apple]
        
        while True:
            print "now at iteration "+str(iter_count)
            b.train(inputs_to_train, outputs_to_train)
            
            if iter_count==max_iter_count:
                print "--- --- --- --- --- --- --- --- --- --- ---"
                print "Max number of iterations reached! Stopping."
                print "See max_iter_count in driver2.py to change."
                print "--- --- --- --- --- --- --- --- --- --- ---"
                break
            else:
                iter_count += 1
            print ""
        
        print "program execution: "+str(time.time()-start_time)