import cv2

if __name__ == "__main__":
    image = cv2.imread("attachments/bread_board.PNG")
    cv2.imshow('', image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
