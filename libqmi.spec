Summary:	GLib library for talking to WWAN modems and devices using QMI protocol
Name:		libqmi
Version:	1.8.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/libqmi/%{name}-%{version}.tar.xz
# Source0-md5:	1c4c64c0894f691632727363abec32b8
URL:		http://www.freedesktop.org/wiki/Software/libqmi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libqmi is a GLib library for talking to WWAN modems and devices which
speak the Qualcomm MSM Interface (QMI) protocol.

%package devel
Summary:	Header files for libqmi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libqmi library.

%package apidocs
Summary:	libqmi API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for libqmi library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/qmi-network
%attr(755,root,root) %{_bindir}/qmicli
%attr(755,root,root) %ghost %{_libdir}/libqmi-glib.so.1
%attr(755,root,root) %{_libdir}/libqmi-glib.so.*.*.*
%attr(755,root,root) %{_libexecdir}/qmi-proxy
%{_mandir}/man1/qmi-network.1*
%{_mandir}/man1/qmicli.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmi-glib.so
%{_includedir}/libqmi-glib
%{_pkgconfigdir}/qmi-glib.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libqmi-glib

