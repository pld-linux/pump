Summary:	Bootp and dhcp client for automatic IP configuration
Name:		pump
Version:	0.7.9
Release:	2
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	MIT
Source:		%{name}-%{version}.tar.gz
Patch:		pump-Makefile.patch
Requires:	rc-scripts
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bootpc

%description
DHCP (Dynamic Host Configuration Protocol) and BOOTP (Boot Protocol)
are protocols which allow individual devices on an IP network to get
their own network configuration information (IP address, subnetmask,
broadcast address, etc.) from network servers.  The overall purpose of
DHCP and BOOTP is to make it easier to administer a large network.

Pump is a combined BOOTP and DHCP client daemon, which allows your machine
to retrieve configuration information from a server.  You should install
this package if you are on a network which uses BOOTP or DHCP.

%prep
%setup -q
%patch -p1

%build
make LDFLAGS="-s" COPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install MAN8PATH="$RPM_BUILD_ROOT%{_mandir}/man8"

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pump
%{_mandir}/man8/*
