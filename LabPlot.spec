Summary:	Function and Data Plotter
Summary(pl):	Wykre¶lacz funkcji i danych
Name:		LabPlot
URL:		http://labplot.sourceforge.net/
Version:	1.3.1
Release:	1
Source0:	http://dl.sourceforge.net/labplot/%{name}-%{version}.tar.bz2
Group:		Applications/Math
License:	GPL
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program for plotting of functions and data manipulation.

%description -l pl
Program do wykre¶lania funkcji oraz manipulacji na danych.

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
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO INSTALL ChangeLog CHANGES FEATURES LabPlot.lsm
%attr(755,root,root) %{_bindir}/LabPlot
%{_datadir}/applnk/Applications/LabPlot.desktop
%{_datadir}/mimelnk/application/x-lpl.desktop
%{_datadir}/apps/LabPlot/
%{_datadir}/icons/hicolor/64x64/mimetypes/lpl.png
%{_datadir}/icons/locolor/16x16/apps/LabPlot.png
%{_datadir}/icons/locolor/16x16/mimetypes/lpl.png
%{_datadir}/icons/locolor/32x32/apps/LabPlot.png
%{_datadir}/icons/locolor/32x32/mimetypes/lpl.png
%{_datadir}/icons/hicolor/48x48/apps/LabPlot.png
%{_datadir}/icons/hicolor/48x48/mimetypes/lpl.png
%{_libdir}/lib*.so.*.*.*
%lang(en) %{_kdedocdir}/en/%{name}
%lang(de) %{_kdedocdir}/de/%{name}
