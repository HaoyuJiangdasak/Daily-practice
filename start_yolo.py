from ultralytics import YOLO
import cv2
def main():
    model = YOLO("yolov8n.pt") 
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("没开摄像头")
        return
    print("按q退出")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()