Summary:	Bootp and dhcp client for automatic IP configuration
Name:		pump
Version:	0.6.4
Release:	2
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Copyright:	MIT
Source:		%{name}-%{version}.tar.gz
Requires:	rc-scripts
BuildPrereq:	popt-devel
BuildRoot:	/tmp/%{name}-%{version}-root
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

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pump
/usr/man/man8/*

%changelog
* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-2]
- adde "BuildPrereq: popt-devel",
- added Group(pl).

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- it was always requesting a 20 second lease

* Mon Mar 22 1999 Michael K. Johnson <johnsonm@redhat.com>
- added minimal man page /usr/man/man8/pump.8
