import numpy as np
import cv2
import base64


cap = cv2.VideoCapture(0)


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
#frame = cv2.flip(frame,0)

# write the flipped frame


        cv2.imshow('frame',frame)
        if cv2.waitKey(20) :
            retval, buffer = cv2.imencode('.jpg', frame)
            cv2.imwrite("b64.jpg",frame)
            jpg_as_text = base64.b64encode(buffer)
            #jpg_as_text = jpg_as_text[2:len(jpg_as_text)-1]
            file = open("b64.txt", "w")

            jpg_as_text= str(jpg_as_text)
            

            file.write(jpg_as_text)
            break

    else:
        break

# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()
