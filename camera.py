import cv2
#from PIL import Image
from pyzbar import pyzbar
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#cv2.namedWindow("live", cv2.WINDOW_AUTOSIZE); # 命名一個視窗，可不寫
while(True):
    # 擷取影像
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 彩色轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    original_image = frame
    barcodes = pyzbar.decode(gray)
    
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print(x,y)
        cv2.putText(original_image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)
    # 顯示圖片
    cv2.imshow('live', original_image)
    #cv2.imshow('live', gray)
    # 按下 q 鍵離開迴圈 
    if cv2.waitKey(1) == ord('q'):
        #image = Image.fromarray(original_image.astype(np.uint8))
        #image.show()
        break

cap.release()
cv2.destroyAllWindows()
