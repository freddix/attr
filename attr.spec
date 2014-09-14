# based on PLD Linux spec git://git.pld-linux.org/packages/attr.git
Summary:	Utilities for managing filesystem extended attributes
Name:		attr
Version:	2.4.47
Release:	3
License:	LGPL v2+ (library), GPL v2+ (utilities)
Group:		Core/System
Source0:	http://download.savannah.gnu.org/releases/attr/%{name}-%{version}.src.tar.gz
# Source0-md5:	84f58dec00b60f2dc8fd1c9709291cc7
URL:		http://savannah.nongnu.org/projects/attr
BuildRequires:	gettext
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of tools for manipulating extended attributes on filesystem
objects, in particular getfattr(1) and setfattr(1).

%package devel
Summary:	Header files and libraries for attr development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries needed to develop programs which make use
of extended attributes.

%prep
%setup -q

%build
%{__libtoolize}
%configure \
	--disable-static
%{__make} \
	DEBUG="-DNDEBUG"    \
	OPTIMIZER="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-lib install-dev \
	DIST_ROOT=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man2

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/CHANGES
%attr(755,root,root) %{_bindir}/attr
%attr(755,root,root) %{_bindir}/getfattr
%attr(755,root,root) %{_bindir}/setfattr
%attr(755,root,root) %ghost %{_libdir}/libattr.so.?
%attr(755,root,root) %{_libdir}/libattr.so.*.*.*
%{_mandir}/man1/attr.1*
%{_mandir}/man1/getfattr.1*
%{_mandir}/man1/setfattr.1*
%{_mandir}/man5/attr.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/libattr.so
%{_libdir}/libattr.la
%{_includedir}/attr
%{_mandir}/man3/attr_*.3*

