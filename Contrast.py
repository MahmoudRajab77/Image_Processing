import numpy as np
import cv2
import math
class pythontasks:
    def double (self,image):
        max_value=np.max(image)
        min_value=np.min(image)
        value=(image.astype('float')-min_value)/(max_value-min_value)
        return value




    def contrast(self,image,q):
        image=self.double(image)
        mp=math.pow(2,q)-1
        a=np.max(image)
        b=np.min(image)
        R=a-b
        row,col=np.shape(image)
        for r in range(row):
            for c in range(col):
                image[r][c]=((image[r][c]-b)/R)*mp
                image[r][c]=round(image[r][c])
        return image
obj=pythontasks()
img=cv2.imread('C:\\Users\\Mr_Tech\\Desktop\\temp.jpg',0)
cv2.imshow('before',img)
a=obj.contrast(img,2)
cv2.imshow('after',a)
cv2.waitKey(0)
cv2.destroyAllWindows()
