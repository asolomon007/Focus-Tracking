# Focus-Tracking

My focus tracking program tracks whether I am paying attention or not while driving.

[Imgur](https://imgur.com/a/pfHOOU7)

## The Algorithm

My project uses a custom model retrained with the resnet18 network. I have three datesets that are tuned to recognize me either paying attention or being distracted. It can also detect the absence of a person which is helpful because there is no need for a result if nobody is there. While I am looking at the camera which would be positioned in front of me (so I look in a similar direction to the camera while I am driving), the attentive mode is triggered which will slowly beep every five seceonds to display standby. In the event of me being distracted, the buzzer will beep every half second. The "not detected" mode will not play a sound as it would be unnecesarry. While attention is detected, it is checked every five seconds which saves more energy. While I am distracted, it is actively checking every half second waiting for me to pay attention again.

## Running my project

**My project was trained with a custom dataset that I developed off of me, results are likely to vary for other people due to the fact that this is trained to recognize me. For best results, retraining with another custom network would be necesary.

- The piezoelectric buzzer must be connected to the Jetson Nano's GPIO pin 12 which has an output of 5V, and grounded to any ground pin.

- Before Running:
  - Jetson Inference must be downloaded
  - Ensure that your settings allow control of the GPIO Pins

– Required Files:
  - focus-tracking.py, labels.txt, resnet18.onnx and TrackingDataset Folder
  
To Run: within the folder of this project, run: $ python3 focus-tracking.py
  
https://youtu.be/i8LZ_Jxxv1Qhttps://youtu.be/i8LZ_Jxxv1Q
