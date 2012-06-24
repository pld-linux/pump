Summary:	Bootp and dhcp client for automatic IP configuration
Summary(es):	Cliente dchp y bootp para configuraci�n autom�tica de IP
Summary(pl):	Klient bootp i dhcp do automatycznej konfiguracji IP
Summary(pt_BR):	Cliente para dhcp e bootp para configura��o autom�tica de IP
Summary(ru):	������ bootp � dhcp ��� �������������� ��������� IP
Summary(uk):	�̦��� bootp �� dhcp ��� ������������� ������������ IP
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
