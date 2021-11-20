import numpy
import cv2


class Tracker:
    # dimensions that SSD was trained on.
    RESIZED_DIMENSIONS = (300, 300)
    # in grayscale a pixel can range between 0 and 255
    IMG_NORM_RATIO = 0.007843
    CONFIDENCE_FORMAT = "{}: {:.2f}%"
    # list of categories
    CATEGORIES = {
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

    def __init__(self):
        # load the pre-trained neural network
        self.neural_network = cv2.dnn.readNetFromCaffe(
            "MobileNetSSD_deploy.prototxt.txt",
            "MobileNetSSD_deploy.caffemodel"
        )

    def get_bbox_colors(self, grayscale = True):
        if grayscale:
            bbox_colors = [[x, x, x] for x in range(0, 255, 255 // len(self.CATEGORIES))]
        else:
            bbox_colors = numpy.random.uniform(255, 0, size = (len(self.CATEGORIES), 3))
        return bbox_colors

    @staticmethod
    def get_video_stream():
        return cv2.VideoCapture(0)

    def track_on_video_stream(self, video_stream):
        bbox_colors = self.get_bbox_colors()

        while video_stream.isOpened():
            success, frame = video_stream.read()
            frame = cv2.flip(frame, 1)

            if success:
                (h, w) = frame.shape[:2]

                # create a blob
                # a blob is a group of connected pixels in a binary
                # frame that share some common property (e.g. grayscale value)
                # preprocess the frame to prepare it for deep learning classification
                reflected_frame = cv2.flip(frame, 1)
                frame_blob = cv2.dnn.blobFromImage(
                    cv2.resize(reflected_frame, self.RESIZED_DIMENSIONS),
                    self.IMG_NORM_RATIO,
                    self.RESIZED_DIMENSIONS,
                    127.5
                )

                # set the input for the neural network
                self.neural_network.setInput(frame_blob)
                # predict the objects in the image
                neural_network_output = self.neural_network.forward()

                # put the bounding boxes around the detected objects
                for i in numpy.arange(0, neural_network_output.shape[2]):
                    confidence = neural_network_output[0, 0, i, 2]

                    # confidence must be at least 30%
                    if confidence > 0.30:
                        category_id = int(neural_network_output[0, 0, i, 1])
                        # left only persons
                        if category_id == 15:
                            bounding_box = neural_network_output[0, 0, i, 3:7] * numpy.array([w, h, w, h])
                            (startX, startY, endX, endY) = bounding_box.astype("int")
                            label = self.CONFIDENCE_FORMAT.format(
                                [x for x in self.CATEGORIES.values()][category_id],
                                confidence * 100
                            )
                            cv2.rectangle(frame, (startX, startY), (endX, endY), bbox_colors[category_id], 2)
                            y = startY - 15 if startY - 15 > 15 else startY + 15
                            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bbox_colors[category_id], 2)

                cv2.imshow("camera", frame)

                # escape key
                if cv2.waitKey(100) == 27:
                    break
        video_stream.release()


if __name__ == "__main__":
    tracker = Tracker()
    tracker.track_on_video_stream(tracker.get_video_stream())
