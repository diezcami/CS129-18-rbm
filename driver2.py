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
    b = Bam(num_rows, num_cols, True)
    
    for image in images:
        bp = get_bipolar_vector(image)
        # wag muna stochastic as stochastic causes errors
		
        convert_to_image(bp, 'img 1')
		
        total_differences = 0
        total_distance = 0.0
        iter_count = 1
        max_iter_count = 10
        
        while True:
            print "now at iteration "+str(iter_count)
            bp_prime = b.feed_forward(bp)
            bp_new = b.feed_backward(bp_prime)
            
            # count how many elements changed
            count = 0
            for i in zip(bp, bp_new):
                if i[0] != i[1]:
                    count += 1
            print str(count) + " out of " + str(len(bp)) + " features are different."
            
            # numerically determine how different they are based on euclidean dist.
            d = distance(bp_new, bp)
            print "distance is "+str(d)
            if distance(bp_new, bp) < 1:
                print "stopped at iteration "+str(iter_count)
                break
            elif iter_count==max_iter_count:
                print "--- --- --- --- --- --- --- --- --- --- ---"
                print "Max number of iterations reached! Stopping."
                print "See max_iter_count in driver2.py to change."
                print "--- --- --- --- --- --- --- --- --- --- ---"
                break
            else:
                bp = bp_new
                iter_count += 1
            print ""
            total_differences+=count
            total_distance += d
			
            convert_to_image(bp, 'rbm ' + str(iter_count))
        
        mean_difference = float(total_differences)/float(iter_count)
        mean_distance = float(total_distance)/float(iter_count)
        print "average difference: "+str(mean_difference)
        print "average distance: "+str(mean_distance)
        print "program execution: "+str(time.time()-start_time)
		
        cv2.waitKey(0)
        cv2.destroyAllWindows()