import cv2
import pyautogui
import imutils

cap = cv2.VideoCapture(0)

(w_screen, h_screen) = pyautogui.size()

skin_lower = (0, 26, 186)  #look for upper and lower range of colour to detect
skin_upper = (255, 255, 255)

ret, im = cap.read()
im=imutils.resize(im, width=800)  #find new height
h_image = im.shape[0]

h_ratio = h_screen/h_image #compute the aspect ratios
w_ratio = w_screen/800
print(str(h_ratio) + ','+str(w_ratio))

while True:

    ret, frame = cap.read() # Capture frame-by-frame
    frame = imutils.resize(frame, width=800) #resize the frame

    blurred = cv2.GaussianBlur(frame, (11, 11), 0) #blur the image for removing noise
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #convert the image from RGB to HSV

    mask = cv2.inRange(hsv, skin_lower, skin_upper)
    mask = cv2.erode(mask, None, iterations=2) #REmove noise
    mask = cv2.dilate(mask, None, iterations=2)

    (cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

    #encircle the detected hand

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        (x,y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(frame, center, radius, (255, 0, 0), 2)
        pyautogui.moveTo(int(x)*w_ratio, int(y)*h_ratio, duration=0.001)

    cv2.imshow("Tracking", frame) #show output
    #cv2.imshow("Binary", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
