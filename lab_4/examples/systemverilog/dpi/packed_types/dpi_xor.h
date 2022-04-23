/* MTI_DPI */

/*
 * Copyright 2002-2016 Mentor Graphics Corporation.
 *
 * Note:
 *   This file is automatically generated.
 *   Please do not edit this file - you will lose your edits.
 *
 * Settings when this file was generated:
 *   PLATFORM = 'win32pe'
 */
#ifndef INCLUDED_DPI_XOR
#define INCLUDED_DPI_XOR

#ifdef __cplusplus
#define DPI_LINK_DECL  extern "C" 
#else
#define DPI_LINK_DECL 
#endif

#include "svdpi.h"



DPI_LINK_DECL DPI_DLLESPEC
void
xor_bitvec64(
    svBitVecVal* z,
    const svBitVecVal* i0,
    const svBitVecVal* i1);

DPI_LINK_DECL DPI_DLLESPEC
void
xor_logicvec64(
    svLogicVecVal* z,
    const svLogicVecVal* i0,
    const svLogicVecVal* i1);

DPI_LINK_DECL DPI_DLLESPEC
void
xor_longint(
    uint64_t* z,
    uint64_t i0,
    uint64_t i1);

#endif 