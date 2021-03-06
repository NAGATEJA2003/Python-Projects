import numpy as np
import cv2
cap = cv2.VideoCapture (0)
Width = int (cap.get (3))
Height = int (cap.get (4))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc (* 'XVID')
#out = cv2.VideoWriter ('../ desktop/output.avi', fourcc, 20.0, (640,480))
out = cv2.VideoWriter ('output.mp4', fourcc, 20, (Width, Height))
while (cap.isOpened ()):
    ret, frame = cap.read ()
    if ret == True:
        frame = cv2.flip (frame, 1)
        # write the flipped frame
        out.write (frame)
        cv2.imshow ('frame', frame)
        if cv2.waitKey (1)&0xFF == ord ('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release ()
out.release ()
cv2.destroyAllWindows ()
