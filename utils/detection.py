import numpy as np
import cv2

def detect_colors(image_cv, hsv, color_ranges, label_colors):
    output = image_cv.copy()
    min_area = 800

    for color in color_ranges:
        lower = np.array(color_ranges[color][0])
        upper = np.array(color_ranges[color][1])
        mask = cv2.inRange(hsv, lower, upper)

        if color == 'Red':
            lower2 = np.array(color_ranges['Crimson'][0])
            upper2 = np.array(color_ranges['Crimson'][1])
            mask += cv2.inRange(hsv, lower2, upper2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > min_area:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(output, (x, y), (x + w, y + h), label_colors[color], 2)
                text_y = y - 10 if y - 10 > 10 else y + 20
                cv2.putText(output, color, (x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, label_colors[color], 2)

    return output
