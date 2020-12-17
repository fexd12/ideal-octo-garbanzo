from tensorflow.keras.datasets import fashion_mnist
from PIL import Image
import os
import random

(x_train,y_train),(x_teste,y_teste) = fashion_mnist.load_data()

for i in range(0,5):

    idx = random.randrange(0,len(x_teste))
    img  = Image.fromarray(x_teste[idx])
    img.save('uploads_images/{}.jpg'.format(idx))
    os.remove('uploads_images/{}.jpg'.format(idx))
