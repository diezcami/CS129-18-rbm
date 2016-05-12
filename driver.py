import cv2
from bam import *
from process import *

num_rows = 135000
num_cols = 60
    
if __name__ == '__main__':
    start_time = time.time()
    images = load_images_from_folder (INPUT_DIR+"/for training/")
    print "loading images took " + str( time.time()-start_time) + " seconds."
    image_counter = 0

    # ---- training ----------------------------------------
    print "--- --- --- initiating training of vector --- --- ---"
    for image in images:
        start_time = time.time()
        print "starting with image no. "+str(image_counter)
        image_counter+=1
        
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
        
        print "training this image took: "+str(time.time()-start_time)+" seconds"
        
    # ---- part 1: supervised learning ---------------------
    images = load_images_from_folder(INPUT_DIR+"for dreaming/")
    image_counter = 0
    
    for image in images:
        print "now dreaming with image "+str(image_counter)
        image_counter+=1
        
        bp = get_bipoloar_vector(image)
        
        # we're gonna use the trained bam
        convert_to_image(bp, 'img 1')
        
        print_events = True
        max_iter_count = 20
        
        while True:
            if print_events:
                print "now at iteration " + str(iter_count)
            bp_prime = b.feedForward(bp)
            bp_new = b.feedBackward(bp_prime)
            
            # count how many elements changed
            count = 0
            for i in zip(bp, bp_new):
                if i[0] != i[1]:
                    count += 1
            if print_events:
                print str(count) + " out of " + str(len(bp)) + " features are different."
            
            # numerically determine how different they are based on euclidean dist.
            d = distance(bp_new, bp)
            if print_events:
                print "distance is "+str(d)
            if distance(bp_new, bp) < 1:
                if print_events:
                    print "stopped at iteration " + str(iter_count)
                break
            elif iter_count==max_iter_count:
                if print_events:
                    print "--- --- --- --- --- --- --- --- --- --- ---"
                    print "Max number of iterations reached! Stopping."
                    print "See max_iter_count in driver2.py to change."
                    print "--- --- --- --- --- --- --- --- --- --- ---"
                convert_to_image(bp, 'rbm ' + str(iter_count))
                break
            else:
                bp = bp_new
                iter_count += 1
            if print_events:
                print ""