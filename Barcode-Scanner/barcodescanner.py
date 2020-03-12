from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im):
    decodedobjects = pyzbar.decode(im)

    for obj in decodedobjects:
        print('Type:',obj.type)
        print('Data: ',str(obj.data),'\n')

    return decodedobjects


def display(im,decodedobjects):
    for decodedobject in decodedobjects:
        points = decodedobject.polygon

        if len(points) >4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.sequeeze(hull)))

        else:
            hull = points

        n = len(hull)

        for j in range(0,n):
            cv2.line(im,hull[j],hull[ (j+1) %n],(255,0,0),3)
    cv2.imshow("Results",im)
    cv2.waitKey(0)


if __name__ == '__main__':

  # Read image
  im = cv2.imread('zbar-test.jpg')

  decodedObjects = decode(im)
  display(im, decodedObjects)

