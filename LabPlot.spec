Summary:	Function and Data Plotter
Summary(pl):	Wykre¶lacz funkcji i danych
Name:		LabPlot
Version:	1.3.1
Release:	4
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/labplot/%{name}-%{version}.tar.bz2
# Source0-md5:	a6001c52eaee6518b9c5965cfc826f2f
Patch0:		%{name}-desktop.patch
URL:		http://labplot.sourceforge.net/
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program for plotting of functions and data manipulation.

%description -l pl
Program do wykre¶lania funkcji oraz manipulacji na danych.

%prep
%setup -q
%patch0

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
cp -f /usr/share/automake/config.sub admin
%configure \
%ifarch sparc sparc64 ppc ppc64 amd64
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
