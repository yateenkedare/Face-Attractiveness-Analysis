import os.path
import cv2
import stasm
import numpy as np
import math

def calculateEuclideanDistance(pointA, pointB):
    return np.linalg.norm(pointA-pointB, ord=2)

def calculateGoldenRatio(img):
    landmarks = stasm.search_single(img)

    if len(landmarks) == 0:
        return -1
    else:
        landmarks = stasm.force_points_into_image(landmarks,img)
        lips = [ (landmarks[67][0] + landmarks[70][0])/2 , (landmarks[67][1] + landmarks[70][1])/2 ]
        #a = calculateEuclideanDistance(landmarks[change], landmarks[6])
        #b = calculateEuclideanDistance(landmarks[change], landmarks[38])
        c = calculateEuclideanDistance(landmarks[38], landmarks[56])
        d = calculateEuclideanDistance(landmarks[14], lips)
        e = calculateEuclideanDistance(landmarks[56], landmarks[54])
        f = calculateEuclideanDistance(landmarks[34], landmarks[44])
        g = calculateEuclideanDistance(landmarks[0], landmarks[12])
        h = calculateEuclideanDistance(landmarks[14], landmarks[38])
        i = calculateEuclideanDistance(landmarks[56], landmarks[6])
        j = calculateEuclideanDistance(lips, landmarks[6])
        k = calculateEuclideanDistance(landmarks[62], landmarks[74])
        l = calculateEuclideanDistance(landmarks[56], lips)

        #res1 = a/g
        #res2 = b/d
        res3 = i/j
        res4 = i/c
        res5 = e/l
        res6 = f/h
        res7 = k/e

        #finalRes = (res1 + res2 + res3 + res4 + res5 + res6 + res7)/7
        finalRes = (res3 + res4 + res5 + res6 + res7)/5
        return finalRes



img = cv2.imread("a.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Cannot load", path)
    raise SystemExit

goldenRatio = calculateGoldenRatio(img)
if(goldenRatio < 0):
    print("No face found")

print goldenRatio

#cv2.imshow("stasm minimal", img)
#cv2.waitKey(0)
