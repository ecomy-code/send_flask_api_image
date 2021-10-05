import requests
from PIL import Image
import json
import base64
from io import BytesIO
import time
def enviar_imagen(url_foto):
	try:
		img = Image.open(url_foto)
		image_toBytes = BytesIO()
		img.save(image_toBytes, format=img.format)
		image_toBytes = image_toBytes.getvalue()
		image_encoding = base64.b64encode(image_toBytes)
		image_convert_json = image_encoding.decode('utf-8') #Se completa conversión
		time.sleep(1)
		files = {
		    "text" : "Diccionario enviado con la imagen",
		    "img" : image_convert_json
		    }

		r = requests.post("http://192.168.0.14:2555", json=json.dumps(files)) #POST to server as json

		print(r.json())
	except Exception as e:
		print("ha ocrurrido un error ->: " + str(e))

enviar_imagen("./test.png") # Se agrega URL DE LA IMAGEN
