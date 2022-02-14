import os
import pathlib

from net.consts import HIGH_LEVEL, LOW_LEVEL
from net.draw import draw_flatten
from net.layers import Dense
from net.models import Model
from net.save_data import save_data


X_s = [
    # пример из методички - https://drive.google.com/file/d/1m6zY5B-IF5lbJcGPvImYcny-8JQaMOBO/view
    # страница 6, внизу
    [
        [1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 0, 1]
    ],
    [
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, ],
    ],
    [
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, ],
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, ],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, ],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, ],
    ],
    [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, ],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ],
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    ],
    [
        [1, 1, 1, 1, 0, 1, 1, 0, 1, ],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, ],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, ],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, ],
    ],
    [
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, ],
    ],
]
y_s = [
    [[HIGH_LEVEL], [LOW_LEVEL], ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
    [
        [HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL, LOW_LEVEL],
        [LOW_LEVEL, LOW_LEVEL, LOW_LEVEL, HIGH_LEVEL],
    ],
]
data_shapes = [
    [3, 3],
    [4, 4],
    [4, 4],
    [4, 4],
    [4, 4],
    [3, 3],
    [4, 4],
]


if __name__ == '__main__':
    example_number = 6
    X = X_s[example_number]
    y = y_s[example_number]
    # len(y[0]) - количество нейронов
    # len(X[0]) - количество входов каждого нейрона
    model = Model(Dense(len(y[0]), len(X[0])))
    # тренировка
    model.fit(X, y, 1000)
    # распознавание
    y_pred = model.predict(X)
    for y_true, y_expected, row in zip(y, y_pred, X):
        print('Expected: {}, predicted: {}'.format(y_expected, y_true))
        draw_flatten(row, *data_shapes[example_number])
        print()

    for row in X:
        print("x = {}'b{}".format(len(row), ''.join(map(str, row[::-1]))))

    root = pathlib.Path(os.path.join(os.getcwd(), __file__)).parent.parent
    root = os.path.join(root, 'de10-nano')
    save_data(model, root)
