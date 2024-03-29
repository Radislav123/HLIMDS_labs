// Copyright 1991-2015 Mentor Graphics Corporation

// All Rights Reserved.

// THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
// WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
// OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.

#ifndef INCLUDED_RETRIEVE
#define INCLUDED_RETRIEVE

#include <systemc.h>

SC_MODULE(retrieve)
{
public:
    // Ports
    sc_in<sc_logic>        outstrobe;
    sc_in<sc_lv<9> >       ramadrs;
    sc_in<sc_lv<16> >      buffer;
    sc_out<sc_logic>       rxda;

    // Internal Signals
    sc_signal<sc_logic>    rd0a;

    // Methods
    void retriever();
    void rxda_driver();

    SC_CTOR(retrieve)
      : outstrobe("outstrobe"),
        ramadrs("ramadrs"),
        buffer("buffer"),
        rxda("rxda"),
        rd0a("rd0a")
    {
        SC_METHOD(retriever);
        sensitive << buffer << ramadrs;
        dont_initialize();

        SC_METHOD(rxda_driver);
        sensitive << rd0a << outstrobe;
        dont_initialize();
    }

    // Destructor does nothing
    ~retrieve()
    {
    }
};


//
// This method assigns temporary signal rd0a to the
// properly selected bit in the buffer.
//
inline void retrieve::retriever()
{
    int i = ramadrs.read().range(3, 0).get_word(0);
    rd0a.write(buffer.read()[i]);
}


//
// This method drives the rxda signal
//
inline void retrieve::rxda_driver()
{
    rxda.write(rd0a.read() & outstrobe.read());
}

#endif
