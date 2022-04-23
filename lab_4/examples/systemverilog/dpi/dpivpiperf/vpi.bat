vlib work

REM vlog vpi_adder.v -dpiheader vpi_adder.h vpi_adder.c -sv
REM vsim -i vpi_adder -do "add wave *; view source"

vlog vpi_adder vpi_adder.c -c
vsim -i vpi_adder -do "add wave *; view source"