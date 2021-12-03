class Neuron:

    def __init__(self, number):
        # {link_from_another_neuron: weight_of_link}
        self.weights = None
        # from data == neuron input
        self.input = None
        # self.output can be '+1' or '-1'
        self.output = None
        self.number = number

    def set_weights(self, weights):
        self.weights = weights

    # step function
    def compute(self, other_outputs):
        self.output = -1 if sum([other_outputs[i] * self.weights[i] for i in range(len(other_outputs))]) < 0 else 1
        return self.output

    def __repr__(self):
        return f"neuron {self.number}"


if __name__ == "__main__":
    pass
