import cv2 
f = open("coordinatess.txt","w")

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img,"coordinatess (%d,%d)"%(x,y),(60,60),2,1,(0,255,0)) 
        f.write(str(x)+"\n")                                              
        f.write(str(y)+"\n")                                              
img = cv2.imread("vigcerti.jpg")


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_circle)

while(1):
    
    cv2.imshow('image',img)
    if cv2.waitKey(10) & 0xFF == 27:   #Press Escape Key to terminate window
        break
cv2.destroyAllWindows()   

f.close()