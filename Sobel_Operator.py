import numpy as np
import cv2
import math
class pythontasks:
    def sobel(self,image):
        image_x = np.zeros(image.shape)
        image_y = np.zeros(image.shape)
        image_result = np.zeros(image.shape)
        row,col=np.shape(image)
        for r in range(2,row-2):
            for c in range(2,col-2):
                image_x[r][c]=image[r-1][c-1]*-1 + image[r][c-1]*-2 + image[r+1][c-1]*-1 + \
                              image[r-1][c+1]*1 + image[r][c+1]*2 + image[r+1][c+1]*1
                image_y[r][c] = image[r - 1][c - 1] * -1 + image[r + 1][c - 1] *1 + image[r - 1][c] * -2 +\
                               image[r + 1][c] * 2 +  image[r - 1][c + 1] * -1  +  image[r + 1][c + 1]*1
                q= image_x[r][c] + image_y[r][c]
                if (q>100):
                    image_result[r][c] = 255
                else:
                    image_result[r][c] = 0
        return image_result

object=pythontasks()
img=cv2.imread('C:\\Users\\Mr_Tech\\Desktop\\temp_2.jpg',0)

cv2.imshow('before',img)
after=object.sobel(img)
cv2.imshow('after',after)
cv2.waitKey(0)
cv2.destroyAllWindows()