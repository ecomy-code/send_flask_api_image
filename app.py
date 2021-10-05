from flask import Flask, jsonify, request
from PIL import Image
import json
import base64
from io import BytesIO
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    json_data = request.get_json() #POSTDATA
    dict_data = json.loads(json_data)
    img = dict_data["img"]
    img = base64.b64decode(img)
    img = BytesIO(img)
    img = Image.open(img)
    #img.show()

    img.save('rasto.png')

    
    img_shape = img.size

    text = "Se ha cambiado con é" 

    response = {
        "text" : text,
        "img_shape":img_shape        
        }

    return jsonify(response)





if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 2555)
