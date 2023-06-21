

Name:    uxplay
Version: 1.65
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
* Wed Jun 21 2023 laolux <25555671+laolux@users.noreply.github.com> 1.65-1
- Automatic commit of package [uxplay] release [1.63-1].
  (25555671+laolux@users.noreply.github.com)
- README fixes (fduncanh@gmail.com)
- Automatic commit of package [uxplay] release [1.62-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.61-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.60-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.56-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.55-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.47-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46b-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46-1].
  (25555671+laolux@users.noreply.github.com)
- Initialized to use tito. (25555671+laolux@users.noreply.github.com)
- README updates (fduncanh@gmail.com)
- corrected parsing of configuration file for quoted option items
  (fduncanh@gmail.com)
- Preparing for v1.65 release; cleanup after changes (fduncanh@gmail.com)
- Disable "SupportsLegacyPairing" to allow fast connections (thanks @shuax)
  (fduncanh@gmail.com)
- fix unsafe strcmp (AirMyPC segfault) + timing fix for AirMyPC client
  (fduncanh@gmail.com)
- protocol modifications allowing "supports legacy pairing" to be disabled
  (fduncanh@gmail.com)
- call audio_renderer_stop after audio connection stops (fixes #201)
  (fduncanh@gmail.com)
- mac /Homebrew cleanup of PKG_CONFIG_PATH (fduncanh@gmail.com)
- README update (building libplist from source) (fduncanh@gmail.com)
- fix README typos, macOS updates (fduncanh@gmail.com)
- UxPlay 1.64: -h, manpage and README updates (fduncanh@gmail.com)
- add ability to use a configuration file uxplayrc (fduncanh@gmail.com)
- clean up SPS/PPS prepend code (for IDR frames) + cosmetic cleanups
  (fduncanh@gmail.com)
- update README about -vsync, -async options (fduncanh@gmail.com)
- raop_ntp.c, utils.c : fixes #192 (fduncanh@gmail.com)
- only call utils_data_to_string in -d debug mode (fduncanh@gmail.com)
- fix errors in recent sprintf->snprintf "fix" (fduncanh@gmail.com)
- update README for Homebrew changes on macOS (fduncanh@gmail.com)
- replace sprintf by snprintf (silence warning by macOS compiler)
  (fduncanh@gmail.com)
- update README to show R Pi 3 model B+ testing (fduncanh@gmail.com)
- fix for homebrew on M1 macs (fduncanh@gmail.com)
- add --help -help -? synonyms for -h; hint if option is unknown
  (fduncanh@gmail.com)
- README fixes (fduncanh@gmail.com)

* Thu Feb 16 2023 laolux <25555671+laolux@users.noreply.github.com> 1.63-1
- README fixes (fduncanh@gmail.com)
- fix timestamp_to_date, etc. for nanosecond timestamps (fduncanh@gmail.com)
- README updated for 1.63 (fduncanh@gmail.com)
- introduce -vsync, -async options (fduncanh@gmail.com)
- add remote_clock_offset to convert remote timestamps to local REALTIME
  (fduncanh@gmail.com)
- remove video/audio _start_time and base_time additions (fduncanh@gmail.com)
- cleaned up raop_rtp.c (fduncanh@gmail.com)
- add gst_start_time (fduncanh@gmail.com)
- raop_ntp cleanup parentheses (fduncanh@gmail.com)
- export both local and remote ntp times with audio and video frames
  (fduncanh@gmail.com)
- add pipeline base_time, start_time variables (fduncanh@gmail.com)
- add change statement: authorship, dates to LGPL v2.1 files
  (fduncanh@gmail.com)
- Add modification date, authorship notices to GPLv3 files (fduncanh@gmail.com)
- improved debug output for timings (fduncanh@gmail.com)
- add a -sync option to activate server-client sync in audio-only mode
  (fduncanh@gmail.com)
- remove unnecessary "audio delay" feature. (fduncanh@gmail.com)
- cleanups of initial latency code. ntp and rtp times (fduncanh@gmail.com)
- v1.63: fix audio sync with client video in Audio-only mode
  (fduncanh@gmail.com)
- use rtp_clock_rate instead of rtp_sync_scale (fduncanh@gmail.com)
- convert all times from micro to nano secs (fduncanh@gmail.com)
- revert use of TIME_MONOTONIC back to TIME_REALTIME (fduncanh@gmail.com)
- README edits about macPorts build of GStreamer (fduncanh@gmail.com)
- CMake adjustments for macOS (fduncanh@gmail.com)
- README update (fduncanh@gmail.com)
- remove unused memalign.h (fduncanh@gmail.com)
- remove use of obsolete gettimeofday (fduncanh@gmail.com)

* Mon Jan 23 2023 laolux <25555671+laolux@users.noreply.github.com> 1.62-1
- Automatic commit of package [uxplay] release [1.61-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.60-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.56-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.55-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.47-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46b-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46-1].
  (25555671+laolux@users.noreply.github.com)
- Initialized to use tito. (25555671+laolux@users.noreply.github.com)
- Revert default maxFPS back from 60 to 30. (fduncanh@gmail.com)
- minor README update (fduncanh@gmail.com)
- cleanup of the gstreamer audio and video PTS system (fduncanh@gmail.com)
- update deprecated gstreamer syntax (fduncanh@gmail.com)
- README  update Changelog for v1.62 (fduncanh@gmail.com)
- cleanups in X11 UxPlay window  detection, add fpsdisplaysink to list
  (fduncanh@gmail.com)
- increase default maxFPS plist setting from 30 to 60 (fduncanh@gmail.com)
- README: add instruction for avahi service on non-systemd systems
  (fduncanh@gmail.com)
- remove unnecessary audio buffer flush on volume change (may cause audio
  artefacts) This was first introduced in RPiPlay 2019-07-12 in commit https://
  github.com/FD-/RPiPlay/commit/ad0872961fc34c3b86eae1ba08e6b820f5ff10bc
  (fduncanh@gmail.com)
- cleanup: use fprintf to stderr for error exits from option parser
  (fduncanh@gmail.com)
- cleanup: remove some printf's (replace by logger) (fduncanh@gmail.com)
- uxplay 1.62: add audio-only mode time offset option -ao x.y
  (fduncanh@gmail.com)
- some more dmap codes (fduncanh@gmail.com)
- option -ad n to add delay n millisec to ALAC streams (undocumented)
  (fduncanh@gmail.com)
- fixes in README (fduncanh@gmail.com)
- Rearrange and update README with "repology" info. (fduncanh@gmail.com)
- Windows: UTF-8 on console; fix 0x01 video packets with no payload
  (fduncanh@gmail.com)
- uxplay.cpp: cleaner shutdown (fduncanh@gmail.com)
- lib/CMakeLists.txt: remove -U_FORTIFY_SOURCE from Cflags (fduncanh@gmail.com)
- UxPlay 1.61 remove -t option and CMakeList.txt fixes; refactor uxplay.cpp
  (fduncanh@gmail.com)

* Fri Dec 30 2022 laolux <25555671+laolux@users.noreply.github.com> 1.61-1
- UxPlay 1.61 remove -t option and CMakeList.txt fixes; refactor uxplay.cpp
  (fduncanh@gmail.com)
- uxplay.cpp remove redundant declarations (fduncanh@gmail.com)
- uxplay.cpp move dnssd items to above start_raop_server (fduncanh@gmail.com)
- uxplay.cpp move main program to end of file (fduncanh@gmail.com)
- refactor start_raop_server to separate start_dnssd (fduncanh@gmail.com)
- update README: avahi configuration (fduncanh@gmail.com)
- postpend (instead of prepend) any $CFLAGS from build environment to Cflags
  (fduncanh@gmail.com)
- lib/CMakeLists.txt: remove debug option -g from Cflags (fduncanh@gmail.com)
- add modified instructions for Fedora (fduncanh@gmail.com)
- README update for new behavior if DNS_SD  registration fails
  (fduncanh@gmail.com)
- cosmetic change (keep lib free of UxPlay mentions in case of re-use) make
  NOHOLD feature a #define item (fduncanh@gmail.com)

* Wed Dec 21 2022 laolux <25555671+laolux@users.noreply.github.com> 1.60-1
- 1.60 release (fduncanh@gmail.com)
- added cmake message that -DZOOMFIX=ON is no longer used (fduncanh@gmail.com)
- add code to detect unsupported AirPlay 2 "Remote Control" protocol
  (fduncanh@gmail.com)
- add error message if dnssd_register_airplay or _raop fails
  (fduncanh@gmail.com)
- corrected parsing of DMAP metadata (fduncanh@gmail.com)
- minor cosmetic fix (fduncanh@gmail.com)
- Changelog for 1.59, add initial terminal message with uxplay version
  (fduncanh@gmail.com)
- dont report sizes if option -vs 0 is used (fix prevents segfault)
  (fduncanh@gmail.com)
- yet another new fullscreen code cleanup (fduncanh@gmail.com)
- dmap "code: should be called dmap "tag" (fduncanh@gmail.com)
- minor cleanup of new fullscreen code (fduncanh@gmail.com)
- more fixes of fullscreen toggle so -fs also works for X11
  (fduncanh@gmail.com)
- CMakeLists.txt: update to use X_DISPLAY_FIX by default (fduncanh@gmail.com)
- fixes to new full-screen toggle code (fduncanh@gmail.com)
- add F11 shortcut to toggle into fullscreen mode (gerbon@gerbon-HP-
  EliteDesk-800-G4-SFF)
- uxplay.cpp: cleanup handling of DMAP/DAAP AirPlay-audio metadata
  (fduncanh@gmail.com)
- update README (fduncanh@gmail.com)
- remove (show in -d mode only) terminal messages about connections +edits to
  README (fduncanh@gmail.com)
- update llhttp to v8.1.0 (fduncanh@gmail.com)
- add -nohold option: drop current client when new client connects
  (fduncanh@gmail.com)
- README updates (fduncanh@gmail.com)
- rearrange previous commit (avoid exit with active logger)
  (fduncanh@gmail.com)
- UxPlay 1.57 (fduncanh@gmail.com)
- more graceful exit if required GStreamer plugins are missing
  (fduncanh@gmail.com)
- do not call ISSET with invalid mirror_data_sock = -1. (prevents  Archlinux
  coredump with CFLAGS = -DFORTIFY_SOURCE) (fduncanh@gmail.com)
- ignore ZOOMFIX request if GStreamer >= 1.20 (fduncanh@gmail.com)
- add fullscreen-toggle-mode=alt-enter to -vs d3d11videosink
  (fduncanh@gmail.com)
- Add missing LGPL headers (fduncanh@gmail.com)
- README: add info about fullscreen mode on Windows (fduncanh@gmail.com)
- correct incorrect UDP port for -p in Troubleshooting (fduncanh@gmail.com)
- minor cleanup of parsing for -admp, -vdmp options (fduncanh@gmail.com)
- iPod Touch gen 5 and later is supported; iOS 16 supports UxPlay
  (fduncanh@gmail.com)
- Update README: Raspberry Pi OS no longer needs a patch (fduncanh@gmail.com)
- changes to README for windows build (fduncanh@gmail.com)
- WIN32 audio updates, README and manpage added audioresample to audio pipeline
  for WIN32 (fduncanh@gmail.com)
- add WIN32 code for finding system MAC address don't buffer stdout in WIN32
  when debug_log=false (fduncanh@gmail.com)
- update README for building on Windows (thanks to @aelmod)
  (fduncanh@gmail.com)
- modified keepalive settings for WIN32 (fduncanh@gmail.com)
- CMakeLists.txt: add WIN32 compilation (from @aelmod) (fduncanh@gmail.com)
- uxplay.cpp: fixes by @aelmod for compilation on Windows (fduncanh@gmail.com)
- raop airplay lib: fixes by @aelmod for compilation on Windows
  (fduncanh@gmail.com)
- uxplay.cpp: small cleanup; also remove unused WIN32 code in lib/threads.h.
  (fduncanh@gmail.com)
- revert a change that used assert in a way that fails with NDEBUG (pointed out
  by @heweishing, thanks) (fduncanh@gmail.com)
- README edits + cosmetic changes to manpage, -h output (fduncanh@gmail.com)

* Mon Aug 01 2022 laolux <25555671+laolux@users.noreply.github.com> 1.56-1
- Automatic commit of package [uxplay] release [1.55-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.47-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46b-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46-1].
  (25555671+laolux@users.noreply.github.com)
- Initialized to use tito. (25555671+laolux@users.noreply.github.com)
- remove -bt709 from -rpi etc. add -rpigl convenience option
  (fduncanh@gmail.com)

* Fri Jul 29 2022 laolux <25555671+laolux@users.noreply.github.com> 1.55-1
- Automatic commit of package [uxplay] release [1.47-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46b-1].
  (25555671+laolux@users.noreply.github.com)
- Automatic commit of package [uxplay] release [1.46-1].
  (25555671+laolux@users.noreply.github.com)
- Initialized to use tito. (25555671+laolux@users.noreply.github.com)
- fix inconsistent argument in video_renderer_flush reported by PetrusZ #111
  (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- update llhttp to v6.0.7; README typo. (fduncanh@gmail.com)
- use g_assert instead of assert in renderers (fduncanh@gmail.com)
- minor change: -v for version info only, -h for help text (fduncanh@gmail.com)
- update README for 1.55 (fduncanh@gmail.com)
- add -bt709 option for the bt709 fix (for future gstreamer changes) -v4l2 now
  does NOT include the -bt709 fix, use -v4l2 -bt709 . -rpi -rpifb -rpiwl still
  include  the bt709 fix for v4l2 on RPi (fduncanh@gmail.com)
- typo 1.53 instead of 1.54 on manpage (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- separate RAOP and AirPlay features (fduncanh@gmail.com)
- support for display of cover art in AirPlay Audio-only (ALAC) mode
  (fduncanh@gmail.com)
- make features in plist from raop_handlers.h consistent with dnssdint.h
  (fduncanh@gmail.com)
- move bt709 fix to -v4l2 and -rpi* options, instead of Caps for all.
  (fduncanh@gmail.com)
- only start processing resent audio  packet if length >=12
  (fduncanh@gmail.com)
- send uint64_t rtp_time to sync_clock (without subtraction of rtp_start_time)
  (fduncanh@gmail.com)
- remove assertion in  rtp64_time (fduncanh@gmail.com)
- fir minor typo in comment (fduncanh@gmail.com)
- send uint64_t ntp_times to raop_rtp_sync_clock without subtracting
  ntp_start_time (fduncanh@gmail.com)
- add seqnum to audio_decode_struct (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- cleaner implementation of 32->64 bit rtp_time (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- raop_rtp.c more code cleanup in audio rtp_sync (fduncanh@gmail.com)
- start rtp64_time at a sync event if it happens before audio is received
  (fduncanh@gmail.com)
- remove sync_scale (now unused) from raop_rtp_t (fduncanh@gmail.com)
- cosmetic (typo in comment) (fduncanh@gmail.com)
- cosmetic cleanups to recent changes in raop_rtp.c (fduncanh@gmail.com)
- prepare for v 1.53, remove "have_synced" from audio data structure.
  (fduncanh@gmail.com)
- make arguments to rtp32_to_64time const (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- cleanup initial audio sync; now use 64-bit rpt time to avoid epoch issues
  (fduncanh@gmail.com)
- whitespace and cosmetic cleanups (fduncanh@gmail.com)
- code cleanup in raop_rtp.c (uint32 issues) (fduncanh@gmail.com)
- cleanup resent data code in raop_rtp.c (fduncanh@gmail.com)
- cleanup in raop_rtp.c for unusual  control and data packets
  (fduncanh@gmail.com)
- simplified call to raop_buffer_enqueue: packet contains rtp_timestamp
  (fduncanh@gmail.com)
- small cleanup in raop_rtp.c (fduncanh@gmail.com)
- fix for too-short resent audio packets crash reported by @ephemient
  (fduncanh@gmail.com)
- update README (fduncanh@gmail.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit  README (fduncanh@gmail.com)
- mirror_buffer.c: comment out unused variable outputlength
  (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edit README (fduncanh@gmail.com)
- edit README, remove "Improvements" section (fduncanh@gmail.com)
- README: Remove FD- 's note on Airplay protocol, replace with link to
  original. (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edi README (fduncanh@gmail.com)
- edit READMR (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- README fix typo (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- README edits (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- added support for display of ALAC audio metadata on the terminal
  (fduncanh@gmail.com)
- README minor correction (fduncanh@gmail.com)
- updated README (fduncanh@gmail.com)
- add --define-prefex option to pkg-config on macOS (needed by new GStreamer
  builds) (fduncanh@gmail.com)
- initialze gstreamer once only, check for videoparsersbad plugin
  (fduncanh@gmail.com)
- cosmetic: tidy up error message  "Internal data stream error"
  (fduncanh@gmail.com)
- README fix typo (fduncanh@gmail.com)
- README fix typo (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- update README (current iOS = 15.4) (fduncanh@gmail.com)
- fix typo in comment added in last commit (fduncanh@gmail.com)
- add explanatory comment about when the SPS+PPS NAL is prepended to current
  NAL (fduncanh@gmail.com)
- remove unnecessary assertion about packet[5] (fduncanh@gmail.com)
- update ChangeLog in README (fduncanh@gmail.com)
- typo in comment (fduncanh@gmail.com)
- set shift to 0 as default for ALAC (fduncanh@gmail.com)
- fix typo in message (fduncanh@gmail.com)
- small change in format label (fduncanh@gmail.com)
- cleaner error message handling (fduncanh@gmail.com)
- fix small memory leak (from valgrind) (fduncanh@gmail.com)
- fix typo in last commit (fduncanh@gmail.com)
- initialize pointers for coverart dacp_id etc. (fduncanh@gmail.com)
- destroy raop_ntp after  rtp and rtp_mirror (fduncanh@gmail.com)
- nullify freed address in buffer (fduncanh@gmail.com)
- one more plist=-not-freed memory leak fix (fduncanh@gmail.com)
- fix yet more  plist not-freed memory leaks (fduncanh@gmail.com)
- fix some plist not-freed memory leaks (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- fix small memory leak (ekey, eiv) in raop_handlers.h (fduncanh@gmail.com)
- make more audio time details available to renderer (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- place more complete timing data in audio_decode_struct (fduncanh@gmail.com)
- fix broken -rpi option (broken by typo) (fduncanh@gmail.com)
- fix a corrupted first line from last commit (fduncanh@gmail.com)
- cosmetic changes (fduncanh@gmail.com)
- whitespace cleanup (fduncanh@gmail.com)
- cleanups of debug text and initial audio syc (fduncanh@gmail.com)
- clean up debug output (fduncanh@gmail.com)
- rename aac_decode_struct to audio_decode_struct and cosmetic fixes
  (fduncanh@gmail.com)
- cleanup of initial audio synchronization (fduncanh@gmail.com)
- activate resend in raop_rpt, add "compression type"  ct to raop_rtp_t
  (fduncanh@gmail.com)
- clean up initial timestamp of audio stream, before first sync event
  (fduncanh@gmail.com)
- rtp time wraps around uint32_t  after 27 hours! (fduncanh@gmail.com)
- subtract off start times from rpt and ntp timestamps (fduncanh@gmail.com)
- store rtp_timestamp, not ntp_timestamp, in audio buffer (fduncanh@gmail.com)
- part of last revert (fduncanh@gmail.com)
- revert previous 3 commits (fduncanh@gmail.com)
- typo in comment (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- make initial video timestamp available (fduncanh@gmail.com)
- save remote timestamp of start of video stream (fduncanh@gmail.com)
- initialize conn->raop_rtp_mirror to NULL (fduncanh@gmail.com)
- extra info in debug for time sync (fduncanh@gmail.com)
- next_rtp is not needed in time sync (fduncanh@gmail.com)
- cosmetic (typo in comment) (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- identify meaning of rtp_next in time synchronization (fduncanh@gmail.com)
- correct some comments (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- add some comments about packet structure (fduncanh@gmail.com)
- cleanup (cosmetic) and add defaults to switches (fduncanh@gmail.com)
- whitespace cleanup (fduncanh@gmail.com)
- small cleanup of appsrc construction. (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- cleanup of leftover -rpi option (fduncanh@gmail.com)
- increase version to 1.51 (fduncanh@gmail.com)
- update for uxplay 1.51 rearranged rpi options (fduncanh@gmail.com)
- revert commit 5efcf01 of March 12, 2020 This breaks reconnection after "stop
  streaming" is sent by client. It was intended to aid reconnection if a
  network interruption left a socket blocked.   Some other fix for that issue
  will be needed. This is connected to issue  #58 (fduncanh@gmail.com)
- restrict audio formats to AAC-ELD and ALAC (only ones ever seen)
  (fduncanh@gmail.com)
- cosmetic (clarify a comment) (fduncanh@gmail.com)
- fix typo in README (fduncanh@gmail.com)
- edit README for 1.50 release (fduncanh@gmail.com)
- edited README (fduncanh@gmail.com)
- move init_sockets to proper place in file (fduncanh@gmail.com)
- whitespace cleanup (fduncanh@gmail.com)
- rework to keep PPS and SPS data longer (trying to fix issue #87)
  (fduncanh@gmail.com)
- resore debug output of each nalu type (fduncanh@gmail.com)
- cleanup debug output (fduncanh@gmail.com)
- correct value of nal_type, check "forbidden zero bit" at start of nalu
  (fduncanh@gmail.com)
- cleanup writing of h264 nal start code (fduncanh@gmail.com)
- move colorimetry=bt709 to video caps set in video_renderer_gstreamer.c
  (fduncanh@gmail.com)
- whitespace/cosmetic (fduncanh@gmail.com)
- correct a comment (fduncanh@gmail.com)
- make -rpi be the option for framebuffer on RPi (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- modifiy RPATH setting for macOS (fduncanh@gmail.com)
- update for 1.50: added -fs -rpigl -rpiwl -rpifb options (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- replace GST_BUFFER_DTS by GST_BUFFER_PTS (fduncanh@gmail.com)
- set h264 "type"  to nal_count (fduncanh@gmail.com)
- remove unneeded line (fduncanh@gmail.com)
- minor changes to debug output and comments about contents of "packet"
  (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- whitespace cleanup (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- README fix typo (fduncanh@gmail.com)
- fix typo that broke code (fduncanh@gmail.com)
- edit READEME typo (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edit README (fduncanh@gmail.com)
- README edit (fduncanh@gmail.com)
- README edits (fduncanh@gmail.com)
- whitespace cleanup (fduncanh@gmail.com)
- fixed M1 video problem (fduncanh@gmail.com)
- add @RPATH /Library/Frameworks for macOS GStreamer (fduncanh@gmail.com)
- uxplay.cpp fix missing variable in err  message (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- minor README edits (fduncanh@gmail.com)
- fix typo in comment (fduncanh@gmail.com)
- README fix typo (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edit README (cosmetic) (fduncanh@gmail.com)
- Edit README (fduncanh@gmail.com)
- whitespace and cosmetic fixes (fduncanh@gmail.com)
- add options to dump video or audio to file (fduncanh@gmail.com)
- video_renderer_gstreamer.c: add caps (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- raop_rtp_mirror.c: add sps and pps to debug ouput (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- typo in README (fduncanh@gmail.com)
- EDIT README (for gstreamer-1.20.1) (fduncanh@gmail.com)
- README typo (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edited README to point to wiki patching instructions (fduncanh@gmail.com)
- revert last change (fduncanh@gmail.com)
- Update README.md (72711181+fduncanh@users.noreply.github.com)
- README edit (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edits to manpage and help message about kmssink (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- edited README (fduncanh@gmail.com)
- fix historic bug whene socket closes (fduncanh@gmail.com)
- restore LOGGER_DEBUG level for TEARDOWN reports (fduncanh@gmail.com)
- corrections to Teardown sequence (fduncanh@gmail.com)
- cleanup in teardown calls (fduncanh@gmail.com)
- cleanup of free'd raop dnssd render_logger (fduncanh@gmail.com)
- silence first ntp timeout notice when client is sleeping (fduncanh@gmail.com)
- improved debug message (fduncanh@gmail.com)
- better debug message (fduncanh@gmail.com)
- raop_rtp_mirror, make two debug messages distinguishable (fduncanh@gmail.com)
- UxPlay 1.48; Edited README for release (fduncanh@gmail.com)
- update README with R Pi news (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- typo in README (fduncanh@gmail.com)
- adjust pkg-config path for self-built gstreamer in /usr/local
  (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- fix typo in README (fduncanh@gmail.com)
- updates for R Pi support (fduncanh@gmail.com)
- use glimagesink for r pi (fduncanh@gmail.com)
- README typo in section on R Pi (fduncanh@gmail.com)
- update README about R Pi (fduncanh@gmail.com)
- add back undocumented -rpi option (improved, work in progress)
  (fduncanh@gmail.com)
- edit REASDME (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- remove -rpi option (it was premature to add it) (fduncanh@gmail.com)
- fix typo in CMakeLists.txt output message (fduncanh@gmail.com)
- typo in README (fduncanh@gmail.com)
- fixe typo in README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- add option for modifying h264parse in video pipeline (fduncanh@gmail.com)
- small tweak to CFLAGS -march=native support (fduncanh@gmail.com)
- add cmake option -DNO_MARCH_NATIVE=ON to remove -march=native from CFLAGS
  (fduncanh@gmail.com)
- CMakefile.txt rearrangement (fduncanh@gmail.com)
- modify C_MAKE_CFLAGS so -march=native is only used with x86 and x86_64
  compiles (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- glimagesink is not required for  RPi hardware h264 decoding
  (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- edited README (fduncanh@gmail.com)
- README small edit (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- minor README edit (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- Edit README (fduncanh@gmail.com)
- edits README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- edits to README (fduncanh@gmail.com)
- added -rpi option for Raspberry Pi video with GPU h264 decoding
  (fduncanh@gmail.com)
- edited -v and manpage help options (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- edit README (fduncanh@gmail.com)
- README edits (fduncanh@gmail.com)
- uxplay 1.48 make video pipeline configurable for hardware h264 decoders
  (fduncanh@gmail.com)
- undocumented option -nvdec for NVIDIA hardware h264 decoding
  (fduncanh@gmail.com)
- clarify last commit (fduncanh@gmail.com)
- complete previous commit (fduncanh@gmail.com)
- raop_rtp_mirror.c: add an error message when thread exits b/c running=false
  (fduncanh@gmail.com)
- make sourceVersion = GLOBAL_VERSION from global.h and other cleanups
  (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- byteuils used in cleanup (fduncanh@gmail.com)
- cleanup to use byteutils in raop_rtp.c (fduncanh@gmail.com)
- make -avdec always use videoconvert (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- make video pipeline more configurable (fduncanh@gmail.com)
- undocumented -v4l2  option for Raspberry Pi (fduncanh@gmail.com)
- add INFO message just before GStreamer starts streaming. (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- cosmetic, for consistency (fduncanh@gmail.com)
- whitespace (fduncanh@gmail.com)
- add timestamp_to_time for raop_ntp timeout reports; read remote cport from
  plist (fduncanh@gmail.com)
- Edits (fduncanh@gmail.com)
- README edits (Arch) (fduncanh@gmail.com)

* Thu Feb 10 2022 laolux <25555671+laolux@users.noreply.github.com> 1.47-1
- Automatic commit of package [uxplay] release [1.47].
  (25555671+laolux@users.noreply.github.com)
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
