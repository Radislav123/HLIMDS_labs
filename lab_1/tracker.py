from sensor import Sensor
from servo import Servo
from led import Led
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

    def __init__(self, bounding_box_grayscale = True):
        self.sensor = Sensor()
        self.servo = Servo()
        self.led = Led()
        # load the pre-trained neural network
        self.neural_network = cv2.dnn.readNetFromCaffe(
            "MobileNetSSD_deploy.prototxt.txt",
            "MobileNetSSD_deploy.caffemodel"
        )
        if bounding_box_grayscale:
            self.bounding_box_colors = [[x, x, x] for x in range(0, 255, 255 // len(self.CATEGORIES))]
        else:
            self.bounding_box_colors = numpy.random.uniform(255, 0, size = (len(self.CATEGORIES), 3))

    @staticmethod
    def get_video_stream():
        return cv2.VideoCapture(0)

    def process_frame(self, frame):
        # create a blob
        # a blob is a group of connected pixels in a binary
        # frame that share some common property (e.g. grayscale value)
        # preprocess the frame to prepare it for deep learning classification
        frame_blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, self.RESIZED_DIMENSIONS),
            self.IMG_NORM_RATIO,
            self.RESIZED_DIMENSIONS,
            127.5
        )
        # set the input for the neural network
        self.neural_network.setInput(frame_blob)
        # predict the objects in the image
        neural_network_output = self.neural_network.forward()
        return neural_network_output

    def set_bounding_boxes(self, frame, neural_network_output):
        for i in numpy.arange(0, neural_network_output.shape[2]):
            category_id = int(neural_network_output[0, 0, i, 1])
            # left only persons
            if category_id == 15:
                confidence = neural_network_output[0, 0, i, 2]
                # confidence must be at least 30%
                if confidence > 0.30:
                    h, w = frame.shape[:2]
                    bounding_box = neural_network_output[0, 0, i, 3:7] * numpy.array([w, h, w, h])
                    start_x, start_y, end_x, end_y = bounding_box.astype("int")
                    label = self.CONFIDENCE_FORMAT.format(
                        [x for x in self.CATEGORIES.values()][category_id],
                        confidence * 100
                    )
                    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), self.bounding_box_colors[category_id], 2)
                    y = start_y - 15 if start_y - 15 > 15 else start_y + 15
                    cv2.putText(frame, label, (start_x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                self.bounding_box_colors[category_id], 2)

                    # gpio stuff
                    # led
                    self.led.light_on()
                    # sensor
                    print(self.sensor.get_distance_string(self.sensor.get_distance()))
                    # servo
                    center_x = (start_x + end_x) / 2
                    if center_x > w // 8 * 5:
                        self.servo.change_angle(1)
                    elif center_x < w // 8 * 3:
                        self.servo.change_angle(-1)
                else:
                    # gpio stuff
                    # led
                    self.led.light_off()

    def track_on_video_stream(self, video_stream):
        while video_stream.isOpened():
            success, frame = video_stream.read()

            if success:
                reflected_frame = cv2.flip(frame, 1)
                neural_network_output = self.process_frame(reflected_frame)
                self.set_bounding_boxes(reflected_frame, neural_network_output)
                cv2.imshow("camera", reflected_frame)

                # escape key
                if cv2.waitKey(100) == 27:
                    break

        video_stream.release()


if __name__ == "__main__":
    tracker = Tracker()
    tracker.track_on_video_stream(tracker.get_video_stream())
