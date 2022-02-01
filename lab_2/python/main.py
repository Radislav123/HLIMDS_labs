from matplotlib import pyplot, colors
from network import Network
import numpy


# small 5x7
# big 40x40
TEST_IMAGES_SIZE = "big"
TEST_IMAGES_SHAPES = {
    "small": (5, 7),
    "medium": (40, 40),
    "big": (100, 100),
    # 16 GB RAM is not enough
    "huge": (250, 250)
}
WEIGHTS_PATH = "../data/weights_list.txt"
WEIGHTS_HEX_PATH = "../data/weights_list.hex"
IMAGE_PATH = f"../data/{TEST_IMAGES_SIZE}/standard.bmp"
BROKEN_IMAGE_PATHS = [f"../data/{TEST_IMAGES_SIZE}/broken_{i}.bmp" for i in range(3)]
COLOR_MAP = colors.ListedColormap(['black', 'white'])


def read_image(path):
    image = pyplot.imread(path)
    pyplot.imshow(image)
    pyplot.show()
    return image


def rgb_to_bin(image):
    image_grayscale = numpy.dot(image[..., :3], [1, 1, 1]) / 765
    image_grayscale[image_grayscale == 0] = -1
    image_grayscale = image_grayscale.astype(numpy.int8)
    return image_grayscale


if __name__ == "__main__":
    # train and write weights
    data = read_image(IMAGE_PATH)
    data = rgb_to_bin(data)
    pyplot.imsave(f"../data/{TEST_IMAGES_SIZE}/standard_binary.bmp", data, cmap = COLOR_MAP)
    flat_data = data.ravel()

    network = Network(flat_data.shape[0], TEST_IMAGES_SHAPES[TEST_IMAGES_SIZE])
    network.train(flat_data)
    # network.print_weights()
    network.write_weights(WEIGHTS_PATH)
    network.write_weights(WEIGHTS_HEX_PATH, True)

    # repair broken image
    for number, broken_image_path in enumerate(BROKEN_IMAGE_PATHS):
        broken_data = read_image(broken_image_path)
        broken_data = rgb_to_bin(broken_data)
        broken_data = broken_data.ravel()
        repaired_data = network.repair(broken_data)
        print(network.iteration)
        repaired_data_to_save = numpy.reshape(repaired_data, (network.shape[1], network.shape[0]))

        pyplot.imsave(f"../data/{TEST_IMAGES_SIZE}/repaired_{number}.bmp", repaired_data_to_save, cmap = COLOR_MAP)
