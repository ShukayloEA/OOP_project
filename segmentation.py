import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd

import keras
from keras.models import Model, load_model

import matplotlib.image

def segmentation(input, output):
    model = keras.models.load_model("my_model_v10.h5")

    image = cv2.imread(input)
    
#    (w, h) = image.shape[:-1]
    
    image = cv2.resize(image, (256, 256))
    matplotlib.image.imsave(input, image)
    pred = model.predict(np.array([image]))
    image_output = pred[0, ..., 0] > 0.5
#    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 25))
#    axes[0].imshow(image)
#    axes[1].imshow(image_output)
#    plt.show()

    matplotlib.image.imsave(output, image_output)
#    cv2.imwrite(output, image_output)
#    image_output = cv2.resize(image_output, (w, h))
#    print("after resize")
#    with open(output,'wb') as new_file:
#            new_file.write(image_output)


segmentation("C:\\Users\\Aila\\OOP project\\data\\test\\0ce66b539f52_01.jpg", "C:\\Users\\Aila\\OOP project\\data\\test\\0ce66b539f52_01_1.jpg")