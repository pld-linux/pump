Summary:	Bootp and dhcp client for automatic IP configuration
Summary(es):	Cliente dchp y bootp para configuraci�n autom�tica de IP
Summary(pl):	Klient bootp i dhcp do automatycznej konfiguracji IP
Summary(pt_BR):	Cliente para dhcp e bootp para configura��o autom�tica de IP
Summary(ru):	������ bootp � dhcp ��� �������������� ��������� IP
Summary(uk):	�̦��� bootp �� dhcp ��� ������������� ������������ IP
Name:		pump
Version:	0.8.24
Release:	1
License:	MIT
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	866fc9f62b8161eb1514a6a06597edc9
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-pl.patch
BuildRequires:	gettext-devel
BuildRequires:	popt-devel
Requires:	rc-scripts
Obsoletes:	bootpc
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

%description -l es
Cliente dchp y bootp para configuraci�n autom�tica de IP.

%description -l pl
DHCP (Dynamic Host Configuration Protocol) i BOOTP (Boot Protocol) to
protoko�y pozwalaj�ce urz�dzeniom w sieci IP otrzyma� informacje o
konfiguracji swojej sieci od serwer�w. Celem DHCP i BOOTP jest
u�atwienie administrowania du�� sieci�.

Pump jest demonem zawieraj�cym klient�w BOOTP i DHCP, co pozwala
maszynie odczytywa� informacje o konfiguracji z serwera.

%description -l pt_BR
O pump � um cliente DHCP e BOOTP, que permite que sua m�quina busque
informa��es de configura��o de um servidor.

Instale este pacote se voc� deseja utilizar BOOTP ou DHCP.

%description -l uk
DHCP (Dynamic Host Configuration Protocol) �� BOOTP (Boot Protocol) -
�� ���������, �˦ ���������� ������� ��������� IP-����֦ ����������
�������æ� ��� �� ���Ʀ����æ� ((IP-������, ����� Ц�����֦, ��������
� �.�.) � �����Ҧ� ����֦. ��������� ����� DHCP �� BOOTP � ���������
��������� ������� �������.

Pump - �� ���¦������� ����� �̦��Ԧ� BOOTP �� DHCP, ���� ������Ѥ
��ۦ� ����Φ ���������� ���Ʀ����æ��� �������æ� � �������.
������צ�� ��� ����� ���� �� � ����֦, ��� ����������դ BOOTP ���
DHCP.

%description -l ru
DHCP (Dynamic Host Configuration Protocol) � BOOTP (Boot Protocol) -
��� ���������, ������� ��������� ��������� ����������� IP-����
�������� ���������� � �� ������������ (IP-�����, ����� �������,
�������� � �.�.) � ������� ��������. ����� ����� DHCP � BOOTP ��������
��������� ���������� ������� �����.

Pump - ��� ��������������� ����� �������� BOOTP � DHCP, �������
��������� ����� ������ �������� ���������������� ���������� � �������.
���������� ���� ����� ���� �� � ����, ������� ���������� BOOTP ���
DHCP.

%package devel
Summary:	Header file for sending DHCP and BOOTP requests
Summary(pl):	Plik nag��wkowy do wysy�ania ��da� DHCP i BOOTP
Group:		Development/Libraries
# doesn't require base

%description devel
The pump-devel package provides system developers the ability to send
BOOTP and DHCP requests from their programs. BOOTP and DHCP are
protocols used to provide network configuration information to
networked machines.

%description devel -l pl
Ten pakiet daje programistom mo�liwo�� wysy�ania ��da� BOOTP i DHCP w
swoich programach. BOOTP i DHCP to protoko�y s�u��ce do udost�pniania
informacji o konfiguracji sieci innym maszynom.

%package static
Summary:	Static library for sending DHCP and BOOTP requests
Summary(pl):	Biblioteka statyczna do wysy�ania ��da� DHCP i BOOTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for pump.

%description static -l pl
Statyczna biblioteka pump.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{eu_ES,eu}.po
mv -f po/{no,nb}.po
mv -f po/{sr,sr@Latn}.po

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
