import cv2

# load haar classifier
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img

# img = cv2.imread('people.png')
# img = detect(img)

cap = cv2.VideoCapture(0)  # 0:built-in camera
if cap.isOpened() == False:
    print("error!")

while(True):
    ret, frame = cap.read()
    frame = detect(frame)
    cv2.imshow('frame', frame)     # frame show
    if ret == True:
        frame = cv2.flip(frame, 1) # frame flip
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
writer.release()
# cv2.imshow('face detect',img)
# cv2.waitKey(0)
cv2.destroyAllWindows()