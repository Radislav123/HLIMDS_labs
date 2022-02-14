module neuron
(
    input [15:0] x,
    input [271:0] weights,
    output predict
);
    wire [15:0] bias = weights[15:0];
    wire [15:0] w [15:0];
    integer sum;

    genvar i;
    generate
        for (i = 0; i < 16; i = i + 1) begin: weights_assignment
            assign w[i] = weights[16*(i + 2) - 1: 16*(i + 1)];
        end
    endgenerate
    
    
    always @(x) begin
        integer i;
        // вес смещения всегда 1, поэтому без умножения
        sum = bias;
        for (i = 0; i < 16; i = i + 1) begin
            sum = sum + w[i]*x[i];
        end
    end
    
    
    assign predict = sum == 0;
    
    // для проверки корректности назначений
    initial begin
        integer i;
        for (i = 0; i < 16; i = i + 1) begin
            $display("[%d] = [%d: %d]", i, 16*(i + 2) - 1, 16*(i + 1));
        end
    end


endmodule
