%define name	eet
%define version 0.9.10.038
%define release %mkrel 1

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Eet library
Name: 		%name
Version: 	%version
Release: 	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
Source: 	%name-%version.tar.bz2
BuildRoot: 	%_tmppath/%name-buildroot
URL: 		http://www.get-e.org/
BuildRequires: 	jpeg-devel zlib-devel
#BuildRequires:	multiarch-utils

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
Obsoletes: eet < 0.9.10.037
Provides: eet = %{version}-%{release}

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
mkdir %buildroot/%_bindir/
touch %buildroot/%_bindir/%name-config
#%multiarch_binaries %buildroot/%_bindir/%name-config
#rm %buildroot/%_bindir/%name-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root) 
%doc AUTHORS COPYING README
%_libdir/libeet.so.*
%_bindir/%name-config
%_bindir/eet-config
%multiarch %{multiarch_bindir}/eet-config

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/*.a
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/Eet*


%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.9.10.038-1mdv2008.0
- snapshot 20070516

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.10.037-2mdv2008.0
+ Revision: 17095
- Add obsoletes so that people don't keep the old binaries

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.10.037-1mdv2008.0
+ Revision: 17082
- New snapshot
- Removed main binary package as there are no longer /usr/bin/{eet,eet_bench}
- Import eet



* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 0.9.10.025-0.20060323.2mdv2007.0
- rebuild

* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.9.10.025-0.20060323.1mdk
- new cvs checkout

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.9.10.023-0.20060216.1mdk
- new cvs checkout

* Tue Jan 17 2006 Austin Acton <austin@mandriva.org> 0.9.10.023-0.20060117.1mdk
- new cvs checkout

* Thu Jan 12 2006 Austin Acton <austin@mandriva.org> 0.9.10.022-0.20060111.1mdk
- new cvs checkout

* Thu Nov 24 2005 Austin Acton <austin@mandriva.org> 0.9.10.019-0.20051124.1mdk
- new cvs checkout

* Sat Nov 12 2005 Austin Acton <austin@mandriva.org> 0.9.10.019-0.20051112.1mdk
- new cvs checkout

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.9.10.018-0.20051109.1mdk
- new cvs checkout

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 0.9.10.018-0.20051104.1mdk
- new cvs checkout

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.9.10.013-0.20050904.1mdk
- new cvs checkout

* Sat Aug 13 2005 Austin Acton <austin@mandriva.org> 0.9.10.013-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.9.10.010-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.9.10.008-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.9.10.007-0.20050524.2mdk
- clean spec
- multiarch binaries

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.9.10.007-0.20050524.1mdk
- new cvs checkout

* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.9-0.20040913.1mdk
- 0.9.9 20040913

* Wed Jul 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.2-3.20030730.1mdk
- 20030730

* Thu Jun 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.2-3.20030624.1mdk
- update to 20030624 CVS

* Thu Apr 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.1-2mdk
- provides & obsoletes

* Thu Apr 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.1-1mdk
- use macro
- use mklibname
- libification
- fix filelist
- clean spec
- uploaded by <tfernagut@wanadoo.be>

* Sat Jun 23 2001 The Rasterman <raster@rasterman.com>
- Created spec file
