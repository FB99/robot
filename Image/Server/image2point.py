from keras.preprocessing.image import ImageDataGenerator

import keras
import numpy as np
from keras.preprocessing import image 
from keras.models import load_model
import sys
from hdfs.client import Client
import h5py


class Model():
    def __init__(self):
        self.model = None

    def load(self,model_path='output/Model.h5'):
        self.model = load_model(model_path)
    
    def predict(self,img_path):
        test_image = image.load_img(img_path, target_size = (128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0) 
        if self.model is None:
            print("please load or create model firstly")
            return None
        else:
            result = self.model.predict(test_image)
            dic_res = {}
            dic_res['grasping_point'] = result
            return dic_res
    
    def predict2(self,img_byte_array):
        test_image = np.expand_dims(img_byte_array, axis=0) 
        if self.model is None:
            print("please load or create model firstly")
            return None
        else:
            result = self.model.predict(test_image)
            dic_res = {}
            dic_res['grasping_point'] = result
            return dic_res
        

if(__name__=='__main__'):
    
    model = Model()
    ans = model.predict('dog.2.jpg')
    print(ans)    
