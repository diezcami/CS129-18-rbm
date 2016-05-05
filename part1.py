import cv2

img = cv2.imread('sample.jpg', 0)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print th2.shape
bipolar_vector = []
for row in range(th2.shape[0]):
    for col in range(th2.shape[1]):
        val = th2[row,col]
        if val == 0:
            bipolar_vector.append(-1)
        else:
            bipolar_vector.append(1)

# 2) Loop through each pixel value and store it in an array
# Store 0 as -1, 255 as 1
values = []
for row in range (len(matrix)):
    for col in range(len(matrix[0])):
        if bipolar_vector[row][col] == 255:
            values.append(1)
        else:
            values.append(-1)

