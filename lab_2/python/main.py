import matplotlib.pyplot as plt
from network import Network
import numpy


WEIGHTS_PATH = "../data/weights_list.txt"
WEIGHTS_HEX_PATH = "../data/weights_list.hex"
IMAGE_PATH = "../data/standard.bmp"


def read_image(path):
    image = plt.imread(path)
    plt.imshow(image)
    plt.show()
    return image


def rgb_to_bin(image):
    image_grayscale = numpy.dot(image[..., :3], [1, 1, 1]) / 765
    image_grayscale[image_grayscale == 0] = -1
    image_grayscale = image_grayscale.astype(numpy.int8)
    return image_grayscale


if __name__ == "__main__":
    data = read_image(IMAGE_PATH)
    data = rgb_to_bin(data)
    flat_data = data.ravel()

    network = Network(flat_data.shape[0])
    network.train(flat_data)
    # network.print_weights()
    network.write_weights(WEIGHTS_PATH)
    network.write_weights(WEIGHTS_HEX_PATH, True)
