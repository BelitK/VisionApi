import base64
import numpy as np
import cv2
import requests
import json
from IPython import embed

with open("test.jpg", "rb") as f:
    im_b64 = base64.b64encode(f.read()).decode("utf-8")
# image = cv2.imread("test.jpg")
# imm = cv2.imencode('.jpg', image)[1]#.tostring()
# embed()
url = "http://ec2-3-144-225-203.us-east-2.compute.amazonaws.com:8000/test"
pay = {"b64":im_b64,"threshold":0.5}
#embed()
#pay2 = str(pay).encode()
#pay=str(pay).encode('utf-8')
#print(pay2)
a=requests.get(url,json=json.dumps(pay))
print(a.content)