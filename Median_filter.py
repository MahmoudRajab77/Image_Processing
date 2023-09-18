import numpy
import cv2
import math


class pythonTasks28:


      def medainn(self, image):
            row, col = numpy.shape(image)
            image2 = numpy.array(image)
            for r in range(2, row - 2):
                for c in range(2, col - 2):
                    list10 = [image[r - 1][c - 1] , image[r][c - 1] ,image[r + 1][c - 1] , \
                                  image[r - 1][c], image[r][c] , image[r + 1][c] ,  \
                                  image[r - 1][c + 1], image[r][c + 1] , image[r + 1][c + 1] ]
                    list10.sort()
                    image2[r][c] = list10[4]

            return image2

object=pythonTasks28()
img=cv2.imread('images1.jfif',0)
cv2.imshow('before',img)
after=object.medainn(img)
cv2.imshow('after',after)
cv2.waitKey(0)