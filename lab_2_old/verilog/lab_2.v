

module lab_2
(
    input CLOCK_50
);

    // изображение 128*64
    // 8192 - количество нейронов по умолчанию
    localparam NEURONS_NUMBER = 35;
    wire [NEURONS_NUMBER:0] network_out;

    Network #(.NEURONS_NUMBER(NEURONS_NUMBER))
    network
    (
        //.broken_data(0),
        //.weights(0),
        .clock(CLOCK_50),
        .out(network_out)
    );

endmodule
