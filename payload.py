import base64
import cv2
import requests
import json
import sys
test = sys.argv[1]
ob_type = sys.argv[2]

with open(test, "rb") as f:
    im_b64 = base64.b64encode(f.read()).decode("utf-8")
# python .\payload.py .\human.jpg h
if str(ob_type) == 'h':
    pay = {"b64": im_b64}
    url = "api.belitk.tech/human"

else:
    thresh = float(input("threshold (0-1) : "))
    pay = {"b64": im_b64,
           "threshold": thresh}
    url = "api.belitk.tech/vision"

#print(pay)
a = requests.get(url, json=json.dumps(pay))
print(a.content)


# TODO get image from url implement
img = cv2.imread(f"{test}")

data = json.loads(a.content)
for box in data["boxes"]:

    x, y, w, h = box
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0,255), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
