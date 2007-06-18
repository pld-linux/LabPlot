Summary:	Function and Data Plotter
Summary(pl.UTF-8):	Wykreślacz funkcji i danych
Name:		LabPlot
Version:	1.5.1.5
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/labplot/%{name}-%{version}.tar.bz2
# Source0-md5:	c3eac8284688ebe5ad53d90c773ec7bb
URL:		http://labplot.sourceforge.net/
BuildRequires:	ImageMagick-c++-devel >= 1:6.2.4.0
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program for plotting of functions and data manipulation.

%description -l pl.UTF-8
Program do wykreślania funkcji oraz manipulacji na danych.

%package static
Summary:	LabPlot static libraries
Summary(pl.UTF-8):	Biblioteki statyczne LabPlot
Group:		Development/Libraries

%description static
LabPlot static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne LabPlot.

%prep
%setup -q 

%build
# compiled binaries & objects
rm -f texvc/texvc texvc/*.o texvc/*.cmx texvc/*.cmi

export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/labplot.1
echo ".so LabPlot.1" > $RPM_BUILD_ROOT%{_mandir}/man1/labplot.1

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO INSTALL ChangeLog CHANGES FEATURES LabPlot.lsm
%attr(755,root,root) %{_bindir}/LabPlot
%attr(755,root,root) %{_bindir}/opj2dat
%attr(755,root,root) %{_bindir}/texvc
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_desktopdir}/kde/LabPlot.desktop
%{_datadir}/mimelnk/application/x-lpl.desktop
%{_datadir}/apps/LabPlot
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
