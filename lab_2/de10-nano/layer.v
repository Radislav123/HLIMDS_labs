module layer
(
    input [15:0] x,
    // LEDs
    output [3:0] predict
);

    reg [271:0] weights [7:0];
    
    genvar i;
    generate
        for(i = 0; i < 4; i = i + 1) begin: neuron_generating
            neuron neuron(x, weights[i], predict[i]);
        end
    endgenerate
        
    initial begin
        $readmemh ("weights.hex", weights);
    end

endmodule