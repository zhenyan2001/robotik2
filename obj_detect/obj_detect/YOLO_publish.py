#!/usr/bin/env python3
import math

from cv_bridge import CvBridge

from ultralytics import YOLO
from sensor_msgs.msg import Image
import rclpy
import cv2

detection_model = YOLO("yolov8m.pt")
bridge = CvBridge()

def main():
    rclpy.init()
    global publisher
    node = rclpy.create_node('publisher')
    publisher = node.create_publisher(Image, '/image_raw_detect', 10)
    node.create_subscription(Image, '/image_raw', mysubcallback, 10)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

def mysubcallback(msg):
    img = bridge.imgmsg_to_cv2(msg, "bgr8")
    results = detection_model(img,stream=True)
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            #print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            #print("Class name -->", r.names[cls])
            
            if confidence >= 0.5:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(img,f"{r.names[cls], confidence}", org, font, fontScale, color, thickness)
    publisher.publish(bridge.cv2_to_imgmsg(img))

if __name__ == '__main__':
    main()