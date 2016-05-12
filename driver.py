import cv2
from bam import *
from process import *

num_rows = 135000
num_cols = 60
    
if __name__ == '__main__':
    start_time = time.time()
    images = load_images_from_folder (INPUT_DIR)
    image_counter = 0

    # ---- training ----------------------------------------
    for image in images:
        print "starting with image no. "+str(image_counter)
        bp = get_bipolar_vector(image)
        
        # True indicates if a random weight matrix will be initialized.
        b = bam(num_rows, num_cols)
        label_of_apple = get_last_label (True, 25) # Uncomment for more general usage
        
        print "Finished retrieving last label"
		
        convert_to_image(bp, 'img 1')
		
        total_differences = 0
        total_distance = 0.0
        iter_count = 1
        max_iter_count = 10
        
        inputs_to_train = [bp]
        outputs_to_train = [label_of_apple]
        
        while iter_count <= max_iter_count:
            print "now at iteration "+str(iter_count)+" of training"
            b.train(inputs_to_train, outputs_to_train)
            iter_count += 1
        
        print "--- --- --- --- --- --- --- --- --- --- ---"
        print "Max number of iterations reached! Stopping."
        print "Check line 28 of driver.py to change."
        print "--- --- --- --- --- --- --- --- --- --- ---"
        
        print "program execution: "+str(time.time()-start_time)
        
    # ---- part 1: supervised learning ---------------------