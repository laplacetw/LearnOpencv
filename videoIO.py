import cv2

cap = cv2.VideoCapture(0)  # 0:built-in camera
if cap.isOpened() == False:
    print("error!")

# define codec for video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('test.avi', fourcc, 20.0, (w, h))

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)     # frame show
    if ret == True:
        frame = cv2.flip(frame, 1) # frame flip
        writer.write(frame)        # frame write
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()