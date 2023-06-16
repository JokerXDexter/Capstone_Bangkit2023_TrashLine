from PIL import Image
from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array, ImageDataGenerator, load_img
import tensorflow as tf
import io
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = keras.models.load_model("model.h5")

def transform_image(img):
    img = img.resize((224, 224))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, axis=0)
    return img

def predict(x):
    predictions = model.predict(x)
    pred = np.argmax(predictions, axis=1)
    return pred

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def index():
    if 'file' not in request.files:
        return jsonify({"error": "no file"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "no file"})

    try:
        image_bytes = file.read()
        pillow_img = Image.open(io.BytesIO(image_bytes))
        transformed_img = transform_image(pillow_img)
        prediction = predict(transformed_img)
        data = {"prediction": int(prediction)}
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)