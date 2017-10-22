
import cv2
import base64


def use():
    cap = cv2.VideoCapture(0)


    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
    #frame = cv2.flip(frame,0)

    # write the flipped frame


            cv2.imshow('frame',frame)
            if cv2.waitKey(420) :
                retval, buffer = cv2.imencode('.jpg', frame)
                jpg_as_text = base64.b64encode(buffer)

                return(jpg_as_text)

        else:
            break

# Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()
    #out.release()


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    use()
