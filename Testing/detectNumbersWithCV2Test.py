import cv2
img = cv2.imread('../material/letter_detection_test_img.jpeg')
window_name = 'letter detection test image'
cv2.imshow(window_name, img)
