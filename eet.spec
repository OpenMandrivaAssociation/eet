%define name	eet
%define version 1.1.0
%define release %mkrel 2

%define major 	1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Eet library
Name: 		%name
Version: 	%version
Release: 	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source:		http://download.enlightenment.org/snapshots/LATEST/%name-%version.tar.bz2
BuildRoot: 	%_tmppath/%name-buildroot
URL: 		http://www.enlightenment.org/
BuildRequires: 	jpeg-devel zlib-devel

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
%setup -q 

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%_bindir/%name

%files -n %libname
%defattr(-,root,root) 
%_libdir/libeet.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/*.a
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/Eet*
