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
#ifndef INCLUDED_DPIHEADER
#define INCLUDED_DPIHEADER

#ifdef __cplusplus
#define DPI_LINK_DECL  extern "C" 
#else
#define DPI_LINK_DECL 
#endif

#include "svdpi.h"



#ifndef MTI_INCLUDED_TYPEDEF_MyType
#define MTI_INCLUDED_TYPEDEF_MyType

typedef struct {
    svBitVecVal x[SV_PACKED_DATA_NELEMS(12)];
    svLogicVecVal y[SV_PACKED_DATA_NELEMS(12)];
}  MyType;

#endif

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bit_2D_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bit_3D_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bit_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_2D_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_2D_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_3D_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_3D_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_bitvec_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logic_2D_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logic_3D_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logic_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_2D_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_2D_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_3D_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_3D_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_oarr_by_elemptr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_logicvec_oarr_by_elemval(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_struct_oarr(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_struct_oarr_memcpy(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

DPI_LINK_DECL DPI_DLLESPEC
void
clone_struct_oarr_safe(
    const svOpenArrayHandle i,
    const svOpenArrayHandle o);

#endif 
