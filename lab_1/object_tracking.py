import numpy
import cv2

RESIZED_DIMENSIONS = (300, 300)  # Dimensions that SSD was trained on.
IMG_NORM_RATIO = 0.007843  # In grayscale a pixel can range between 0 and 255

# Load the pre-trained neural network
neural_network = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

# List of categories and classes
categories = {
    0: 'background',
    1: 'aeroplane',
    2: 'bicycle',
    3: 'bird',
    4: 'boat',
    5: 'bottle',
    6: 'bus',
    7: 'car',
    8: 'cat',
    9: 'chair',
    10: 'cow',
    11: 'diningtable',
    12: 'dog',
    13: 'horse',
    14: 'motorbike',
    15: 'person',
    16: 'pottedplant',
    17: 'sheep',
    18: 'sofa',
    19: 'train',
    20: 'tvmonitor'
}

classes = [
    "background",
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tvmonitor"
]

# Create the bounding boxes
bbox_colors = numpy.random.uniform(255, 0, size = (len(categories), 3))


def main():
    video_stream = cv2.VideoCapture(0)

    while video_stream.isOpened():
        success, frame = video_stream.read()

        if success:
            (h, w) = frame.shape[:2]

            # Create a blob. A blob is a group of connected pixels in a binary
            # frame that share some common property (e.g. grayscale value)
            # Preprocess the frame to prepare it for deep learning classification
            reflected_frame = cv2.flip(frame, 1)
            frame_blob = cv2.dnn.blobFromImage(cv2.resize(reflected_frame, RESIZED_DIMENSIONS),
                                               IMG_NORM_RATIO, RESIZED_DIMENSIONS, 127.5)

            # Set the input for the neural network
            neural_network.setInput(frame_blob)

            # Predict the objects in the image
            neural_network_output = neural_network.forward()

            # Put the bounding boxes around the detected objects
            for i in numpy.arange(0, neural_network_output.shape[2]):
                confidence = neural_network_output[0, 0, i, 2]

                # Confidence must be at least 70%
                if confidence > 0.70:
                    idx = int(neural_network_output[0, 0, i, 1])
                    bounding_box = neural_network_output[0, 0, i, 3:7] * numpy.array([w, h, w, h])
                    (startX, startY, endX, endY) = bounding_box.astype("int")
                    label = "{}: {:.2f}%".format(classes[idx], confidence * 100)
                    cv2.rectangle(frame, (startX, startY), (endX, endY), bbox_colors[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bbox_colors[idx], 2)

            cv2.imshow("camera", frame)

            # escape key
            if cv2.waitKey(100) == 27:
                break
    video_stream.release()


if __name__ == "__main__":
    main()
