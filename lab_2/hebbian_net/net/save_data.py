from .models import Model
import os


def save_data(model: Model, root: str):
    weights = []
    x_data = None
    for n in model.net.neurons:
        w, x_data = n.dump_verilog(model.x)
        weights.append(w)
    weights = '\n'.join(weights)

    weights_filename = 'weights.hex'
    data_filename = 'data.bin'

    with open(os.path.join(root, weights_filename), 'w') as f:
        f.write(weights)
    with open(os.path.join(root, data_filename), 'w') as f:
        f.write(x_data)
