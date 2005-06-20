Summary:	Function and Data Plotter
Summary(pl):	Wykre¶lacz funkcji i danych
Name:		LabPlot
Version:	1.4.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/labplot/%{name}-%{version}.tar.bz2
# Source0-md5:	b19839478f2c95880c57aaad7b4e05e7
URL:		http://labplot.sourceforge.net/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program for plotting of functions and data manipulation.

%description -l pl
Program do wykre¶lania funkcji oraz manipulacji na danych.

%package static
Summary:	LabPlot static libraries
Summary(pl):	Biblioteki statytczne LabPlot
Group:		Development/Libraries

%description static
LabPlot static libraries

%description static -l pl
Biblioteki statytczne LabPlot

%prep
%setup -q

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
cp -f /usr/share/automake/config.sub admin
%configure \
%ifarch %{x8664} sparc sparc64 ppc ppc64
	--disable-cdf \
%endif
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/LabPlot.desktop $RPM_BUILD_ROOT%{_desktopdir}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_desktopdir}/LabPlot.desktop
%{_datadir}/mimelnk/application/x-lpl.desktop
%{_datadir}/apps/LabPlot
%{_iconsdir}/*/*/*/*.png
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
