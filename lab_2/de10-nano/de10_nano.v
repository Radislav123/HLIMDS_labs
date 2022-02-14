
module de10_nano
(
    input   [1:0]  KEY,
    input   [1:0]  SW,
    output  [3:0]  LED
);

    reg [3:0] data [15:0];
    wire [15:0] input_data;
    
    layer layer (input_data, LED[3:0]);
    
    
    always @(SW) begin
        assign input_data = data[SW];
    end
    
    initial begin
        $readmemb ("data.bin", data);
    end

endmodule
