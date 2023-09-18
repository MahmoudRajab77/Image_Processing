import numpy
import cv2
import math
class pythontasks:

    def laplace(self,image,C):


        row,col=numpy.shape(image)
        image2=numpy.array(image)
        image3 = numpy.array(image)
        for r in range(2,row-2):
            for c in range(2,col-2):
                image2[r][c]=C*(image[r+1][c]+image[r-1][c] +image[r][c-1] + image[r][c + 1] + image[r][c]*-4)
                image3[r][c] =image[r][c]+image2[r][c]

        return image3

object=pythontasks()
img=cv2.imread('im.png',0)

cv2.imshow('before',img)
after=object.laplace(img,1)
cv2.imshow('after',after)
cv2.waitKey(0)
cv2.destroyAllWindows()