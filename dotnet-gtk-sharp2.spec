#
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET language bindings for GTK+
Summary(pl):	Wi±zania GTK+ dla .NET
Name:		dotnet-gtk-sharp2
Version:	2.9.0
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk-sharp/2.9/gtk-sharp-%{version}.tar.bz2
# Source0-md5:	06228185cdbd34e033817940361e143f
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-mint.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	rpm-perlprov
Requires:	gtk+2 >= 2:2.10.1
Requires:	libglade2 >= 1:2.6.0
Requires:	mono >= 1.1.16.1
Obsoletes:	gtk-sharp2
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+ libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z GTK+.

%package devel
Summary:	Development part of GTK#
Summary(pl):	Czê¶æ dla programistów GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc
Requires:	which
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

%prep
%setup -q -n gtk-sharp-%{version}
%patch0 -p1
%patch1 -p1

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
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*sharpglue-2.so
%{_libdir}/lib*sharpglue-2.la
%dir %{_prefix}/lib/gtk-sharp-2.0
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi*
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

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%dir %{_prefix}/lib/mono/gtk-sharp-2.0
%{_prefix}/lib/mono/gtk-sharp-2.0/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/pango-sharp.dll
%{_libdir}/monodoc/sources/*
%dir %{_datadir}/gapi-2.0
%{_datadir}/gapi-2.0/atk-api.xml
%{_datadir}/gapi-2.0/gdk-api.xml
%{_datadir}/gapi-2.0/glade-api.xml
%{_datadir}/gapi-2.0/gtk-api.xml
%{_datadir}/gapi-2.0/pango-api.xml
%{_examplesdir}/%{name}-%{version}
%{_pkgconfigdir}/gapi-2.0.pc
%{_pkgconfigdir}/glade-sharp-2.0.pc
%{_pkgconfigdir}/glib-sharp-2.0.pc
%{_pkgconfigdir}/gtk-dotnet-2.0.pc
%{_pkgconfigdir}/gtk-sharp-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*sharpglue-2.a
