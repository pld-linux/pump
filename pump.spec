Summary:	Bootp and dhcp client for automatic IP configuration
Summary(es):	Cliente dchp y bootp para configuraciСn automАtica de IP
Summary(pl):	Klient bootp i dhcp do automatycznej konfiguracji IP
Summary(pt_BR):	Cliente para dhcp e bootp para configuraГЦo automАtica de IP
Summary(ru):	Клиент bootp и dhcp для автоматической настройки IP
Summary(uk):	Кл╕╓нт bootp та dhcp для автоматичного налагодження IP
Name:		pump
Version:	0.8.11
Release:	10
License:	MIT
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	8bc6cc32a6c2224a8b87e7785eee5fca
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-nobootp.patch
Patch2:		%{name}-retry-forever.patch
Patch3:		%{name}-rhbug-21088.patch
Patch4:		%{name}-rhbug-17724.patch
BuildRequires:	popt-devel
PreReq:		rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	bootpc
Obsoletes:	pump-devel

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

%description -l es
Cliente dchp y bootp para configuraciСn automАtica de IP.

%description -l pl
DHCP (Dynamic Host Configuration Protocol) i BOOTP (Boot Protocol) to
protokoЁy pozwalaj╠ce urz╠dzeniom w sieci IP otrzymaФ informacje o
konfiguracji swojej sieci od serwerСw. Celem DHCP i BOOTP jest
uЁatwienie administrowania du©╠ sieci╠.

Pump jest demonem zawieraj╠cym klientСw BOOTP i DHCP, co pozwala
maszynie odczytywaФ informacje o konfiguracji z serwera.

%description -l pt_BR
O pump И um cliente DHCP e BOOTP, que permite que sua mАquina busque
informaГУes de configuraГЦo de um servidor.

Instale este pacote se vocЙ deseja utilizar BOOTP ou DHCP.

%description -l uk
DHCP (Dynamic Host Configuration Protocol) та BOOTP (Boot Protocol) -
це протоколи, як╕ дозволяють окремим пристроям IP-мереж╕ отримувати
╕нформац╕ю про ╖х конф╕гурац╕ю ((IP-адреса, маска п╕дмереж╕, бродкаст
╕ т.╕.) з сервер╕в мереж╕. Загальною метою DHCP та BOOTP ╓ спрощення
керування великою мережею.

Pump - це комб╕нований демон кл╕╓нт╕в BOOTP та DHCP, який дозволя╓
ваш╕й машин╕ отримувати конф╕гурац╕йну ╕нформац╕ю з сервера.
Встанов╕ть цей пакет якщо ви в мереж╕, яка використову╓ BOOTP або
DHCP.

%description -l ru
DHCP (Dynamic Host Configuration Protocol) и BOOTP (Boot Protocol) -
это протоколы, которые позволяют отдельным устройствам IP-сети
получать информацию о их конфигурации (IP-адрес, маска подсети,
бродкаст и т.п.) с сетевых серверов. Общей целью DHCP и BOOTP является
упрощение управления большой сетью.

Pump - это комбинированный демон клиентов BOOTP и DHCP, который
позволяет вашей машине получать конфигурационную информацию с сервера.
Установите этот пакет если вы в сети, которая использует BOOTP или
DHCP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} \
	LDFLAGS="%{rpmldflags}" \
	COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	MAN8PATH="$RPM_BUILD_ROOT%{_mandir}/man8"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pump
%{_mandir}/man8/*
