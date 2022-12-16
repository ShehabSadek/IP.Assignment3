import cv2 as cv
import numpy as np
import os
#orange
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
images_folder=os.path.join(BASE_DIR,"Images")

# low=np.array([5,50,50])

low=np.array([5,150,150])
high=np.array([15,255,255])