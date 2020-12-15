import tensorflow as tf

def load_model():

    with open('fashion_model_flask.json','r') as f:
        model_json = f.read()

    model = tf.keras.models.model_from_json(model_json)
    model.load_weights("fashion_model_flask.h5")

    return model