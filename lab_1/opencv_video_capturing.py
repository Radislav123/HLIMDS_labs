import cv2


# '0' - camera number
video_stream = cv2.VideoCapture(0)

# saving images and videos
# https://docs.google.com/document/d/11pA2lgObwpOZl51K4_CmMOTmWCd2NKq7ogmkU3c9kXg/edit
while video_stream.isOpened():
    ret_val, frame = video_stream.read()
    if ret_val:
        # flip - reflect an image
        cv2.imshow("camera", cv2.flip(frame, 1))
        # escape key
        if cv2.waitKey(100) == 27:
            break

video_stream.release()
cv2.destroyAllWindows()
