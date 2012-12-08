# needed for rpm53
%bcond_with bootstrap

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
Name:		ossp-uuid
Version:	1.6.2
Release:	10
Summary:	OSSP uuid is a ISO-C:1999 application programming interface
License:	GPLv2+
Group:		Development/C
URL:		http://www.ossp.org/pkg/lib/uuid/
Source0:	ftp://ftp.ossp.org/pkg/lib/uuid/uuid-%{version}.tar.gz
Patch0:		uuid-1.6.2-fix-perl-install.patch
Patch1:		uuid-1.6.2-fix-php-install.patch
Patch2:		uuid-1.6.2-fix-php-link.patch
Patch3:		uuid-1.6.2-ossp.patch
Patch4:		uuid-1.6.2-fix-php-test-module-loading.patch
Patch5:         uuid-1.6.2-php-54x.patch
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
%setup -q -n uuid-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1 -b .ossp~
%patch4 -p1 -b .php_test~
%patch5 -p1 -b .php54~

%build
export PHP_ACLOCAL=aclocal
%configure2_5x	--includedir=%{_includedir}/ossp-uuid \
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
%makeinstall_std -C pgsql 
ln -s ossp-uuid.so %{buildroot}%{_libdir}/postgresql/uuid.so 
ln -s uuid.sql %{buildroot}%{_datadir}/postgresql/ossp-uuid.sql
%endif

%files
%doc OVERVIEW
%{_bindir}/uuid
%{_mandir}/man1/uuid.1*

%files -n %{libname}
%{_libdir}/libossp-uuid.so.%{major}*

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


%changelog
* Mon Jan 23 2012 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-10
+ Revision: 766782
- various fixes
- rebuilt for perl-5.14.2

* Thu Oct 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-9
+ Revision: 703272
- rebuilt due to package loss

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added bootstrap bcond, crazy to expect php and postgresql just to build rpm53

* Wed May 25 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.2-8
+ Revision: 678999
- place headers in their own sub-directory to prevent any possible conflicts

* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.2-7
+ Revision: 673154
- fix permissions and installation of libraries so that we get them all stripped
- fix postgresql plugin
- remove conflicts with libuiid-devel now that it's header path has changed
- rename package to match library name

* Fri Apr 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.2-6
+ Revision: 656711
- add dependencies on the c++ & dce libraries for -devel packages

* Thu Mar 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.2-5
+ Revision: 648404
- fix php test suite and enable regression checks
- build dce library
- enable build of c++ library
- use correct group for perl & php module
- perform some cosmetics and cleanups
- drop bogus provides
- drop ancient ldconfig scriptlets
- fix unique library soname and pkgconfig file (P3)

* Sat Jan 01 2011 Funda Wang <fwang@mandriva.org> 1.6.2-4mdv2011.0
+ Revision: 627159
- fix link of php binding
- use aclocal instead of its 1.7 version for phpize

* Thu Dec 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.2-3mdv2011.0
+ Revision: 622424
- add perl and php bindings

* Tue Jul 13 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.6.2-2mdv2011.0
+ Revision: 551531
- bump release

* Sat May 22 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 545712
- import ossp_uuid

