import base64
#import numpy as np
import cv2
import requests
import json
import sys
from IPython import embed
test = sys.argv[1]
thresh = float(input("threshold (0-1)"))
with open(test, "rb") as f:
    im_b64 = base64.b64encode(f.read()).decode("utf-8")
# image = cv2.imread("test.jpg")
# imm = cv2.imencode('.jpg', image)[1]#.tostring()
# embed()
url = "http://ec2-3-144-225-203.us-east-2.compute.amazonaws.com:8000/vision"
pay = {"b64":im_b64,"threshold":thresh}
#embed()
#pay2 = str(pay).encode()
#pay=str(pay).encode('utf-8')
#print(pay2)
a=requests.get(url,json=json.dumps(pay))
print(a.content)



img = cv2.imread(f"{test}")

data = json.loads(a.content)
for box in data["boxes"]:
    
    x, y, w, h = box
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,0), 1)
    embed()
cv2.imshow("Image", img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
#key = cv2.waitKey(0)


