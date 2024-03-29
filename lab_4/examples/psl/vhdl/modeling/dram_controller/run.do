# Copyright 1991-2015 Mentor Graphics Corporation
#
# All Rights Reserved.
#
# THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
# WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
# OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
# To run this example, bring up the simulator and type the following at the prompt:
#     do run.do
# or, to run from a shell, type the following at the shell prompt:
#     vsim -do run.do -c
# (omit the "-c" to see the GUI while running from the shell)
# Remove the "quit -f" command from this file to view the results in the GUI.
#

# Create the library.
if [file exists work] {
    vdel -all
}
vlib work

# Compile the source files.
vcom -93 dram.vhd
vcom -93 dramcon_rtl.vhd -pslfile dram_cntrl.psl
vcom -93 dramcon_sim.vhd -pslfile dram_tb.psl

# Run the first simulation.
vsim tb -nopsl 
onbreak {resume}
run 501800
quit -sim

# Run the second simulation with assertions.
vsim tb 
run 501800

quit -f
