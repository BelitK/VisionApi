import base64
import cv2
import requests
import json
import sys
from IPython import embed
test = sys.argv[1]
thresh = float(input("threshold (0-1)"))
with open(test, "rb") as f:
    im_b64 = base64.b64encode(f.read()).decode("utf-8")

url = "http://ec2-3-144-225-203.us-east-2.compute.amazonaws.com:8000/vision"
pay = {"b64":im_b64,"threshold":thresh}
a=requests.get(url,json=json.dumps(pay))
print(a.content)


# TODO get image from url implement
img = cv2.imread(f"{test}")

data = json.loads(a.content)
for box in data["boxes"]:
    
    x, y, w, h = box
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,0), 1)
    #embed()
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


