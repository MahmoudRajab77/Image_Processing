import numpy
import cv2
import math
class pythontasks:
    def im2double(self, image):
        max_val = numpy.max(image)
        min_val = numpy.min(image)
        result = (image.astype('float') - min_val) / (max_val - min_val)
        return result

    def gaussian(self,image,a):
        image = self.im2double(image)
        image = numpy.array(image)
        row,col=numpy.shape(image)
        image2 = numpy.array(image)
        for r in range(2, row - 2):
           for c in range(2, col - 2):
                image2[r][c] = ( (1/(2*3.14*a*a))*pow(2.7,(-(pow((0),2) +pow((0),2))/(2*a*a)))*image[r-1][c-1] + \
                              image[r][c-1]*(1/(2*3.14*a*a))*pow(2.7,(-(pow((0),2) +pow((1),2))/(2*a*a))) + \
                              image[r+1][c-1]*(1 / (2 * 3.14 * a *a)) * pow(2.7 , (-(pow((0) ,2 )+ pow((2) , 2) )/ (2 * a *a))) + \
                              image[r - 1][c] * (1 / (2 * 3.14 * a *a)) *pow( 2.7 , (-(pow((1) , 2) + pow((0) , 2)) / (2 * a*a))) + \
                              image[r][c]*(1 / (2 * 3.14 * a *a)) * pow(2.7 ,(-(pow((1 ) , 2) +pow( (1 ) ,2)) / (2 * a *a))) +\
                              image[r+1][c]*(1/(2*3.14*a*a))*pow(2.7,(-(pow((1),2) +pow((2),2))/(2*a*a))) + \
                              image[r - 1][c + 1] * (1/(2*3.14*a*a))*pow(2.7,(-(pow((2),2) +pow((0),2))/(2*a*a))) + \
                              image[r][c+1]*(1 / (2 * 3.14 * a *a)) * pow(2.7 , (-(pow((2) , 2) + pow((1) , 2)) / (2 * a *a))) + \
                              image[r+1][c+1]*( 1 / (2 * 3.14 * a*a)) * pow(2.7 ,(-(pow((2) , 2) + pow((2) , 2)) / (2 * a *a))))

        return image2

object=pythontasks()
img=cv2.imread('images1.jfif',0)
cv2.imshow('before',img)
after=object.gaussian(img,1)
cv2.imshow('after',after)
cv2.waitKey(0)
cv2.destroyAllWindows()