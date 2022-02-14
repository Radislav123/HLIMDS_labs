

module Neuron
#(
    // изображение 128*64
    // 8192 - количество нейронов по умолчанию
    parameter OTHER_NEURONS_NUMBER = 8191
)
(
    input [7:0] other_weights [OTHER_NEURONS_NUMBER: 0],
    input [7:0] other_neurons [OTHER_NEURONS_NUMBER: 0],
    input clock,

    output out
);
    /*
    always @(posedge clock)
    begin
        wire count = 0;
        wire activation_value = 0;
        
        repeat (OTHER_NEURONS_NUMBER)
        begin
            activation_value = activation_value + other_neurons[count]*other_weights[count];
        end
        
        if (activation_value < 0) out = -1; else out = 1;
    end
    */

endmodule