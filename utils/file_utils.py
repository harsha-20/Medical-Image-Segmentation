'''
Created on Mar 13, 2018
@author: yaniv gur
'''
import io
import os
import base64
import numpy as np
from io import BytesIO
from PIL import Image

def file_upload(parsed_files, upload_path):
    # get file from client and save on server
    if parsed_files.get("image") != None:
        file = parsed_files.get("image")
        filename = parsed_files.get("image").filename
        file.save(os.path.join(upload_path, filename))
    else:
        return None

    return filename


def convert_to_base64(seg):
    buffer = io.BytesIO()
    img = Image.fromarray(np.uint8(seg))
    img.save(buffer, "png")
    #img_encoded = base64.standard_b64encode(buffer.getvalue())
    img_encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_encoded

def convert_base64_to_img(base64_string):
    image = Image.open(BytesIO(base64.b64decode(base64_string)))
    img_array = np.array(image)
    return img_array