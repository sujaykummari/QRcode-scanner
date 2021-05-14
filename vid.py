#import libraries
from cv2 import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font,1 , (255, 255, 255), 1)
        #3
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame

def main():
    #1
    camera = cv2.VideoCapture(0)
    camera.set(3, 1000)
    # 3 means height
    camera.set(4,1000)
    # 4 means width
    camera.set(10,100)
    #2
    
    while True:
            
        isTrue , frame = camera.read()
        frame = cv2.flip(frame,1)
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #3
    camera.release()
    cv2.destroyAllWindows()

#4  
if __name__ == '__main__':
    main()