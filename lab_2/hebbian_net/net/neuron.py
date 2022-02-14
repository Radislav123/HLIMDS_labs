from .consts import VECTOR, HIGH_LEVEL, LOW_LEVEL


def as_hex(num):
    # if num < -128:
    if num < -32768:
        raise Exception('Too small')
    # if num > 127:
    if num > 32767:
        raise Exception('Too large')
    if num < 0:
        # num = 256 + num
        num = 65536 + num
    raw = hex(num)[2:]
    if len(raw) == 1:
        raw = '000' + raw
    return raw


VERILOG_TEMPLATE = '''
module neuron
(
    input [{SIZE}:0] x,
    input [{WEIGHTS_SIZE}:0] weights,
    output predict
);
    wire [{NUM_SIZE}:0] bias = weights[{NUM_SIZE}:0];
    wire [{NUM_SIZE}:0] w [{SIZE}:0];
{WEIGHTS_MAP}
    
{LIST_SUM}


endmodule
'''


class Neuron:
    def __init__(self, size: int):
        self.size = size
        self.w = [0] * size
        # смещение
        self.bias = 0

    def forward(self, vector: VECTOR) -> int:
        assert len(vector) == self.size, 'Unsupported vector shape'
        s = self.bias
        for w, x in zip(self.w, vector):
            s += w * x
            if s > 32767 or s < -32768:
                print('Overflow')
        return HIGH_LEVEL if s > 0 else LOW_LEVEL

    def update_w(self, vector: VECTOR, target: int):
        assert len(vector) == self.size, 'Unsupported vector shape'
        self.bias += 1 if target else -1
        for i, x in enumerate(vector):
            self.w[i] += x * (1 if target else -1)

    def dump_verilog(self, x_data):
        num_size = 16
        weights_size = (self.size + 1) * num_size

        weights_map = []
        for i in range(self.size):
            weights_map.append('    assign w[{}] = weights[{}:{}];'.format(
                i, (i + 2) * num_size - 1, (i + 1) * num_size))
        weights_map = '\n'.join(weights_map)

        list_sum = ['bias']
        for i in range(self.size):
            list_sum.append("(x[{}] ? w[{}] : {}'h00)".format(i, i, num_size))
        list_draw = []
        while len(list_sum) > 1:
            a = list_sum.pop(0)
            b = list_sum.pop(0)
            name = 'predict_{:03d}'.format(len(list_draw))
            text = '    wire [{}:0] {} = {} + {};'.format(num_size - 1, name, a, b)
            list_sum.append(name)
            list_draw.append(text)
        it = '    assign predict = {}[{}] == 0;'.format(list_sum[-1], num_size - 1)
        list_draw.append(it)
        list_draw = '\n'.join(list_draw)

        weights_init = ''.join([as_hex(x) for x in [self.bias] + self.w][::-1])

        code = VERILOG_TEMPLATE.format(
            SIZE=self.size - 1, NUM_SIZE=num_size - 1, WEIGHTS_SIZE=weights_size - 1,
            LIST_SUM=list_draw, WEIGHTS_MAP=weights_map)
        # return weights_init, code
        x_data_hex = ''
        for count, x in enumerate(x_data):
            if count > 0:
                x_data_hex += '\n'
            x_data_hex += ''.join(str(i) for i in x)[::-1]
        return weights_init, x_data_hex


__all__ = ['Neuron']
