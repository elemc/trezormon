Name:           trezormon
Version:        0.15.0
Release:        1%{?dist}
Summary:        Trezor Monitoring System application

License:        Proprietary
URL:            http://trezorrussia.ru/
Source0:        https://panov.email/%{name}-%{version}.tar.xz

BuildArch:      x86_64

BuildRequires:  systemd-rpm-macros 
Requires:       postgresql-server

%description
This package contains Trezor Monitoring System application. 
Application for monitoring of Trezor secuity devices.

%prep
%autosetup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/trezormon
mkdir -p $RPM_BUILD_ROOT/opt/trezormon/frontend
mkdir -p $RPM_BUILD_ROOT/opt/trezormon/docs
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp -r  %{_builddir}/%{name}-%{version}/frontend $RPM_BUILD_ROOT/opt/trezormon/
cp -r  %{_builddir}/%{name}-%{version}/docs $RPM_BUILD_ROOT/opt/trezormon/
ln -sf /opt/trezormon/%{name}-%{version} $RPM_BUILD_ROOT/opt/trezormon/%{name}
install -D -m 0755 %{_builddir}/%{name}-%{version}/%{name}-%{version} $RPM_BUILD_ROOT/opt/trezormon/%{name}-%{version}
install -D -m 0644 %{_builddir}/%{name}-%{version}/%{name}.toml $RPM_BUILD_ROOT/opt/trezormon/%{name}.toml
install -D -m 0644 %{_builddir}/%{name}-%{version}/%{name}.service $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%files
/opt/trezormon/frontend/*
/opt/trezormon/docs/*
/opt/trezormon/%{name}-%{version}
/opt/trezormon/%{name}
/opt/trezormon/%{name}.toml
%{_unitdir}/%{name}.service

%preun
%systemd_preun %{name}.service
exit 0

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Thu Oct 31 2024 Alexei Panov <alexei@panov.email> - 0.15.0
- new release

* Tue Jun 25 2024 Alexei Panov <alexei@panov.email> - 0.14.3-1
- new release

* Thu Jun 20 2024 Alexei Panov <alexei@panov.email> - 0.14.0-1
- new release

* Thu Apr 18 2024 Alexei Panov <alexei@panov.email> - 0.12.0-1
- new release

* Wed Jan 10 2024 Alexei Panov <alexei@panov.email> - 0.10.0-2
- fix in files

* Wed Jan 10 2024 Alexei Panov <alexei@panov.email> - 0.10.0-1
- initial build
