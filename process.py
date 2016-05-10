import cv2
import os
import numpy as np

INPUT_DIR = 'input/'

# Input: Image
# Output: Bipolar Vector
def get_bipolar_vector (img):
    img = cv2.resize(img, (450,300))
    ret2, th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    bipolar_vector = []
    for row in range(th2.shape[0]):
        for col in range(th2.shape[1]):
            val = th2[row,col]
            if val == 0:
                bipolar_vector.append(-1)
            else:
                bipolar_vector.append(1)
    return bipolar_vector

# Input: Bipolar Vector
# Output: Image (Matrix)
def get_image (bipolar_vector):
    image_vector = [[0 for i in range(300)] for j in range(450)]
    bv_index = 0 
    for row in range(len(image_vector)):
        for col in range(len(image_vector[0])):
            if bipolar_vector[bv_index] == 1:
                image_vector[row][col] = 255
            else:
                image_vector[row][col] = 1
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

if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)

    for image in images:
        bp = get_bipolar_vector (image)
        new_image = get_image (bp)
        cv2.imshow('black and white',np.array(new_image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

