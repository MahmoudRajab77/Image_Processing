import numpy
import cv2
import math


class pythonTasks28:

        def minn(self, image):
            row, col = numpy.shape(image)
            image2 = numpy.array(image)
            for r in range(2, row - 2):
                for c in range(2, col - 2):
                    list1 = [ image[r - 1][c - 1] , image[r][c - 1] ,image[r + 1][c - 1] , \
                                  image[r - 1][c], image[r][c] , image[r + 1][c] ,  \
                                  image[r - 1][c + 1], image[r][c + 1] , image[r + 1][c + 1] ]
                list1.sort()
                image2[r][c] = list1[0]
            return image2

object=pythonTasks28()
img=cv2.imread('images1.jfif',0)
cv2.imshow('before',img)
after=object.minn(img)
cv2.imshow('after',after)
cv2.waitKey(0)