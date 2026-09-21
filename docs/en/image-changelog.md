# DLTNG image changelog

## 10.0.0-rc.4-upgrade.2-clean-update – 2026-09-21

- New full pilot image retaining the local boot console. Company-LAN DHCP and the static service address coexist; networking starts before the maintenance display.
- Updated device display after completed downloads and during backup preparation. Requires Upgrade app 0.2.10.
- Filesystems, ARM64 applications, boot console, full decompression and checksums verified. Compressed size 992,888,644 bytes; raw size 4,647,288,832 bytes.
- Compressed-file SHA256: f69b04015cba117882dc69bc4a4b7431d66163a36aa4abb9f3f7ce4d28db4716.
- Signed UPS approval checked for the registered 32-GB pilot device, including download authorization and resumable byte ranges. The three earlier faulty pilot approvals were revoked.
- Targeted boot/network correction is confirmed on the test device. First boot of this newly built image, complete migration and 16-GB acceptance remain pending. No general customer approval.

## Unreleased – 2026-09-18: Startup and reconnection

- Identified and corrected a startup fault in the image recipe: a local boot console must remain available when the serial interface is disabled. Without it, the device can stop before the display and network start.
- Two physical reboots on the 32-GB test device verified the fix, regular maintenance display, network and session proof. The original kernel and startup files remain in use; temporary diagnostics were removed.
- The service network profile will retain both DHCP for the company LAN and the static service address for a direct cable. The app also tries the previously known LAN address when reconnecting.
- **No new image or EXE has been published.** Existing downloads do not yet contain these changes. First boot of a rebuilt image, complete data restoration and the 16-GB variant still require validation. See [troubleshooting](troubleshooting.md) for step 09.

## Upgrade helper 0.2.8 – 2026-09-17

Fullscreen overlay with progress and verified visibility. Tested on the original-1.0 device. Published images and UPS approvals remain unchanged; the app refreshes the helper after device/session verification. Future image builds will include it.

This history includes earlier migration images as well as the clean profile used by DLTNG Upgrade. Statements in historical entries refer to the respective image. The Windows application has its [own changelog](changelog.md).

## 10.0.0-rc.4-upgrade.1-clean-update – 2026-09-17

- Persistent BUSY status and a separate maintenance display from session-verified startup. German/English stages; business services remain inhibited until final checks. Requires Upgrade test build 0.2.7 or later.
- Image built: 993,321,032 bytes compressed, 4,647,288,832 bytes raw. ARM64 applications, boot files, partitions, FAT/ext4, complete decompression and checksum comparisons passed. Maintenance display also tested under Linux at 480 × 320 pixels.
- Compressed-file SHA256: `dbd63f07cadd6de650a3478fc1983032a89be46d70552489d880a2e5448ef806`.
- Physical CM4/display acceptance remains pending. Previous images remain unchanged; no general customer approval.

## Upgrade helper 0.2.3 – 2026-09-16

Legacy NFC build and uWSGI logs are archived and restored. Existing image files and UPS approvals remain unchanged. The app installs the revised helper after device/session verification.

## Pilot delivery – 2026-09-16

- Additional signed approval for the assessed original image with application version `1`/`1.0`, requiring the separate 0.2.2 test build. Image bytes are unchanged; the app supplies the updated backup/migration helper after session verification.
- Isolated database, file and configuration restoration passed; physical acceptance remains pending. Older upload files without reliable receipts require Offline mode.
- The clean image from 15 September is delivered unchanged through UPS for an explicitly registered CM4 test device.
- Signed manifest with an expiry date and a separate Upgrade 0.2.1 test build. Approval is bound to the test device, 32 GB hardware profile and source version.
- The initial pilot accepts source versions 9.5, 10.0.0-rc.3 and 10.0.0-rc.4. Additional approval with Upgrade 0.2.2 also supports the assessed 1.0 profile.
- No general hardware or customer approval. See [Pilot test](pilot.md) for the procedure and outstanding checks.

## 10.0.0-rc.4-startup.1-clean-update – 2026-09-15

- Separate clean profile for reinstallation followed by customer-data restoration. Reference settings, logos, reports, data files and SQL dumps are excluded.
- Persistent maintenance state, session-bound startup configuration, service network and device identity proof.
- Device helper for backup, restoration, network rollback and final checks; business services remain paused until successful completion.
- Complete image built: 991,882,668 bytes compressed and 4,647,288,832 bytes raw. ARM64 web processes, both exported startup images, FAT/ext4 and full decompression/checksum comparison passed.
- Build recipe `0cb6f9a`; corrected final verification `20e54c1`. Startup graphics are checked on the delivered boot partition because pi-gen creates the final startup files during export.
- Physical CM4 boot, 16/32 GB migration, power-loss recovery and actual recovery-image boot remain pending. No customer approval or production image signature.

## 10.0.0-rc.4-startup.1 – 2026-09-15

- Show the existing blue startup screen in the kernel, with left-aligned “DLTNG STARTET …” text and normal/rotated graphics in initramfs.
- Full-screen intermediate display during Xorg/Chromium startup. Starts independently of nginx; the helper exits when the full-screen browser appears.
- Suppress the firmware rainbow, local boot console and systemd status output during normal startup; retain SSH and logs.
- Separate image tag and delivery folder; all three applications retain their rc.4 commits. Previously published images remain unchanged.
- Configuration, graphics and X11-transition tests; real display and boot-time acceptance still required. Technical details are maintained in the image project's `STARTUP.md`.

## Build tools after 10.0.0-rc.4

- When reusing build directories, select the raw image using the current compressed export's filename. Older raw images are retained and the complete SHA-256 comparison remains in place. The published rc.4 file and version marker are unchanged.

## 10.0.0-rc.4 – 2026-09-15

- Transfer the confirmed SFTP/port-22 reference configuration into the migration image; retain the original private backup unchanged.
- Common rc.4 build containing all hotfixes verified after rc.3, persistent diagnostic history and a separate support service running as `pi`.
- Generate device keys on the target module only; no device key in the image. Diagnostic storage stays within the log budget; restoration takes existing history into account.
- Sanitized manual UPS packages, checked AI recommendations, separate maintenance contracts and a company-wide annual quota; technical details in the image project's `DIAGNOSTICS.md`.
- Physical one-second-response and 72-hour acceptance remain pending; software tests do not constitute hardware approval.
- Silent upload timer: an additional rc.3 hotfix suppresses timer-related display and busy messages. Exclusive processing, error logging, confirmed transfers and visible smartcard/USB processing remain. Existing image files and packages are unchanged.
- Smartcard correction for rc.3: create the missing work directory in the image and check it during the build. Separate package for safe file creation, one upload after a successful read and exclusive use until card removal; error, restart and USB regression cases checked. Existing images are unchanged.
- rc.3 display correction: a separate hotfix moves RAM information to System Information and removes duplicate CPU temperature from the LAN page. German/English and installed code checked on CM4; the published image is unchanged.
- Login/redirects: custom nginx/uWSGI parameters preserve the normalized hostname and local port 8888 or 12005. The distribution's previous default passed only the hostname and redirected logins to unused port 80. Canonical redirects for both applications are now checked for same-origin behavior during image runtime testing.
- Kiosk: “DLTNG startet …” startup text. Keyboard icon fixed at the bottom right with a 12-pixel gap; moving/resizing disabled and position calculated from actual screen geometry. Separate supplementary rc.3 hotfix.
- Follow-up rc.3 correction: enable GNOME accessibility before Onboard so the on-screen keyboard appears automatically without a prompt. Provided as a separate hotfix together with the NFC-service correction, persistent error display and left-aligned status messages.
- Kiosk startup correction for rc.3: explicitly retain `libglib2.0-bin` as a runtime package. Its `gsettings` command was missing after package cleanup and ended the graphical session before browser startup. Corrected on a CM4 with 4 GB RAM; the user confirmed the DLT display.
- On-screen keyboard: explicitly install the required GNOME schemas, AT-SPI bus and Atspi typelib and verify actual imports.
- Capture kiosk output in the system journal. Stop the graphical session explicitly so a manual restart does not wait 90 seconds for remaining graphics processes. Final checks verify kiosk programs and actual ARM64 settings keys; separate hotfix script for existing rc.3 installations. Published images are unchanged.
- Verification tool: inspect disabled EEPROM-service links themselves without resolving absolute links outside the checked filesystem. The already-built rc.2 image is unchanged.

## 10.0.0-rc.3 – 2026-09-15

- Common rc.3 build with exclusive device processing, preserved display text file and independent 100 ms status access through nginx.
- USB mount management, FAT/exFAT/NTFS support and limited system helpers for release and display rotation; desktop automount suppressed.
- Dedicated kiosk user without administrator groups, Chromium sandbox, restricted Openbox session, on-screen keyboard and early startup display; graphical recovery independent of active imports.
- Automatic package checks/installations and system notifications disabled; manufacturer application updates retained.
- Backup includes transfer acknowledgements and conflict files; restoration preserves current pending transfers and adds existing acknowledgements.
- Isolated regression tests and browser measurements added; physical media response, USB-port mapping, touch, boot-time comparison and 72-hour acceptance on CM4 2 GB/16 GB remain pending.

## 10.0.0-rc.2 – 2026-09-14

- Configurable LAN speed and EEE with rollback timer, restoration after restart and status display in DLT web configuration. Image defaults: automatic speed, EEE off.
- Hardware diagnostics for temperature, RAM, undervoltage, throttling and the EEPROM shutdown setting.
- Raspberry Pi diagnostic tools and their device-tree dependency are retained during package cleanup and checked in the completed image.
- Optional CM5 test profile for the existing CM4 carrier: official 2712 kernel, RP1 I²C6 on GPIO38/39 as `/dev/i2c-10`, external PCF85063A RTC and PN7150. CM4 remains the default.
- CM5 test profile initially limits CPU speed to 1.5 GHz and loads no fan controller. No CM5 hardware approval; GPIO_VREF remains a separate electrical finding.
- Publication tool: explicitly read GitHub responses as UTF-8 so special characters work with the Windows default encoding. Additional regression test; the built image is unchanged.

## 10.0.0-rc.1 – 2026-09-14

- Common version number and release tags for all three applications and the image.
- Dedicated private image repository, pinned application commits and version display independent of restored settings.
- Private GitHub download with SHA-256 verification and additional QNAP backup per version.
- Raspberry Pi OS Lite Trixie, ARM64; new Python environments and rebuilt NFC/CCID components.
- CM4 with 2 GB RAM/16 GB eMMC defines resource budgets; the same image is intended for 4 GB/32 GB.
- NetworkManager, RTC/time corrections, bounded logs, serialized reports and safe data restoration.
- Hardware acceptance including a 72-hour test remains pending. No CM5 approval.

## Before version 10

- 2026-09-14: first CM4 Trixie test image built from frozen reference sources and migration patches, checked in software.
- This original image is archived unchanged under `archive-cm4-20260914`, including its original checksum.
- Earlier application versions and development history are documented in the changelogs of the three application repositories.
- Git histories remain unchanged. Local development with additional DLC features is retained in the respective `codex/development-10.1` branches.
