%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Eet library
Name:		eet
Version:	1.7.6
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(eina) >= 1.0.0
BuildRequires:	pkgconfig(gnutls) >= 1.7.6
# note: pkgconfig(libgcrypt) is for 2013.0+, for Rosa 2012.1 should be libgcrypt-devel
BuildRequires:	pkgconfig(libgcrypt)
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

%package -n %{devname}
Summary:	Eet headers, libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and libraries from eet

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/libeet.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%{_includedir}/eet*
