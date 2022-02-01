from neuron import Neuron
import numpy
import copy


class Network:

    def __init__(self, neuron_number, shape = (5, 7)):
        # x = 5, y = 7
        # w = 5, h = 7
        self.shape = shape
        self.standard_data = None
        self.iteration = None
        self.neurons_number = self.shape[0] * self.shape[1]
        self.neurons = [Neuron(number) for number in range(neuron_number)]
        for neuron in self.neurons:
            other_neurons = copy.copy(self.neurons)
            other_neurons.remove(neuron)
            neuron.weights = dict(zip(other_neurons, [0 for _ in range(neuron_number)]))

    # standard_data - list of '1' and '-1'
    def train(self, standard_data):
        self.standard_data = standard_data.tolist()
        for neuron_i in self.neurons:
            for neuron_j in neuron_i.weights.keys():
                neuron_i.weights[neuron_j] = self.standard_data[neuron_i.number] * self.standard_data[neuron_j.number]

    def get_weights(self, list_shape = False):
        weights_list = [0 for _ in range(self.neurons_number**2)]
        weights_table = numpy.reshape(weights_list, (len(self.neurons), len(self.neurons)))
        for neuron_i in self.neurons:
            for neuron_j in neuron_i.weights.keys():
                weights_table[neuron_i.number].__setitem__(neuron_j.number, neuron_i.weights[neuron_j])
        if list_shape:
            weights = numpy.reshape(self.get_weights(), (1, self.neurons_number**2))[0]
        else:
            weights = weights_table
        return weights

    def print_weights(self):
        for row in self.get_weights():
            for weight in row:
                if weight >= 0:
                    print(' ', end = "")
                print(weight, end = "\t")
            print()

    def write_weights(self, path, hex_format = False):
        with open(path, 'w') as file:
            for weight in self.get_weights(True):
                if hex_format:
                    file.write(int(weight).to_bytes(2, "big", signed = True).hex().upper())
                else:
                    file.write(str(int(weight).to_bytes(2, "big", signed = True)))

    def repair(self, data, print_outputs_by_iterations = False, print_outputs_by_neurons = False):
        if print_outputs_by_iterations or print_outputs_by_neurons:
            print()
        for neuron, input_data in zip(self.neurons, data.tolist()):
            neuron.output = input_data
        self.iteration = 0
        old_outputs = self.standard_data
        outputs = data.tolist()
        while (old_outputs != outputs) and (self.iteration < 1000):
            self.iteration += 1
            for neuron in self.neurons:
                if print_outputs_by_neurons:
                    print(f"{neuron}: {[i.output for i in self.neurons]}")
                other_neurons = copy.copy(self.neurons)
                other_neurons.remove(neuron)
                # other_outputs = [other_neuron.output for other_neuron in other_neurons]
                neuron.compute(other_neurons)
            old_outputs = outputs
            outputs = [neuron.output for neuron in self.neurons]
            if print_outputs_by_iterations:
                print(f"iteration {self.iteration}: {outputs}")
        return outputs


if __name__ == "__main__":
    network = Network(6, (2, 3))
    network.print_weights()
