#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/eet eet; \
#cd eet; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf eet-$PKG_VERSION.tar.xz eet/ --exclude .svn --exclude .*ignore

%define snapshot 0
%if %{snapshot}
%define	svndate	20120103
%define	svnrev	66634
%endif

%define	major	1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Eet library
Name:		eet
%if %{snapshot}
Version:	1.5.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.6.1
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
%if %{snapshot}
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif
URL:		http://www.enlightenment.org/
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(eina) >= 1.0.0
BuildRequires:	pkgconfig(gnutls) >= 1.7.6
BuildRequires:	pkgconfig(zlib)

%description
Eet is a tiny library designed to write an arbitary set of chunks of data
to a file and optionally compress each chunk (very much like a zip file)
and allow fast random-access reading of the file later on. It does not
do zip as a zip itself has more complexity than is needed, and it was much
simpler to impliment this once here.

This package is part of the E17 desktop shell.

%package -n %{libname}
Summary:	Eet library
Group:		System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Eet headers, libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from eet

%prep
%if %{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

%build

%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static

%make

%install
rm -fr %{buildroot}
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/libeet.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%{_includedir}/eet*

