Summary:	Utility to store sensitive data
Summary(pl.UTF-8):	Narzędzie do przechowywania delikatnych danych
Name:		gringotts
Version:	1.2.8
Release:	4
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://devel.pluto.linux.it/projects/Gringotts/current/%{name}-%{version}.tar.bz2
# Source0-md5:	f84add2aadca642a354105f63c117dec
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gtk+2.patch
URL:		http://devel.pluto.linux.it/projects/Gringotts/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgringotts-devel >= 1.1.1
BuildRequires:	libmcrypt-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gringotts is a small but useful utility that stores sensitive data
(passwords, credit card numbers, friends' addresses) in an organized,
optimized and most of all very secure form.

%description -l pl.UTF-8
Gringotts jest małym, lecz użytecznym narzędziem przechowującym
delikatne dane (hasła, numery kart kredytowych, adresy przyjaciół) w
zorganizowanej, zoptymalizowanej i przede wszystkim bardzo bezpiecznej
formie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Utilities/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
