import numpy as np
import cv2 as ocv
class pythTasks :

    def im2double(self,image):
        max_val=np.max(image)
        min_val=np.min(image)
        val=(image.astype('float')-min_val)/(max_val-min_val)
        return  val
    def incGrayLevel(self,image,k):
        image=self.im2double(image)
        image=np.array(image)
        row,col=np.shape(image)
        for r in range(row):
            for c in range(col):
                image[r][c]=image[r][c]*k

        return image

    def decreaseGrayLevel(self,image,k):
        image=self.im2double(image)
        image=np.array(image)
        row,col=np.shape(image)
        for r in range(row):
            for c in range(col):
                image[r][c]=image[r][c]/k

        return image
    def deltaRule(self,image,k):
        image=self.im2double(image)
        image=np.array(image)
        row,col=np.shape(image)
        for r in range(row):
            for c in range(col):
                image[r][c]=np.abs(image[r][c]/k)*k

        return image

obj1 = pythTasks()
im=ocv.imread('Lenna_(test_image).png',0)
ocv.imshow("lena",im)
im2=obj1.decreaseGrayLevel(im,2)
ocv.imshow('Increse Gray Level',im2)
im2=obj1.incGrayLevel(im,2)
ocv.imshow('Decrease Gray Level',im2)
im2=obj1.deltaRule(im,2)
ocv.imshow('Delta Rule',im2)
ocv.waitKey()
ocv.destroyAllWindows()