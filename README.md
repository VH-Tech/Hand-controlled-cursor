# Hand-controlled-cursor
control your computers cursor with your hand using OpenCV and Python3

<h3>How it works?</h3>
1. Detects user's hand using colour based image segmentation.<br>
2. calculates the ratio of user's screen to image source.<br>
3. find's the coordinates of center of the hand.<br>
4. Moves the cursor according to the coordinates of hand multiplied by the aspect ratio.<br>
