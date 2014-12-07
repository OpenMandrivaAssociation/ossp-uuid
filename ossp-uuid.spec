# needed for rpm53
%bcond_with bootstrap
%bcond_with crosscompile

%if %{with bootstrap}
%bcond_with perl
%bcond_with php
%bcond_with postgresql
%else
%bcond_without perl
%bcond_without php
%bcond_without postgresql
%endif

%define oname	ossp_uuid

Summary:	OSSP uuid is a ISO-C:1999 application programming interface
Name:		ossp-uuid
Version:	1.6.2
Release:	21
License:	GPLv2+
Group:		Development/C
Url:		http://www.ossp.org/pkg/lib/uuid/
Source0:	ftp://ftp.ossp.org/pkg/lib/uuid/uuid-%{version}.tar.gz
Patch0:		uuid-1.6.2-fix-perl-install.patch
Patch1:		uuid-1.6.2-fix-php-install.patch
Patch2:		uuid-1.6.2-fix-php-link.patch
Patch3:		uuid-1.6.2-ossp.patch
Patch4:		uuid-1.6.2-fix-php-test-module-loading.patch
Patch5:		uuid-1.6.2-php-54x.patch
#We don't want anything stripped
#Upstream-Status: Inappropriate [no upstream]
#The project appears to no longer be accepting changes.
Patch6:		uuid-nostrip.patch
Patch7:		uuid-aarch64.patch
%if %{with postgresql}
BuildRequires:	postgresql-devel
%endif
%if %{with perl}
BuildRequires:	perl-devel
%endif
%if %{with php}
BuildRequires:	php-devel
BuildRequires:	php-cli
%endif
%rename		%{oname}

%description
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs

%define	major	16
%define libname %mklibname %{name} %{major}
%define	oldname	%mklibname %{oname} %{major}

%package -n     %{libname}
Summary:	Main library for ossp-uuid
Group:		System/Libraries
%rename		%{oldname}

%description -n %{libname}
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs

%define	libcxx	%mklibname %{name}++ %{major}
%define	oldcxx	%mklibname %{oname}++ %{major}

%package -n     %{libcxx}
Summary:	C++ library for ossp-uuid
Group:		System/Libraries
%rename		%{oldcxx}

%description -n	%{libcxx}
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs

%define	libdce	%mklibname %{name}_dce %{major}
%define	olddce	%mklibname %{oname}_dce %{major}

%package -n     %{libdce}
Summary:	DCE library for ossp-uuid
Group:		System/Libraries
%rename		%{olddce}

%description -n	%{libdce}
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs

%define devname	%mklibname %{name} -d
%define	devold	%mklibname %{oname} -d

%package -n	%{devname}
Summary:	Header files for the ossp-uuid library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libcxx} = %{version}
Requires:	%{libdce} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{devold}

%description -n	%{devname}
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs
These are .h files.

%if %{with perl}
%package -n	perl-OSSP-uuid
Summary:	Perl bindings for ossp-uuid
Group:		Development/Perl

%description -n	perl-OSSP-uuid
This package contains perl bindings for %{name}.
%endif

%if %{with php}
%package -n	php-OSSP-uuid
Summary:	PHP bindings for ossp-uuid
Group:		Development/PHP

%description -n	php-OSSP-uuid
This package contains php bindings for %{name}.
%endif

%if %{with postgresql}
%package -n	postgresql-OSSP-uuid
Summary:	Postgresql library for ossp-uuid
Group:		System/Libraries
%rename		%{libname}-pgsql

%description -n	postgresql-OSSP-uuid
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation of
DCE 1.1, ISO/IEC 11578:1996 and IETF RFC-4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs
%endif

%prep
%setup -qn uuid-%{version}
%apply_patches

%build
export PHP_ACLOCAL=aclocal
%if %{with crosscompile}
export ac_cv_va_copy=yes
export ac_cv_func_clock_gettime=yes
export ac_cv_func_getifaddrs=yes
export ac_cv_func_gettimeofday=yes
%endif

%configure \
	--includedir=%{_includedir}/ossp-uuid \
%if %{with postgresql}
	--with-pgsql \
%endif
%if %{with perl}
	--with-perl \
%endif
%if %{with php}
	--with-php \
%endif
	--with-cxx \
	--with-dce \
	--disable-static
%make

%check
make check

%install
%makeinstall_std PHP_EXTENSIONDIR=%{_libdir}/php/extensions
%if %{with postgresql}
mkdir -p %{buildroot}/%{_libdir}/postgresql/
mkdir -p %{buildroot}/%{_datadir}/postgresql/
%makeinstall_std -C pgsql 
ln -s ossp-uuid.so %{buildroot}%{_libdir}/postgresql/uuid.so 
ln -s uuid.sql %{buildroot}%{_datadir}/postgresql/ossp-uuid.sql
%endif

mkdir %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libossp-uuid.so.%{major}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libossp-uuid.so.%{major}.*.* %{buildroot}%{_libdir}/libossp-uuid.so

%files
%doc OVERVIEW
%{_bindir}/uuid
%{_mandir}/man1/uuid.1*

%files -n %{libname}
/%{_lib}/libossp-uuid.so.%{major}*

%files -n %{libcxx}
%{_libdir}/libossp-uuid++.so.%{major}*

%files -n %{libdce}
%{_libdir}/libossp-uuid_dce.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/ossp-uuid.pc
%dir %{_includedir}/ossp-uuid
%{_includedir}/ossp-uuid/uuid.h
%{_includedir}/ossp-uuid/uuid++.hh
%{_includedir}/ossp-uuid/uuid_dce.h
%{_bindir}/uuid-config
%{_libdir}/libossp-uuid.so
%{_libdir}/libossp-uuid++.so
%{_libdir}/libossp-uuid_dce.so
%{_mandir}/man1/uuid-config.1*
%{_mandir}/man3/ossp-uuid.3*
%{_mandir}/man3/ossp-uuid++.3*

%if %{with perl}
%files -n perl-OSSP-uuid
%{perl_vendorarch}/OSSP
%{perl_vendorarch}/auto/OSSP
%{_mandir}/man3/OSSP::uuid.3*
%endif

%if %{with php}
%files -n php-OSSP-uuid
%{_libdir}/php/extensions/ossp-uuid.so
%{_libdir}/php/extensions/uuid.php
%endif

%if %{with postgresql}
%files -n postgresql-OSSP-uuid
%{_libdir}/postgresql/uuid.so
%{_libdir}/postgresql/ossp-uuid.so
%{_datadir}/postgresql/uuid.sql
%{_datadir}/postgresql/ossp-uuid.sql
%endif
