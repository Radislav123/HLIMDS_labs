module dpi_adder;

parameter L = 40000000;
integer i;
integer accumulate = 0;
integer mcd;

import "DPI-C" function void add(inout int accumulate, input int b);

initial begin
    for (i = 1; i <= L; i++) begin
        add(accumulate, i);
    end
    mcd = $fopen("results.txt") | 1;
    $fdisplay(mcd, "accumulate = %d", accumulate);
    $fclose(mcd);
end

endmodule
