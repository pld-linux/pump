Summary:	Bootp and dhcp client for automatic IP configuration
Summary(es.UTF-8):	Cliente dchp y bootp para configuración automática de IP
Summary(pl.UTF-8):	Klient bootp i dhcp do automatycznej konfiguracji IP
Summary(pt_BR.UTF-8):	Cliente para dhcp e bootp para configuração automática de IP
Summary(ru.UTF-8):	Клиент bootp и dhcp для автоматической настройки IP
Summary(uk.UTF-8):	Клієнт bootp та dhcp для автоматичного налагодження IP
Name:		pump
Version:	0.8.24
Release:	2
License:	MIT
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	866fc9f62b8161eb1514a6a06597edc9
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-pl.patch
BuildRequires:	gettext-tools
BuildRequires:	popt-devel
Requires:	rc-scripts
Obsoletes:	bootpc
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
Cliente dchp y bootp para configuración automática de IP.

%description -l pl.UTF-8
DHCP (Dynamic Host Configuration Protocol) i BOOTP (Boot Protocol) to
protokoły pozwalające urządzeniom w sieci IP otrzymać informacje o
konfiguracji swojej sieci od serwerów. Celem DHCP i BOOTP jest
ułatwienie administrowania dużą siecią.

Pump jest demonem zawierającym klientów BOOTP i DHCP, co pozwala
maszynie odczytywać informacje o konfiguracji z serwera.

%description -l pt_BR.UTF-8
O pump é um cliente DHCP e BOOTP, que permite que sua máquina busque
informações de configuração de um servidor.

Instale este pacote se você deseja utilizar BOOTP ou DHCP.

%description -l uk.UTF-8
DHCP (Dynamic Host Configuration Protocol) та BOOTP (Boot Protocol) -
це протоколи, які дозволяють окремим пристроям IP-мережі отримувати
інформацію про їх конфігурацію ((IP-адреса, маска підмережі, бродкаст
і т.і.) з серверів мережі. Загальною метою DHCP та BOOTP є спрощення
керування великою мережею.

Pump - це комбінований демон клієнтів BOOTP та DHCP, який дозволяє
вашій машині отримувати конфігураційну інформацію з сервера.
Встановіть цей пакет якщо ви в мережі, яка використовує BOOTP або
DHCP.

%description -l ru.UTF-8
DHCP (Dynamic Host Configuration Protocol) и BOOTP (Boot Protocol) -
это протоколы, которые позволяют отдельным устройствам IP-сети
получать информацию о их конфигурации (IP-адрес, маска подсети,
бродкаст и т.п.) с сетевых серверов. Общей целью DHCP и BOOTP является
упрощение управления большой сетью.

Pump - это комбинированный демон клиентов BOOTP и DHCP, который
позволяет вашей машине получать конфигурационную информацию с сервера.
Установите этот пакет если вы в сети, которая использует BOOTP или
DHCP.

%package devel
Summary:	Header file for sending DHCP and BOOTP requests
Summary(pl.UTF-8):	Plik nagłówkowy do wysyłania żądań DHCP i BOOTP
Group:		Development/Libraries
# doesn't require base

%description devel
The pump-devel package provides system developers the ability to send
BOOTP and DHCP requests from their programs. BOOTP and DHCP are
protocols used to provide network configuration information to
networked machines.

%description devel -l pl.UTF-8
Ten pakiet daje programistom możliwość wysyłania żądań BOOTP i DHCP w
swoich programach. BOOTP i DHCP to protokoły służące do udostępniania
informacji o konfiguracji sieci innym maszynom.

%package static
Summary:	Static library for sending DHCP and BOOTP requests
Summary(pl.UTF-8):	Biblioteka statyczna do wysyłania żądań DHCP i BOOTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for pump.

%description static -l pl.UTF-8
Statyczna biblioteka pump.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{eu_ES,eu}.po
mv -f po/{no,nb}.po
mv -f po/{sr,sr@latin}.po

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	lib=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pump
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pump.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpump.a
