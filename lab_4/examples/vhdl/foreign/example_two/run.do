#
# Copyright 1991-2015 Mentor Graphics Corporation
#
# All Rights Reserved.
#
# THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
# WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
# OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
#
# To run this example, bring up the simulator and type the following at the prompt:
#     do run.do
# or, to run from a shell, type the following at the shell prompt:
#     vsim -c -do run.do
# (omit the "-c" to see the GUI while running from the shell)
#

onerror {resume}
# Create the library.
if [file exists work] {
    vdel -all
}
vlib work

# Get the simulator installation directory.
quietly set INSTALL_HOME [file dirname [file normalize $::env(MODEL_TECH)]]

# Set the compiler and linker paths.
if {$tcl_platform(platform) eq "windows"} {
	source $INSTALL_HOME/examples/c_windows/setup/setup_compiler_and_linker_paths_mingwgcc.tcl
} else {
	source $INSTALL_HOME/examples/c_posix/setup/setup_compiler_and_linker_paths_gcc.tcl
}

# Compile the C source(s).
echo $CC dumpdes.c gates.c monitor.c
eval $CC dumpdes.c gates.c monitor.c
echo $LD dumpdes.so dumpdes.o $MTIPLILIB
eval $LD dumpdes.so dumpdes.o $MTIPLILIB
echo $LD monitor.so monitor.o $MTIPLILIB
eval $LD monitor.so monitor.o $MTIPLILIB
echo $LD gates.so gates.o $MTIPLILIB
eval $LD gates.so gates.o $MTIPLILIB

# Compile the VHDL source(s).
vcom foreign.vhd

# Simulate the design.
onerror {resume}
vsim testbench
view structure
view signals
add wave *
run 500

quit -f
