Name:           uxplay
Version:        1.65.3
Release:        2%{?dist}

%define gittag  v%{version}

Summary:        AirPlay-Mirror and AirPlay-Audio server
License:        GPLv3+
URL:            https://github.com/FDH2/UxPlay
Source0:        https://github.com/FDH2/UxPlay/archive/%{gittag}/%{name}-%{version}.tar.gz

Packager:       UxPlay maintainer
 
BuildRequires:  cmake >= 3.4.1
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       avahi

#RedHat and clones 
%if %{defined fedora} || %{defined rhel}
BuildRequires:  pkgconf
BuildRequires:  openssl-devel >= 3.0
BuildRequires:  libplist-devel >= 2.0
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
Requires:       openssl-libs >= 3.0
Requires:       libplist >= 2.0
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-libav
%endif

#Mageia
%if "%{_host_vendor}" == "mageia"
BuildRequires:  pkgconf
BuildRequires:  %{mklibname openssl-devel} >= 3.0
BuildRequires:  %{mklibname plist-devel} >= 2.0
BuildRequires:  %{mklibname avahi-compat-libdns_sd-devel}
BuildRequires:  %{mklibname gstreamer1.0-devel}
BuildRequires:  %{mklibname gstreamer-plugins-base1.0-devel}
Requires:       %{mklibname openssl3}
Requires:       %{mklibname plist2.0_3}   
Requires:       gstreamer1.0-plugins-base
Requires:       gstreamer1.0-plugins-good
Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-libav
%endif

#SUSE
%if "%{_host_vendor}" == "suse"
BuildRequires:  pkg-config
BuildRequires:  libopenssl-3-devel
BuildRequires:  libplist-2_0-devel
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
Requires:       libopenssl3
Requires:       libplist-2_0-3
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-libav
%endif

%description
An AirPlay2 Mirror and AirPlay2 Audio (but not Video) server that provides
screen-mirroring (with audio) of iOS/MacOS clients in a display window on
the server host (which can be shared using a screen-sharing application);
Apple Lossless Audio (ALAC) (e.g.,iTunes) can be streamed from client to
server in non-mirror mode

%prep

%autosetup -n uxplay-%{version}

%cmake -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}

%cmake_build

%if "%{_host_vendor}" == "suse"
#suse macro %%cmake_install installs from %%{buildsubdir} (misses docs in source directory  above it)
cd ..   
%endif

%cmake_install 

%files
%{_bindir}/uxplay
%{_mandir}/man1/uxplay.1*

%doc
%{_docdir}/%{name}/README.txt
%{_docdir}/%{name}/README.html
%{_docdir}/%{name}/README.md

%license
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/llhttp/LICENSE-MIT

%changelog
* Wed Jul 26 2023 laolux <25555671+laolux@users.noreply.github.com> 1.65.3-1
- move spec file (25555671+laolux@users.noreply.github.com)
- improve uxplay.spec (fduncanh@gmail.com)
- README edits (fduncanh@gmail.com)
- improvements to uxplay.spec RPM spec file (fduncanh@gmail.com)
- prepare 1.65.3 release (fduncanh@gmail.com)
- allow uxplay to function w/o audio in avdec_aac is missing
  (fduncanh@gmail.com)
- uxplay 1.65.2: add advice to clear cache if plugin not found
  (fduncanh@gmail.com)
- add RPM spec file, document it in README; 1.65.1 release (fduncanh@gmail.com)
- provide graceful exit if avdec_aac is absent (fduncanh@gmail.com)
- fixes for various compiler warnings (fduncanh@gmail.com)
- llhttp: minor update to v8.1.1 (fduncanh@gmail.com)
- fix minor error in uxplay -h text (fduncanh@gmail.com)
- README update about R Pi OS Legacy (Buster) (fduncanh@gmail.com)
- cosmetic fixes to debug output (fduncanh@gmail.com)
- replace a libplist-2.1.0 function, restore Debian 10 compatibility
  (fduncanh@gmail.com)
- README update (fduncanh@gmail.com)
- WIN32 use default location if BONJOUR_SDK_HOME not set (fduncanh@gmail.com)
- README updates (fduncanh@gmail.com)

* Mon Jul 24 2023 UxPlay maintainer <https://github.com/FDH2/UxPlay>
  Initial uxplay.spec: tested on Fedora 38, Rocky Linux 9.2, OpenSUSE
  Leap 15.5, Mageia 9.
- 
