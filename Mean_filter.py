import numpy
import cv2
import math
class pythontasks:
    def mean(self,image):

        row,col=numpy.shape(image)
        image2 = numpy.array(image)
        for r in range(2,row-2):
            for c in range(2,col-2):
                image2[r][c]=(image[r-1][c-1]*1/9 + image[r][c-1]*1/9 + image[r+1][c-1]*1/9 + image[r-1][c]*1/9 + image[r][c]*1/9 + image[r+1][c]*1/9 + image[r-1][c+1]*1/9 + image[r][c+1]*1/9 + image[r+1][c+1]*1/9)
        return image2

object=pythontasks()
img=cv2.imread('images.jfif',0)

cv2.imshow('before',img)
after=object.mean(img)
cv2.imshow('after',after)
cv2.waitKey(0)
cv2.destroyAllWindows()