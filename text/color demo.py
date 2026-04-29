import cv2
import numpy as np

def main():
    camera_id = 0 
    cap = cv2.VideoCapture(camera_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    COLOR_DEFINITIONS = {
        "Black": {
            "lower": [np.array([0, 0, 0])],
            "upper": [np.array([180, 255, 46])],
            "bgr_color": (100, 100, 100)
        },
        "Red": {
            "lower": [np.array([0, 120, 70]), np.array([150, 120, 70])],
            "upper": [np.array([10, 255, 255]), np.array([180, 255, 255])],
            "bgr_color": (0, 0, 255)
        },
        "Green": {
            "lower": [np.array([35, 43, 46])],
            "upper": [np.array([77, 255, 255])],
            "bgr_color": (0, 255, 0)
        },
        "Blue": {
            "lower": [np.array([100, 43, 46])],
            "upper": [np.array([124, 255, 255])],
            "bgr_color": (255, 0, 0)
        },
        "Yellow": {
            "lower": [np.array([26, 43, 46])],
            "upper": [np.array([34, 255, 255])],
            "bgr_color": (0, 255, 255)
        },
        "Orange": {
            "lower": [np.array([11, 43, 46])],
            "upper": [np.array([25, 255, 255])],
            "bgr_color": (0, 165, 255)
        },
        "Purple": {
            "lower": [np.array([125, 43, 46])],
            "upper": [np.array([149, 255, 255])],
            "bgr_color": (255, 0, 130)
        }
    }
    
    min_area_threshold = 500
    while True:
        ret, frame = cap.read()
        if not ret:
            print("gg")
            cv2.waitKey(100)
            continue
            
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_frame)
        v = cv2.equalizeHist(v)
        hsv_frame_robust = cv2.merge([h, s, v])
        
        for color_name, definition in COLOR_DEFINITIONS.items():
            
            current_mask = cv2.inRange(hsv_frame_robust, definition["lower"][0], definition["upper"][0])
            if len(definition["lower"]) > 1:
                mask_part2 = cv2.inRange(hsv_frame_robust, definition["lower"][1], definition["upper"][1])
                current_mask = cv2.add(current_mask, mask_part2)
                
            kernel = np.ones((5, 5), np.uint8)
            mask_eroded = cv2.erode(current_mask, kernel, iterations=2)
            mask_final = cv2.dilate(mask_eroded, kernel, iterations=2)
            
            contours, _ = cv2.findContours(mask_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) > min_area_threshold:
                    x, y, w, h = cv2.boundingRect(contour)
                    label_color = definition["bgr_color"]
                    label_text = color_name
                    cv2.rectangle(frame, (x, y), (x + w, y + h), label_color, 2)
                    (text_w, text_h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                    cv2.rectangle(frame, (x, y - text_h - 10), (x + text_w, y), label_color, -1)
                    cv2.putText(frame, label_text, (x, y - 5), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)                               
        cv2.imshow("Color Detection", frame)     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break           
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()