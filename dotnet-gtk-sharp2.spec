#
# Conditional build:
%bcond_without	gnome	# don't build GNOME (and dependent) bindings
#
%define		gtkhtml_soversion	%(/bin/ls %{_libdir}/libgtkhtml-3.8.so.* 2>/dev/null | /usr/bin/head -n 1 | /bin/awk '{ split($1,v,"."); print v[4]; }')
%define		gtkhtml_version		%(if [ -e /usr/bin/pkg-config ]; then /usr/bin/pkg-config --modversion libgtkhtml-3.8 2>/dev/null || echo 0; else echo 0; fi)
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.mono
Summary:	.NET language bindings for GTK+ and GNOME
Summary(pl):	Wi±zania GTK+ oraz GNOME dla .NET
Name:		dotnet-gtk-sharp2
Version:	2.5.90
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.go-mono.com/sources/gtk-sharp-2.0/gtk-sharp-%{version}.tar.gz
# Source0-md5:	aedbcaaa99cc9204159564b981c7a980
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-mint.patch
Patch3:		%{name}-pc-libdir.patch
Patch4:		%{name}-gtkhtml.patch
URL:		http://gtk-sharp.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libart_lgpl-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	librsvg-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	rpm-perlprov
%if %{with gnome}
BuildRequires:	gnome-panel-devel >= 2.10.0
BuildRequires:	gtkhtml-devel >= 3.8.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
%{?with_gda:BuildRequires:	libgnomedb-devel >= 1.0.0}
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	vte-devel >= 0.11.10
%endif
Requires:	mono >= 1.1.7
Obsoletes:	gtk-sharp2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z GTK+2 oraz
GNOME2.

%package devel
Summary:	Development part of GTK#
Summary(pl):	Czê¶æ dla programistów GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gtk-sharp2-devel

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%description devel -l pl
Narzêdzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystaj±cych z GTK#.

%package static
Summary:	Static gtk-sharp libraries
Summary(pl):	Biblioteki statyczne gtk-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-sharp libraries.

%description static -l pl
Biblioteki statyczne gtk-sharp.

%package gnome
Summary:	.NET language bindings for GNOME libraries
Summary(pl):	Wi±zania .NET dla bibliotek GNOME
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_gnome:Requires:	gtkhtml = %{gtkhtml_version}}

%description gnome
.NET language bindings for GNOME libraries.

%description gnome -l pl
Wi±zania .NET dla bibliotek GNOME.

%package gnome-devel
Summary:	.NET language bindings for GNOME libraries - development files
Summary(pl):	Wi±zania .NET dla bibliotek GNOME - pliki programistyczne
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
.NET language bindings for GNOME libraries - development files.

%description gnome-devel -l pl
Wi±zania .NET dla bibliotek GNOME - pliki programistyczne.

%package gnome-static
Summary:	.NET language bindings for GNOME libraries - static libraries
Summary(pl):	Wi±zania .NET dla bibliotek GNOME - static libraries
Group:		Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
.NET language bindings for GNOME libraries - static libraries.

%description gnome-static -l pl
Wi±zania .NET dla bibliotek GNOME - static libraries.

%prep
%setup -q -n gtk-sharp-%{version}
%patch1 -p1
%patch2 -p1
# for patch3:
# sed -i -e 's|libdir=${exec_prefix}/lib|libdir=@libdir@|' `find . -name '*.pc.in'`
%patch3 -p1
%patch4 -p1

# workaround for variable name
echo 'm4_pattern_allow(PKG_PATH)' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*sharpglue-2.so
%attr(755,root,root) /usr/lib/gtk-sharp-2.0/gapi*
%dir /usr/lib/gtk-sharp-2.0
%{_libdir}/lib*sharpglue-2.la
/usr/lib/mono/gac/art-sharp
/usr/lib/mono/gac/atk-sharp
/usr/lib/mono/gac/gdk-sharp
/usr/lib/mono/gac/glade-sharp
/usr/lib/mono/gac/glib-sharp
/usr/lib/mono/gac/gtk-dotnet
/usr/lib/mono/gac/gtk-sharp
/usr/lib/mono/gac/pango-sharp

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%dir /usr/lib/mono/gtk-sharp-2.0
/usr/lib/mono/gtk-sharp-2.0/art-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/atk-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/gdk-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/glade-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/glib-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/gtk-dotnet.dll
/usr/lib/mono/gtk-sharp-2.0/gtk-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/pango-sharp.dll
%dir %{_datadir}/gapi-2.0
%{_datadir}/gapi-2.0/art-api.xml
%{_datadir}/gapi-2.0/atk-api.xml
%{_datadir}/gapi-2.0/gdk-api.xml
%{_datadir}/gapi-2.0/glade-api.xml
%{_datadir}/gapi-2.0/gtk-api.xml
%{_datadir}/gapi-2.0/pango-api.xml
%{_examplesdir}/%{name}-%{version}
%{_pkgconfigdir}/art-sharp-2.0.pc
%{_pkgconfigdir}/gapi-2.0.pc
%{_pkgconfigdir}/glade-sharp-2.0.pc
%{_pkgconfigdir}/gtk-dotnet-2.0.pc
%{_pkgconfigdir}/gtk-sharp-2.0.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/lib*sharpglue-2.a

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp2-schemagen
%attr(755,root,root) /usr/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%attr(755,root,root) %{_libdir}/libgnomesharpglue-2.so
%{_libdir}/libgnomesharpglue-2.la
/usr/lib/mono/gac/gconf-sharp
/usr/lib/mono/gac/gconf-sharp-peditors
/usr/lib/mono/gac/gnome-sharp
/usr/lib/mono/gac/gnome-vfs-sharp
/usr/lib/mono/gac/gtkhtml-sharp
/usr/lib/mono/gac/rsvg-sharp
/usr/lib/mono/gac/vte-sharp

%files gnome-devel
%defattr(644,root,root,755)
/usr/lib/mono/gtk-sharp-2.0/gconf-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/gconf-sharp-peditors.dll
/usr/lib/mono/gtk-sharp-2.0/gnome-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/gnome-vfs-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/gtkhtml-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/rsvg-sharp.dll
/usr/lib/mono/gtk-sharp-2.0/vte-sharp.dll
%{_datadir}/gapi-2.0/gnome-api.xml
%{_datadir}/gapi-2.0/gnome-vfs-api.xml
%{_datadir}/gapi-2.0/gtkhtml-api.xml
%{_datadir}/gapi-2.0/rsvg-api.xml
%{_datadir}/gapi-2.0/vte-api.xml
%{_pkgconfigdir}/gconf-sharp-2.0.pc
%{_pkgconfigdir}/gnome-sharp-2.0.pc
%{_pkgconfigdir}/gnome-vfs-sharp-2.0.pc
%{_pkgconfigdir}/gtkhtml-sharp-2.0.pc
%{_pkgconfigdir}/rsvg-sharp-2.0.pc
%{_pkgconfigdir}/vte-sharp-2.0.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnomesharpglue-2.a
%endif
