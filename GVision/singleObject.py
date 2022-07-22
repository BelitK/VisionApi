import cv2
import sys
import json
import base64
import requests

from IPython import embed
# python singleObject.py .\image.jpg
test = sys.argv[1]
with open(test, "rb") as f:
    im_b64 = base64.b64encode(f.read()).decode("utf-8")
pay = {
    "payload": {
        "image": {
            "imageBytes": im_b64
        }
    }
}

json.dump(pay, open("test.json", "w"))
headers = {
    'Authorization': 'insert token here',
    'Content-Type': 'application/json; charset=utf-8',
}

with open('test.json', "rb") as f:
    data = f.read()
response = requests.post(
    'insert adress here', headers=headers, data=data)

sonuc = json.loads(response.content)
print(sonuc)
con_score = sonuc['payload'][0]['classification']['score']
clas_name = sonuc['payload'][0]['displayName']
print(sonuc['payload'][0]['classification']['score'])
print(sonuc['payload'][0]['displayName'])

img = cv2.imread(f"{test}")
font = cv2.FONT_HERSHEY_SIMPLEX

# org
fonts = 1

# Blue color in BGR
color = (255, 255, 255)
thickness = 2
image = cv2.putText(img, "confidence =" + str(con_score), (20, 20), font,
                    fonts, color, thickness)
image = cv2.putText(img, "class = " + clas_name, (50, 50), font,
                    fonts, color, thickness)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# embed()
