Summary:	Function and Data Plotter
Summary(pl):	Wykreślacz funkcji i danych
Name:		LabPlot
URL:		http://labplot.sourceforge.net/
Version:	1.3.1
Release:	1
Source0:	http://dl.sourceforge.net/labplot/%{name}-%{version}.tar.bz2
# Source0-md5:	a6001c52eaee6518b9c5965cfc826f2f
Group:		Applications/Math
License:	GPL
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program for plotting of functions and data manipulation.

%description -l pl
Program do wykreślania funkcji oraz manipulacji na danych.

%prep
%setup -q

%build
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
	DESTDIR="$RPM_BUILD_ROOT"

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/LabPlot.desktop $RPM_BUILD_ROOT%{_desktopdir}
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO INSTALL ChangeLog CHANGES FEATURES LabPlot.lsm
%attr(755,root,root) %{_bindir}/LabPlot
%{_desktopdir}/LabPlot.desktop
%{_datadir}/mimelnk/application/x-lpl.desktop
%{_datadir}/apps/LabPlot/
%{_iconsdir}/*/*/*/*.png
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
