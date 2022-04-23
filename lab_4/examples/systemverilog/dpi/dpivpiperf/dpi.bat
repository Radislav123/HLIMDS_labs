vlib work

REM vlog test.sv -dpiheader dpi_types.h foreign.c
REM vsim -i test -do "add wave light; view source"

vlog dpi_adder.v -dpiheader dpi_adder.h dpi_adder.c -sv
vsim -i dpi_adder -do "add wave *; view source"