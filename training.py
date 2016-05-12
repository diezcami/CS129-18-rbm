import cv2
import os
import numpy as np
from bam import *

TRAINING_DIR = 'input/training_set/'

width = 450
height = 300
num_rows = 135000
num_cols = 60

# Input: Image
# Output: Bipolar Vector
def get_bipolar_vector (img):
    img = cv2.resize(img, (width, height))
    ret2, th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    bipolar_vector = []
    for row in range(th2.shape[0]):
        for col in range(th2.shape[1]):
            val = th2[row,col]
            if val == 0:
                bipolar_vector.append(-1)
            else:
                bipolar_vector.append(1)
				
	# cv2.imshow('bnw',th2)
    return bipolar_vector

# Input: Bipolar Vector
# Output: Image (Matrix)
def get_image (bipolar_vector):
    # Tae annoying nito forever amp - andre
    image_vector = np.zeros((height, width), np.float32)
    bv_index = 0 
    for row in range(image_vector.shape[0]):
        for col in range(image_vector.shape[1]):
            if bipolar_vector[bv_index] == 1:
                image_vector[row,col] = 255
            else:
                image_vector[row,col] = 0
            # print image_vector[row][col]
            bv_index += 1
    return image_vector 

# Input: Directory of Images
# Output: Array of images inside the directory
def load_images_from_folder (folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), 0)
        if img is not None:
            images.append(img)
    return images

def convert_to_image (bp, st, show_image=False):
	new_image = get_image(bp)
	if show_image:
		cv2.imshow(st, np.mat(new_image))

# Gets the Euclidean distance between a and b
def distance(a, b):
    dist = 0.0
    for pair in zip(a, b):
        dist+=((pair[0]-pair[1])*(pair[0]-pair[1]))
    return m.sqrt(dist)


# Input: A single image and BAM instance
# Output: Last label of the processed image
def get_last_label(image, b, max_iter_count = 10):
    print "Get_Last_Label: Beginning"
    bp = get_bipolar_vector(image)        
    total_differences = 0
    total_distance = 0.0
    iter_count = 1
    
    while True:
        bp_prime = b.feedForward(bp)
        bp_new = b.feedBackward(bp_prime)        
        count = 0 # Number of elements that changed
        for i in zip(bp, bp_new):
            if i[0] != i[1]:
                count += 1       
        # Numerically determine how different they are based on euclidean dist.
        d = distance(bp_new, bp)
        if distance(bp_new, bp) < 1:
            print "Get_Last_Label: Distance is less than 1 - done!"
            break
        elif iter_count==max_iter_count:
            print "Get_Last_Label: Maximum iterations reached!"
            break
        else:
            bp = bp_new
            iter_count += 1
        total_differences+=count
        total_distance += d
        
    return bp_prime

if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)

    i = 0
    for image in images:
        bp = get_bipolar_vector (image) # Converts image to bipolar vector
        new_image = get_image(bp) # Converts bipolar vector to an image array
        cv2.imshow(str(i), np.mat(new_image));
        i += 1

    cv2.waitKey(0)
    cv2.destroyAllWindows()