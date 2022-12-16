#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import jetson.inference
import jetson_utils
import argparse
import sys
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

input = jetson.utils.videoSource("/dev/video0", argv=sys.argv)
output = jetson.utils.videoOutput("", argv=sys.argv)
netFolder = os.path.split(__file__)[0]
paramaters = [f"--model={os.path.join(netFolder, 'resnet18.onnx')}", "--input_blob=input_0", "--output_blob=output_0", f"--labels={os.path.join(netFolder, 'labels.txt')}"]
# load the recognition network
net = jetson.inference.imageNet("resnet18", paramaters)

# find the object description
# class_desc = net.GetClassDesc(class_idx)

# print out the result
# print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
def buzzer():
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(12, GPIO.LOW)
buzzer()

while output.IsStreaming():
    image = input.Capture(format='rgb8')  # can also be format='rgba8', 'rgb32f', 'rgba32f'
    class_idx, confidence = net.Classify(image)
    class_desc = net.GetClassDesc(class_idx)
    
    if class_idx == 0:
        #Attentive
        print("Attentive")
        buzzer()
        time.sleep(5)
    elif class_idx == 1:
        print("Not Attentive")
        #Not Attentive
        buzzer()
        time.sleep(0.1)
    elif class_idx == 2:
        print("Not Present")
        #Not Present

