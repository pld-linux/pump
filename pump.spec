Summary:	Bootp and dhcp client for automatic IP configuration
Summary(pl):	Klient bootp i dhcp do automatycznej konfiguracji IP
Name:		pump
Version:	0.7.9
Release:	3
License:	MIT
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Prereq:		rc-scripts
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bootpc

%description
DHCP (Dynamic Host Configuration Protocol) and BOOTP (Boot Protocol)
are protocols which allow individual devices on an IP network to get
their own network configuration information (IP address, subnetmask,
broadcast address, etc.) from network servers. The overall purpose of
DHCP and BOOTP is to make it easier to administer a large network.

Pump is a combined BOOTP and DHCP client daemon, which allows your
machine to retrieve configuration information from a server. You
should install this package if you are on a network which uses BOOTP
or DHCP.

%description -l pl
DHCP (Dynamic Host Configuration Protocol) i BOOTP (Boot Protocol) to
protoko³y pozwalaj±ce urz±dzeniom w sieci IP otrzymaæ informacje o
konfiguracji swojej sieci od serwerów. Celem DHCP i BOOTP jest
u³atwienie administrowania du¿± sieci±.

Pump jest demonem zawieraj±cym klientów BOOTP i DHCP, co pozwala
maszynie odczytywaæ informacje o konfiguracji z serwera.

%prep
%setup -q
%patch -p1

%build
%{__make} LDFLAGS="%{rpmldflags}" COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install MAN8PATH="$RPM_BUILD_ROOT%{_mandir}/man8"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pump
%{_mandir}/man8/*
