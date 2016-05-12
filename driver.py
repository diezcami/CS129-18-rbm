import cv2
from bam import *
from process import *

num_rows = 135000
num_cols = 60
    
if __name__ == '__main__':
    start_time = time.time()
    images = load_images_from_folder (INPUT_DIR)
    
    # True indicates if a random weight matrix will be initialized.
    b = bam(num_rows, num_cols)
    label_of_apple = get_last_label (True, 25) # Uncomment for more general usage
    print "Finished retrieving last label"

    filecount = 0
    for image in images:
        bp = get_bipolar_vector(image)
		
        convert_to_image(bp, 'img '+count)
		
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
                print "Check line 14 of driver.py to change."
                print "--- --- --- --- --- --- --- --- --- --- ---"
                break
            else:
                iter_count += 1
            print ""
        
        print "program execution: "+str(time.time()-start_time)