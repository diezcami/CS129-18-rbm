import cv2

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

# Input: Directory of Images
# Output: Array of images inside the directory
def load_images_from_folder (folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)

    for image in images:
        bp = get_bipolar_vector (image)