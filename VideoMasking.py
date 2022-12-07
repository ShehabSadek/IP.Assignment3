from Globals import *
def vidMasking():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        # cv.imshow('original',frame)

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        mask=cv.inRange(hsv,low,high)
        imask = mask>0
        orange = np.zeros_like(frame, np.uint8)
        orange[imask] = frame[imask]

        vertical_concat = np.concatenate((frame, orange), axis=0)

        cv.imshow('vid comparison',vertical_concat)

        if cv.waitKey(1) == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()