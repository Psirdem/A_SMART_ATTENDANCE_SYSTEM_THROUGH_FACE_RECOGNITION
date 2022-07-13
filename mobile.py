import cv2

ip_ulr = "http://192.168.43.1:8080"

cam = f"{ip_ulr}/video"

cap = cv2.VideoCapture(cam)

while True:
    ret,frame = cap.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (800,400))
    cv2.imshow("mobile camera",frame)
    if cv2.waitKey(10)==ord('q'):
        break
cap.release() 
cv2.destroyAllWindows()   
