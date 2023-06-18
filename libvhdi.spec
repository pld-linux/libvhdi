#
# Conditional build:
%bcond_without	python	# Python bindings (any)
%bcond_without	python2	# CPython 2.x bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20220115
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfguid_ver		20120426
%define		libuna_ver		20210801
Summary:	Library to access the Virtual Hard Disk image format
Summary(pl.UTF-8):	Biblioteka dostępu do formatu obrazów Virtual Hard Disk
Name:		libvhdi
Version:	20221124
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libvhdi/releases
Source0:	https://github.com/libyal/libvhdi/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	1d45d0b78dcf2244758e05d694990d45
URL:		https://github.com/libyal/libvhdi/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfguid-devel >= %{libfguid_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
%{?with_python2:BuildRequires:	python-devel >= 1:2.5}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
Requires:	libfdata >= %{libfdata_ver}
Requires:	libfguid >= %{libfguid_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvhdi is a library to access the Virtual Hard Disk image format.

Read supported formats:
- Virtual Hard Disk version 1 (VHD)
- Virtual Hard Disk version 2 (VHDX)

Supported image types:
- Fixed-size hard disk image
- Dynamic-size (or sparse) hard disk image
- Differential (or differencing) hard disk image
  - Note that an undo disk image (.vud) is also a differential image

%description -l pl.UTF-8
libvhdi to biblioteka służąca do dostępu do formatu obrazów Virtual
Hard Disk.

Obsługuje odczyt formatów:
- Virtual Hard Disk w wersji 1 (VHD)
- Virtual Hard Disk w wersji 2 (VHDX)

Obsługiwane typy obrazów:
- obrazy dysków o stałym rozmiarze
- obrazy dysków o rozmiarze dynamicznym (lub rzadkie)
- różnicowe obrazy dysków
  - uwaga: obraz dysku undo (.vud) to także obraz różnicowy

%package devel
Summary:	Header files for libvhdi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvhdi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}
Requires:	libfdata-devel >= %{libfdata_ver}
Requires:	libfguid-devel >= %{libfguid_ver}
Requires:	libuna-devel >= %{libuna_ver}

%description devel
Header files for libvhdi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvhdi.

%package static
Summary:	Static libvhdi library
Summary(pl.UTF-8):	Statyczna biblioteka libvhdi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvhdi library.

%description static -l pl.UTF-8
Statyczna biblioteka libvhdi.

%package tools
Summary:	Tools to support the Expert Witness Compression Format
Summary(pl.UTF-8):	Narzędzia obsługujące format Expert Witness Compression Format
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	libfuse >= 2.6

%description tools
Tools to support the Expert Witness Compression Format.

%description tools -l pl.UTF-8
Narzędzia obsługujące format Expert Witness Compression Format.

%package -n python-pyvhdi
Summary:	Python 2 bindings for libvhdi library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libvhdi
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pyvhdi
Python 2 bindings for libvhdi library.

%description -n python-pyvhdi -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libvhdi.

%package -n python3-pyvhdi
Summary:	Python 3 bindings for libvhdi library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libvhdi
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pyvhdi
Python 3 bindings for libvhdi library.

%description -n python3-pyvhdi -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libvhdi.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python2:--enable-python2} \
	%{?with_python3:--enable-python3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvhdi.la

%if %{with python2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyvhdi.{la,a}
%endif
%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pyvhdi.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libvhdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvhdi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvhdi.so
%{_includedir}/libvhdi
%{_includedir}/libvhdi.h
%{_pkgconfigdir}/libvhdi.pc
%{_mandir}/man3/libvhdi.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libvhdi.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vhdiinfo
%attr(755,root,root) %{_bindir}/vhdimount
%{_mandir}/man1/vhdiinfo.1*

%if %{with python2}
%files -n python-pyvhdi
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyvhdi.so
%endif

%if %{with python3}
%files -n python3-pyvhdi
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pyvhdi.so
%endif
