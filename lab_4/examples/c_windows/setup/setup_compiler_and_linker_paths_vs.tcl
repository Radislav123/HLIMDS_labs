quietly set platform [file tail $env(MODEL_TECH)]
# Check if 64-bit executables are being run.
if {[string match "*64 vsim*" [vsim -version]]} {
	quietly set is64bit 1
} else {
	quietly set is64bit 0
}

quietly set reg_keys [registry keys "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft"]
if {$is64bit == 1 } {
	quietly set VCEDITION "VisualStudio"
} else {
	foreach key $reg_keys {
		if { [string match -nocase "VCExpress" $key] } {
			quietly set VCEDITION "VCExpress"	
			break
		} else {
			quietly set VCEDITION "VisualStudio"
		}
	}
}
		
if {$is64bit == 1 } {
	quietly set regpath "HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\$VCEDITION\\9.0\\Setup\\VC"
} else {
	quietly set regpath "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\$VCEDITION\\9.0\\Setup\\VC"
}
quietly set TOOLPATH [registry get $regpath "ProductDir"]
quietly set TOOLPATHINCLUDE [file join $TOOLPATH include ]
if {$is64bit == 1 } {
	quietly set TOOLPATHBIN [file join $TOOLPATH bin amd64]
	quietly set TOOLPATHLIB [file join $TOOLPATH lib amd64]
} else {
	quietly set TOOLPATHBIN [file join $TOOLPATH bin]
	quietly set TOOLPATHLIB [file join $TOOLPATH lib]
}
quietly set exe_path [file join $TOOLPATHBIN cl.exe]
quietly set cl_exists [file exists $exe_path]

if {$cl_exists != 1 } {
	echo "ERROR: Couldn't find $exe_path. Please install Visual Studio 9.0."
} else {
	quietly set env(PATH) "$TOOLPATHBIN;$TOOLPATH;$::env(PATH)"
}

if {$is64bit == 0 } {
	quietly set regpath "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\$VCEDITION\\9.0"
	quietly set MSPDB80 [file normalize [registry get $regpath "InstallDir" ]]
	quietly set mspdb80_dll_path [file join $MSPDB80 mspdb80.dll]
	quietly set mspdb80_dll_exists [file exists $mspdb80_dll_path]
	if {$mspdb80_dll_exists != 1} {
		echo "ERROR: Couldn't find $MSPDB80/mspdb80.dll. Please install the required mspdb80.dll."
	} else {
		# Add the dll installation directory to teh PATH environment variable.
		quietly set env(PATH) "$MSPDB80;$::env(PATH)"
	}
}

quietly set regpath "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SDKs\\Windows"
quietly set SDKPATH [file normalize [registry get $regpath "CurrentInstallFolder"]]
quietly set SDKPATHINCLUDE [file join $SDKPATH include]
if {$is64bit == 1 } {
	quietly set SDKPATHBIN [file join $SDKPATH bin x64]
	quietly set SDKPATHLIB [file join $SDKPATH lib x64]
} else {
	quietly set SDKPATHBIN [file join $SDKPATH bin]
	quietly set SDKPATHLIB [file join $SDKPATH lib]
}
quietly set mt_exe_path [file join $SDKPATHBIN mt.exe]
quietly set mt_exe_exists [file exists $mt_exe_path]
if {$mt_exe_exists != 1} {
    echo "ERROR: Couldn't find $mt_exe_path. Please install the required SDK."
} else {
	quietly set env(PATH) "$SDKPATHBIN;$::env(PATH)"
}

quietly set env(INCLUDE) "$TOOLPATHINCLUDE;$SDKPATHINCLUDE"
quietly set env(LIB) "$TOOLPATHLIB;$SDKPATHLIB"

# Setup - Set path to the C compiler and linker.
quietly set CC "cl -c -Ox -Oy -I$INSTALL_HOME/include"
quietly set LD "link /DLL $INSTALL_HOME/$platform/mtipli.lib"
quietly set UCDB_LD "link /NODEFAULTLIB:libcmt.lib"
quietly set UCDBLIB " -DEFAULTLIB:$INSTALL_HOME/$platform/ucdb.lib"
quietly set UCDBLIB_STATIC " $INSTALL_HOME/$platform/libucdb.lib"
