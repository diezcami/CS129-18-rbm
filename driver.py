import cv2
from bam import *
from training import *

num_rows = 135000
num_cols = 60

TRAINING_DIR = 'input/training_set/'
DREAMING_DIR = 'input/dreaming_set/'

def train(training_set, b, max_iter_count = 10):
    image_count = 1
    for image in training_set:
        print "Training image no. "+str(image_count)
        image_count += 1
        
        bp = get_bipolar_vector(image)
        #image, b, max_iter_count = 10
        image_label = get_last_label (image, b)
        
        inputs_to_train = [bp]
        outputs_to_train = [image_label]
        iter_count = 0
        while iter_count <= max_iter_count:
            b.train(inputs_to_train, outputs_to_train)
            iter_count += 1

def dream(dreaming_set, b, print_events = False, max_iter_count = 20):
    image_count = 1
    for image in dreaming_set:
        print "Dreaming image no. "+str(image_count)
        image_count += 1  
        iter_count = 0

        bp = get_bipolar_vector(image)
        
        while True:
            if print_events:
                print "Dreaming iteration: " + str(iter_count)
            bp_prime = b.feedForward(bp)
            bp_new = b.feedBackward(bp_prime)
            
            count = 0 # Number of changed elements
            for i in zip(bp, bp_new):
                if i[0] != i[1]:
                    count += 1
            if print_events:
                print str(count) + " out of " + str(len(bp)) + " features are different."
            
            # Numerically determine how different they are based on euclidean dist.
            d = distance(bp_new, bp)
            if print_events:
                print "Distance is "+str(d)
            if distance(bp_new, bp) < 1:
                if print_events:
                    print "Dreaming: Distance is less than 1 - done!"
                #convert_to_image(bp, 'Dream Result: ' + str(iter_count))
                break
            elif iter_count==max_iter_count:
                if print_events:
                    print "Dreaming: Maximum iterations reached!"
                #convert_to_image(bp, 'Dream Result: ' + str(image_count))
                break
            else:
                bp = bp_new
                iter_count += 1
        print "Displaying image:"
        convert_to_image(bp, 'Dream Result: ' + str(image_count), True)

if __name__ == '__main__':
    print "Which would you like to perform? (Input 1 or 2)"
    print "[1] Supervised Daydreaming (Part 1)"
    print "[2] Unsupervised Daydreaming (Part 2)"
    input = raw_input()

    if input == 1: # Supervised
        training_set = load_images_from_folder (TRAINING_DIR)
        dreaming_set = load_images_from_folder (DREAMING_DIR)
        b = bam(num_rows, num_cols)

        print "<-- PART 1/2: TRAINING -->"
        train (training_set, b)
        print "<-- PART 2/2: DREAMING -->"
        dream (dreaming_set, b, True, 5)

    else: # input == 2, Unsupervised
        print "Pls put code here"
    cv2.waitKey(0)
    cv2.destroyAllWindows()