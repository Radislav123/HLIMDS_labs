--
-- Copyright 1991-2015 Mentor Graphics Corporation
--
-- All Rights Reserved.
--
-- THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
-- WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
-- OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
--

-- Filename    : ringbuf.vhd
--
-- Description : Top Level

library ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;

ENTITY ringbuf IS
    generic (
        counter_size : integer;
        buffer_size : integer);
    PORT (
        clock     : IN std_logic;
        reset     : IN std_logic;
        txda      : INOUT std_logic;
        rxda      : INOUT std_logic;
        txc       : OUT std_logic;
        outstrobe : OUT std_logic;
        buffers   : INOUT std_logic_vector(15 DOWNTO 0)
    );

END ringbuf;

ARCHITECTURE RTL OF ringbuf IS

COMPONENT store
    GENERIC (
        counter_size : integer := 4;
        buffer_size : integer := 16
    );
    PORT (
        clock     : IN std_logic;
        reset     : IN std_logic;
        oeenable : IN std_logic;
        txda     : INOUT std_logic;
        ramadrs  : IN std_logic_vector((counter_size *2) DOWNTO 0);
        buffers  : OUT std_logic_vector((buffer_size-1) DOWNTO 0)
    );
END component;

component control
    GENERIC (
        counter_size : integer := 4
    );
    PORT (
        clock     : IN std_logic;
        reset     : IN std_logic;
        ramadrs   : OUT std_logic_vector((counter_size * 2) DOWNTO 0);
        oeenable  : OUT std_logic;
        outstrobe : OUT std_logic;
        txc       : OUT std_logic
   );
END component;

component retrieve
    GENERIC (
        counter_size : integer := 4;
        buffer_size : integer := 16
    );
    PORT (
        outstrobe : IN std_logic;
        ramadrs   : IN std_logic_vector((counter_size * 2) DOWNTO 0);
        buffers   : IN std_logic_vector((buffer_size -1) DOWNTO 0);
        rxda      : INOUT std_logic
    );
END component;

signal ramadrs       : std_logic_vector((counter_size * 2) DOWNTO 0);
signal oeenable      : std_logic;
signal outstrobe_int : std_logic;

BEGIN

    block1_INST: store
        GENERIC MAP(
            counter_size => counter_size,
            buffer_size  => buffer_size
        )
        PORT MAP (
            clock    => clock,
            reset    => reset,
            oeenable => oeenable,
            txda     => txda,
            ramadrs  => ramadrs,
            buffers  => buffers
        );

    block2_INST: control
        GENERIC MAP (
            counter_size => counter_size
        )
        PORT MAP (
            clock     => clock,
            reset     => reset,
            ramadrs   => ramadrs,
            oeenable  => oeenable,
            outstrobe => outstrobe_int,
            txc => txc
        );

    block3_INST: retrieve
        GENERIC MAP (
            counter_size => counter_size,
            buffer_size  => buffer_size
        )
        PORT MAP (
            outstrobe => outstrobe_int,
            ramadrs   => ramadrs,
            buffers   => buffers,
            rxda      => rxda
        );

    outstrobe <= outstrobe_int;

END RTL;
