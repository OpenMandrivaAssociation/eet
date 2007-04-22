%define name	eet
%define version 0.9.10.025
%define release %mkrel 0.%{cvsrel}.2

%define cvsrel 20060323

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Eet library
Name: 		%name
Version: 	%version
Release: 	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source: 	%name-%{cvsrel}.tar.bz2
BuildRoot: 	%_tmppath/%name-buildroot
URL: 		http://www.get-e.org/
BuildRequires: 	jpeg-devel zlib-devel
BuildRequires:	multiarch-utils

%description
Eet is a tiny library designed to write an arbitary set of chunks of data
to a file and optionally compress each chunk (very much like a zip file)
and allow fast random-access reading of the file later on. It does not
do zip as a zip itself has more complexity than is needed, and it was much
simpler to impliment this once here.

This package is part of the E17 desktop shell.

%package -n %libname
Summary: Eet library
Group: System/Libraries

%description -n %libname
This package contains the dynamic libraries from %name.

%package -n %libnamedev
Summary: Eet headers, static libraries, documentation and test programs
Group: Development/Other
Requires: %{libname} = %{version}
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libnamedev
Headers and static libraries from eet

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%_bindir/eet
%_bindir/eet_bench

%files -n %libname
%defattr(-,root,root) 
%_libdir/libeet.so.*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/*.a
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_bindir/eet-config
%multiarch %{multiarch_bindir}/eet-config
%_includedir/Eet*
