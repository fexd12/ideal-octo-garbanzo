from . import bp
from .auxiliar import convert

from flask import Flask,request,jsonify
from app import cross_origin

import numpy as np

@bp.route('/',methods=['POST'])
@cross_origin()
def predict_img():
    base_dir = 'uploads/'

    data = request.get_json()

    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    
    img = convert(data['imagem'])
    img.resize((28,28))

    predictions = model.predict([img.reshape(1,img.height*img.width)])

    return jsonify({
        'img_classifier': classes[np.argmax(predictions[0])]
    }),200
