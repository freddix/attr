Summary:	Utility for managing filesystem extended attributes
Name:		attr
Version:	2.4.46
Release:	1
License:	LGPL v2+ (library), GPL v2+ (utilities)
Group:		Applications/System
Source0:	http://download.savannah.gnu.org/releases/attr/%{name}-%{version}.src.tar.gz
# Source0-md5:	db557c17fdfa4f785333ecda08654010
URL:		http://savannah.nongnu.org/projects/attr
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An experimental attr command to manipulate extended attributes under
Linux.

%package devel
Summary:	Header files and libraries to use extended attributes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files to develop software which manipulate extended attributes.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--disable-static
%{__make} \
	DEBUG="-DNDEBUG"	\
	OPTIMIZER="%{rpmcflags} -DENABLE_GETTEXT"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-lib install-dev \
	DIST_ROOT=$RPM_BUILD_ROOT

rm -rf	$RPM_BUILD_ROOT%{_mandir}/man2

%find_lang %{name}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

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

