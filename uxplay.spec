

Name:    uxplay
Version: 1.46b
Release: 1%{?dist}
Summary: UxPlay is an AirPlay server for Linux

License: GPLv3
Source0: uxplay-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  libplist-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  libX11-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
Requires:  openssl
Requires:  gstreamer1-libav
Requires:  gstreamer1-plugins-bad-free
Requires:  gstreamer1-vaapi

%description
UxPlay is an AirPlay server for Linux. It lets you stream the display content of your Apple devices such as IPhone and IPad to your Linux computer via wifi.

%prep
%setup -q

%build
%cmake -DZOOMFIX=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/uxplay
%{_docdir}/uxplay/LICENSE
%{_docdir}/uxplay/README.html
%{_docdir}/uxplay/README.md
%{_docdir}/uxplay/README.txt
%{_docdir}/uxplay/llhttp/LICENSE-MIT
%{_mandir}/man1/uxplay.1.gz

%changelog
* Sun Jan 23 2022 laolux <25555671+laolux@users.noreply.github.com> 1.46b-1
- update to v1.46b

* Thu Jan 20 2022 laolux <25555671+laolux@users.noreply.github.com> 1.46-1
- updated to version 1.46

* Mon Jan 17 2022 laolux <25555671+laolux@users.noreply.github.com> v1.45-1
- updated to upstream release v1.45

* Sun Jan 16 2022 laolux <25555671+laolux@users.noreply.github.com> v1.44g-1
- new package built with tito

* Sat Jan 15 2022 laolux <laolux@spamprotected.example.com> - v1.44g-1
- Initial RPM release
