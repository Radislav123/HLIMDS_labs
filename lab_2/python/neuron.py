class Neuron:

    def __init__(self, number):
        # {link_from_another_neuron: weight_of_link}
        # sets in Network.train()
        self.weights = None
        # self.output can be '+1' or '-1'
        # and input rolled into one
        self.output = None
        self.number = number

    # step function
    def compute(self, other_neurons):
        self.output = -1 if \
            sum([other_neuron.output * self.weights[other_neuron] for other_neuron in other_neurons]) < 0 \
            else 1
        return self.output

    def __repr__(self):
        return f"neuron {self.number}"


if __name__ == "__main__":
    pass
