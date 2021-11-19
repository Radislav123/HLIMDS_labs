import numpy
import torch
import time
import cv2


# REPO = "pytorch/vision"
REPO = "ultralytics/yolov5"
# MODEL_NAME = "mobilenet_v2"
MODEL_NAME = "yolov5s"


def get_all_entrypoints_names():
    return torch.hub.list(REPO)


def get_entrypoint_help(entrypoint_name):
    return torch.hub.help(REPO, entrypoint_name)


class Tracker:

    def __init__(self, model):
        self.model = model
        self.model.eval()

    @staticmethod
    def get_video_stream():
        """Get video from usb-camera."""
        return cv2.VideoCapture(0)

    def score_frame(self, frame):
        """
        The function below identifies the device which is available to make the prediction
        and uses it to load and infer the frame.
        Once it has results it will extract the labels
        and coordinates(Along with scores) for each object detected in the frame.
        """

        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(device)

        frame = [torch.tensor(frame)]
        results = self.model(frame)

        labels = results.xyxyn[0][:, -1].numpy()
        cord = results.xyxyn[0][:, :-1].numpy()
        return labels, cord

    def plot_boxes(self, results, frame):
        """
        The function below takes the results and the frame as input
        and plots boxes over all the objects which have a score higher than our threshold.
        """

        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            # If score is less than 0.2 we avoid making a prediction.
            if row[4] < 0.2:
                continue
            x1 = int(row[0] * x_shape)
            y1 = int(row[1] * y_shape)
            x2 = int(row[2] * x_shape)
            y2 = int(row[3] * y_shape)
            bgr = (0, 255, 0)  # color of the box
            classes = self.model.names  # get the name of label index
            label_font = cv2.FONT_HERSHEY_SIMPLEX  # font for the label.
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)  # plot the boxes
            cv2.putText(frame, classes[labels[i]], (x1, y1), label_font, 0.9, bgr, 2)  # put a label over box.
            return frame

    def track(self):
        """
        The Function below orchestrates the entire operation and performs the real-time parsing for video stream.
        """

        video_stream = self.get_video_stream()  # get your video stream

        while video_stream.isOpened():  # run until stream is out of frames
            _, frame = video_stream.read()  # read next frame.

            start_time = time.time()  # we would like to measure the FPS.
            results = self.score_frame(frame)  # score the Frame
            frame = self.plot_boxes(results, frame)  # plot the boxes.
            end_time = time.time()

            fps = 1 / numpy.round(end_time - start_time, 3)  # measure the FPS.
            print(f"Frames Per Second : {fps}")

            reflected_frame = cv2.flip(frame, 1)
            cv2.imshow("camera", reflected_frame)  # output

            # escape key
            if cv2.waitKey(100) == 27:
                break

        video_stream.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    my_model = torch.hub.load(REPO, MODEL_NAME, pretrained = True)
    tracker = Tracker(my_model)
    tracker.track()
