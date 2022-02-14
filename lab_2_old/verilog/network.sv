

module Network
#(
    // изображение 128*64
    // 8192 - количество нейронов по умолчанию
    parameter NEURONS_NUMBER = 8192
)
(
    input [7:0] broken_data [NEURONS_NUMBER: 0],
    input [7:0] weights [NEURONS_NUMBER: 0],
    input clock,
    
    output [NEURONS_NUMBER: 0] out
);

    wire [7: 0] other_weights [NEURONS_NUMBER - 2: 0];
    wire [7: 0] other_neurons [NEURONS_NUMBER - 2: 0];

    genvar neuron_number;
    generate
        for(neuron_number = 0; neuron_number < NEURONS_NUMBER; neuron_number = neuron_number + 1)
        begin : neurons_generation
            if (neuron_number < NEURONS_NUMBER - 1)
            begin
                assign other_weights[NEURONS_NUMBER - 2: neuron_number] = weights[NEURONS_NUMBER - 1: neuron_number + 1];
                assign other_neurons[NEURONS_NUMBER - 2: neuron_number] = out[NEURONS_NUMBER - 1: neuron_number + 1];
            end
            if (neuron_number > 0)
            begin
                assign other_weights[neuron_number - 1: 0] = weights[neuron_number - 1: 0];
                assign other_neurons[neuron_number - 1: 0] = out[neuron_number - 1: 0];
            end
            
            Neuron #(.OTHER_NEURONS_NUMBER(NEURONS_NUMBER - 1))
            neuron
            (
                .other_weights(0),
                .other_neurons(0),
                .clock(clock),
                .out(out[neuron_number])
            );
        end
    endgenerate

endmodule