vlib work

vlog test.sv -dpiheader dpi_types.h foreign.c
REM - it is a comment-like
REM vopt +acc test -o opt_test
REM vsim -i opt_test -do "add wave light; view source"
vsim -i test -do "add wave light; view source"
