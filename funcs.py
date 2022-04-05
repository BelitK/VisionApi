import cv2
import base64

import numpy as np


def get_coor(image, threshold=0.3):
    """Object detection using YOLO"""
    net = cv2.dnn.readNet("yolov3_training_last.weights", "yolotest.cfg")
    layer_names = net.getLayerNames()

    # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
    im_bytes = base64.b64decode(image.encode('utf-8'))
    # im_arr is one-dim Numpy array
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    #frame = cv2.resize(img, None, fx=0.4, fy=0.4)
    frame=img
    # 640 * 420 image size limit for better performance
    height, width, channels = frame.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(
        frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > threshold:
                # nesne algilandi
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # sinirlayicci bolge koordinatlari
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    final = {"boxes": boxes, "confidence": confidences}
    return final

# TODO add human detection as second example


def get_human(image):
    """Human detection using Hog-SVM"""
    # set hog descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    # get image and encode
    im_bytes = base64.b64decode(image.encode('utf-8'))
    # im_arr is one-dim Numpy array
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    (humans, _) = hog.detectMultiScale(img,
                                       winStride=(5, 5),
                                       padding=(3, 3),
                                       scale=1.21)

    final = {"boxes": humans.tolist()}
    return final
