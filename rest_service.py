import os
import numpy as np
from flask_cors import cross_origin
from flask import Flask, jsonify, request
from keras.models import load_model
from utils.dice import dice_coef
from utils.file_utils import convert_to_base64, file_upload
from PIL import Image

IMG_COLS = 128
IMG_ROWS = 128
UPLOAD_PATH = '/Users/akararg/Desktop'
model = load_model('/Users/akararg/Desktop/unet_model_16_filters_kernel10x10.h5',custom_objects={'dice_coef':dice_coef})

# setting config file location
app = Flask(__name__)

@app.route('/segment/cxr', methods=['POST'])
@cross_origin()
def segment_cxr():

    parsed_files = request.files

    # get file for upload
    filename = file_upload(parsed_files, UPLOAD_PATH)
    if filename == None:
        output = {"Error": "A file has not been sent to the server!"}
        return jsonify(output)

    image = Image.open(os.path.join(UPLOAD_PATH, filename))

    # convert to grayscale and reshape the array to the network input
    image = image.resize((IMG_COLS, IMG_ROWS))
    image = image.convert('L')
    image = np.asarray(image, dtype=np.float32)
    image/=255
    image = np.reshape(image,(1,IMG_COLS, IMG_ROWS, 1))

    segmentation = model.predict(image).argmax(axis=3)
    segmentation = np.squeeze(segmentation)

    image_encoded = convert_to_base64(segmentation)
    return image_encoded


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5201, debug=False)



