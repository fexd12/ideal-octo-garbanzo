import tensorflow as tf
import os

class ModelLoad():

    def __init__(self):
        self.model = self.load_model()
        
    def load_model(self):

        basedir = os.path.abspath(os.path.dirname(__file__))

        model_json_path = os.path.join(basedir,'fashion_model_flask.json')
        model_h5_path = os.path.join(basedir,"fashion_model_flask.h5")

        with open(model_json_path,'r') as f:
            model_json = f.read()

        model = tf.keras.models.model_from_json(model_json)
        model.load_weights(model_h5_path)

        return model