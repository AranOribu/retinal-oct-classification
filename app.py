import os
import base64
from io import BytesIO
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request, render_template, redirect, jsonify

model = tf.keras.models.load_model('./model/V2/retinal-octV2-94ACC.h5')

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(img):
    img = img.resize((150, 150))
    img = np.expand_dims(img, 0)
    img = np.stack((img,)*3, axis=-1)
    return img

def predict_result(img):
    with tf.device('/CPU:0'):
        Y_pred = model.predict(img)
    predicted_class = np.argmax(Y_pred, axis=1)
    predicted_probability = Y_pred[0][predicted_class[0]] * 100
    return class_labels[predicted_class[0]], predicted_probability



class_labels = {
    0: 'CNV',
    1: 'DME',
    2: 'DRUSEN',
    3: 'NORMAL'
}

@app.route('/upload', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return redirect(request.url)

        images = []
        for file in request.files.getlist('files[]'):
            if allowed_file(file.filename):
                img_str = base64.b64encode(file.read()).decode('utf-8')
                img = Image.open(BytesIO(base64.b64decode(img_str)))
                images.append((img_str, img))

        predictions = [(img_str, *predict_result(prepare_image(img))) for img_str, img in images]
        return render_template('index.html', predictions=predictions, class_labels=class_labels)

    return render_template('index.html')


@app.route('/predict-api', methods=['POST'])
def predict_api():
    if 'files[]' not in request.files:
        return jsonify(error='No files provided'), 400

    images = []
    for file in request.files.getlist('files[]'):
        img = Image.open(file.stream)
        images.append(img)

    predictions = [predict_result(prepare_image(img)) for img in images]

    response = []
    for i, (class_label, prob) in enumerate(predictions):
        response.append({
            'image_id': i,
            'class_label': class_label,
            'probability': prob
        })

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
