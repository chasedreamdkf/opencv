import cv2


if __name__ == "__main__":
    print(cv2.getVersionString())

    image = cv2.imread("opencv_logo.jpg")
    print(image.shape)

    cv2.imshow("image", image)
    cv2.waitKey()

