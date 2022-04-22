# Copyright 1991-2015 Mentor Graphics Corporation
#
# All Rights Reserved.
#
# THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
# WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
# OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.

# Use this run.do file to run this example.
# Either bring up ModelSim and type the following at the "ModelSim>" prompt:
#     do run.do
# or, to run from a shell, type the following at the shell prompt:
#     vsim -sc22 -do run.do -c
# (omit the "-c" to see the GUI while running from the shell)

onbreak {resume}

# create library
if [file exists work] {
    vdel -all
}
vlib work

# compile and link C source files
sccom -sc22 -g -scv main.cpp
sccom -sc22 -link -scv

# open debugging windows
quietly view *

# start and run simulation
vsim -sc22 top
run 2500

# view the results
if {![batch_mode]} {
    quietly add wave -expand top/tr/pipelined_stream
    quietly add wave -expand top/tr/addr_stream
    quietly add wave -expand top/tr/data_stream
    quietly wave zoomrange 0 120
}
