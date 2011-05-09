%if %mdkversion < 201010
%define pgsql 1
%else
%define pgsql 0
%endif

# commandline overrides:
# rpm -ba|--rebuild --with 'xxx'
%{?_with_pgsql: %{expand: %%global pgsql 1}}
%{?_without_pgsql: %{expand: %%global pgsql 0}}

Name:		ossp-uuid
Version:	1.6.2
Release:	7
Summary:    	OSSP uuid is a ISO-C:1999 application programming interface
License:    	GPLv2+
Group:      	Development/C
URL:		http://www.ossp.org/pkg/lib/uuid/
Source0:	ftp://ftp.ossp.org/pkg/lib/uuid/uuid-%{version}.tar.gz
Patch0:		uuid-1.6.2-fix-perl-install.patch
Patch1:		uuid-1.6.2-fix-php-install.patch
Patch2:		uuid-1.6.2-fix-php-link.patch
Patch3:		uuid-1.6.2-ossp.patch
Patch4:		uuid-1.6.2-fix-php-test-module-loading.patch
%if %{pgsql}
BuildRequires:	postgresql-devel
%endif
BuildRequires:	perl-devel
BuildRequires:	php-devel
BuildRequires:	php-cli

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
%define oname	ossp_uuid
%define libname %mklibname %{name} %{major}
%define	oldname	%mklibname %{oname} %{major}

%package -n     %{libname}
Summary:        Main library for ossp-uuid
Group:          System/Libraries
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
Summary:        C++ library for ossp-uuid
Group:          System/Libraries
%rename		%{oldcxx}

%description -n %{libcxx}
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
Summary:        DCE library for ossp-uuid
Group:          System/Libraries
%rename		%{olddce}

%description -n %{libdce}
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
%define	devold	%mklibname %{fname} -d

%package -n	%{devname}
Summary:	Header files for the ossp-uuid library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libcxx} = %{version}
Requires:	%{libdce} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libuuid-devel
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

%package -n	perl-OSSP-uuid
Summary:	Perl bindings for ossp-uuid
Group:		Development/Perl

%description -n	perl-OSSP-uuid
This package contains perl bindings for %{name}.

%package -n	php-OSSP-uuid
Summary:	PHP bindings for ossp-uuid
Group:		Development/PHP

%description -n	php-OSSP-uuid
This package contains php bindings for %{name}.

%if %{pgsql}
%package -n	%{libname}-pgsql
Summary:	Postgresql library for ossp-uuid
Group:		System/Libraries

%description -n	%{libname}-pgsql
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
%setup -q -n uuid-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1 -b .ossp~
%patch4 -p1 -b .php_test~

%build
export PHP_ACLOCAL=aclocal
%configure2_5x \
%if %{pgsql}
    --with-pgsql \
%endif
    --with-perl \
    --with-php \
    --with-cxx \
    --with-dce
%make

%check
make check

%install
%makeinstall_std PHP_EXTENSIONDIR=%{_libdir}/php/extensions

%if %{pgsql}
%post -n  %{libname}-pgsql
/bin/ln -s %{_libdir}/postgresql/uuid.so %{_libdir}/postgresql/uuid-ossp.so

%postun -n  %{libname}-pgsql
/bin/rm -f %{_libdir}/postgresql/uuid-ossp.so
%endif

%files
%doc OVERVIEW
%{_bindir}/uuid
%{_mandir}/man1/uuid.1*
#if %{pgsql}
#exclude %{_defaultdocdir}/lib64ossp_uuid16-pgsql/OVERVIEW
#exclude %{_defaultdocdir}/lib64ossp_uuid16/OVERVIEW
#endif

%files -n %{libname}
%{_libdir}/libossp-uuid.so.%{major}*

%files -n %{libcxx}
%{_libdir}/libossp-uuid++.so.%{major}*

%files -n %{libdce}
%{_libdir}/libossp-uuid_dce.so.%{major}*

%files  -n %{devname}
%{_libdir}/pkgconfig/ossp-uuid.pc
%{_includedir}/uuid.h
%{_includedir}/uuid++.hh
%{_includedir}/uuid_dce.h
%{_bindir}/uuid-config
%{_libdir}/libossp-uuid.so
%{_libdir}/libossp-uuid.a
%{_libdir}/libossp-uuid.la
%{_libdir}/libossp-uuid++.so
%{_libdir}/libossp-uuid++.a
%{_libdir}/libossp-uuid++.la
%{_libdir}/libossp-uuid_dce.so
%{_libdir}/libossp-uuid_dce.a
%{_libdir}/libossp-uuid_dce.la

%{_mandir}/man1/uuid-config.1*
%{_mandir}/man3/ossp-uuid.3*
%{_mandir}/man3/ossp-uuid++.3*

%files -n perl-OSSP-uuid
%{perl_vendorarch}/OSSP
%{perl_vendorarch}/auto/OSSP
%{_mandir}/man3/OSSP::uuid.3*

%files -n php-OSSP-uuid
%{_libdir}/php/extensions/ossp-uuid.so
%{_libdir}/php/extensions/uuid.php

%if %{pgsql}
%files -n %{libname}-pgsql
%{_libdir}/postgresql/ossp-uuid.so
%{_usr}/share/postgresql/ossp-uuid.sql
%endif
