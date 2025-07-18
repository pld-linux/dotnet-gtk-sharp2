Summary:	.NET language bindings for GTK+
Summary(pl.UTF-8):	Wiązania GTK+ dla .NET
Name:		dotnet-gtk-sharp2
Version:	2.12.45
Release:	1
License:	LGPL v2
Group:		Libraries
# latest downloads summary at http://download.mono-project.com/sources-stable/
Source0:	http://download.mono-project.com/sources/gtk-sharp212/gtk-sharp-%{version}.tar.gz
# Source0-md5:	48cdd0292229eba58b403930032fb766
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-mint.patch
URL:		http://www.mono-project.com/GtkSharp
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.31
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	rpmbuild(monoautodeps)
Requires:	glib2 >= 1:2.31
Requires:	gtk+2 >= 2:2.12.0
Requires:	libglade2 >= 1:2.3.6
Requires:	mono >= 1.1.16.1
Obsoletes:	gtk-sharp2
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+ libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z GTK+.

%package devel
Summary:	Development part of Gtk# 2
Summary(pl.UTF-8):	Część dla programistów Gtk# 2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.6
Requires:	which
Obsoletes:	gtk-sharp2-devel

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using Gtk# 2.

%description devel -l pl.UTF-8
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z Gtk# 2.

%package static
Summary:	Static Gtk# 2 libraries
Summary(pl.UTF-8):	Biblioteki statyczne Gtk# 2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Gtk# 2 libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Gtk# 2.

%prep
%setup -q -n gtk-sharp-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libatksharpglue-2.so
%attr(755,root,root) %{_libdir}/libgdksharpglue-2.so
%attr(755,root,root) %{_libdir}/libgladesharpglue-2.so
%attr(755,root,root) %{_libdir}/libglibsharpglue-2.so
%attr(755,root,root) %{_libdir}/libgtksharpglue-2.so
%attr(755,root,root) %{_libdir}/libpangosharpglue-2.so
# needed for DllImport on basename
%{_libdir}/libatksharpglue-2.la
%{_libdir}/libgdksharpglue-2.la
%{_libdir}/libgladesharpglue-2.la
%{_libdir}/libglibsharpglue-2.la
%{_libdir}/libgtksharpglue-2.la
%{_libdir}/libpangosharpglue-2.la
%{_prefix}/lib/mono/gac/atk-sharp
%{_prefix}/lib/mono/gac/gdk-sharp
%{_prefix}/lib/mono/gac/glade-sharp
%{_prefix}/lib/mono/gac/glib-sharp
%{_prefix}/lib/mono/gac/gtk-dotnet
%{_prefix}/lib/mono/gac/gtk-sharp
%{_prefix}/lib/mono/gac/pango-sharp

%{_prefix}/lib/mono/gac/policy.2.4.atk-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gdk-sharp
%{_prefix}/lib/mono/gac/policy.2.4.glade-sharp
%{_prefix}/lib/mono/gac/policy.2.4.glib-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gtk-dotnet
%{_prefix}/lib/mono/gac/policy.2.4.gtk-sharp
%{_prefix}/lib/mono/gac/policy.2.4.pango-sharp

%{_prefix}/lib/mono/gac/policy.2.6.atk-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gdk-sharp
%{_prefix}/lib/mono/gac/policy.2.6.glade-sharp
%{_prefix}/lib/mono/gac/policy.2.6.glib-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gtk-dotnet
%{_prefix}/lib/mono/gac/policy.2.6.gtk-sharp
%{_prefix}/lib/mono/gac/policy.2.6.pango-sharp

%{_prefix}/lib/mono/gac/policy.2.8.atk-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gdk-sharp
%{_prefix}/lib/mono/gac/policy.2.8.glade-sharp
%{_prefix}/lib/mono/gac/policy.2.8.glib-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gtk-dotnet
%{_prefix}/lib/mono/gac/policy.2.8.gtk-sharp
%{_prefix}/lib/mono/gac/policy.2.8.pango-sharp

%{_prefix}/lib/mono/gac/policy.2.10.atk-sharp
%{_prefix}/lib/mono/gac/policy.2.10.gdk-sharp
%{_prefix}/lib/mono/gac/policy.2.10.glade-sharp
%{_prefix}/lib/mono/gac/policy.2.10.glib-sharp
%{_prefix}/lib/mono/gac/policy.2.10.gtk-dotnet
%{_prefix}/lib/mono/gac/policy.2.10.gtk-sharp
%{_prefix}/lib/mono/gac/policy.2.10.pango-sharp

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi2-codegen
%attr(755,root,root) %{_bindir}/gapi2-fixup
%attr(755,root,root) %{_bindir}/gapi2-parser
%dir %{_prefix}/lib/gtk-sharp-2.0
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi-fixup.exe
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi-parser.exe
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi_codegen.exe
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi_pp.pl
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi2xml.pl
%dir %{_prefix}/lib/mono/gtk-sharp-2.0
%{_prefix}/lib/mono/gtk-sharp-2.0/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/pango-sharp.dll

%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.pango-sharp.dll

%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.pango-sharp.dll

%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.pango-sharp.dll

%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.10.pango-sharp.dll

%{_prefix}/lib/monodoc/sources/gtk-sharp-docs.*
%dir %{_datadir}/gapi-2.0
%{_datadir}/gapi-2.0/atk-api.xml
%{_datadir}/gapi-2.0/gdk-api.xml
%{_datadir}/gapi-2.0/glade-api.xml
%{_datadir}/gapi-2.0/glib-api.xml
%{_datadir}/gapi-2.0/gtk-api.xml
%{_datadir}/gapi-2.0/pango-api.xml
%{_pkgconfigdir}/gapi-2.0.pc
%{_pkgconfigdir}/glade-sharp-2.0.pc
%{_pkgconfigdir}/glib-sharp-2.0.pc
%{_pkgconfigdir}/gtk-dotnet-2.0.pc
%{_pkgconfigdir}/gtk-sharp-2.0.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libatksharpglue-2.a
%{_libdir}/libgdksharpglue-2.a
%{_libdir}/libgladesharpglue-2.a
%{_libdir}/libglibsharpglue-2.a
%{_libdir}/libgtksharpglue-2.a
%{_libdir}/libpangosharpglue-2.a
