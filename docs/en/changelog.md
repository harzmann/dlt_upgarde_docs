# Application changelog

### 0.2.3 – 2026-09-16 · Pilot fixes

- Deliver background-task completion to the UI thread, fixing intermittent crashes during step changes.
- Start the system helper from the actual portable EXE: USB driver and direct Ethernet setup no longer require a separate `python.exe`. Distinguish cancelled administrator prompts from launch failures.
- Readable inputs, selection lists and folder dialogs even with dark Windows settings; smaller connection illustration and scroll reset on step changes.
- Device discovery displays phases, progress and explicit results; shorter waits for unrelated SSH devices.
- Dedicated icon for the window, taskbar and executable.
- Archive and restore legacy NFC build and uWSGI logs; continue blocking unknown persistent data.
- Recheck device identity and refresh the backup helper when resuming a backup. Existing downloads and sessions remain usable.
- Package self-test launches the real helper read-only from the compiled EXE. Driver installation, network changes and physical flash/recovery tests remain part of hardware acceptance.

### 0.2.2 – 2026-09-16 · Original 1.0 image

- Separate profile for the original image's stored version `1`, plus `1.0`/`1.0.0`, Debian 11 and Python 3.9.
- Preserve old certificates, archive NFC configuration and correct development-machine paths for generated reports.
- Check the MariaDB schema before backup and after import; missing local database tools block backup. Pause FTP/SMB writers during backup.
- Require offline mode for older upload files without reliable receipts, preventing automatic retransmission caused by the upgrade.
- Rehearsed restoration of the actual original database, settings and certificates plus DDD/CSV fixtures, including repeated import. Physical-device acceptance remains pending.

### 0.2.1 – 2026-09-16 · Pilot preparation

- Signed pilot images delivered through UPS, bound to explicit CM4 serials and an expiry date.
- Lab notice in the UI and device identity checks before installing the backup helper.
- Read-only inspection of serial and source version; version 1.0 stops before changes with an actionable explanation.
- Additional scope, expiry and download-path tests. Direct migration from 1.0 and hardware acceptance remain pending.

### 0.2.0 – 2026-09-15

- Product renamed **DLTNG Upgrade**, executable `DLTNG-Upgrade.exe`, dedicated `dlt_upgrade` repository.
- German/English selection using a country-flag button at the top right; preference saved in the work folder.
- Language changes preserve the device session, inputs, confirmation and progress. Status, errors, dialogs and recovery screens are translated too.
- Bilingual MkDocs documentation and public Windows download in the `dlt_upgarde_docs` repository.
- Description, step-by-step guide, troubleshooting, application changelog and separate image changelog in both languages.
- Existing device/UPS protocol and shared flash lock remain compatible with the previous edition.
- Additional language, preference persistence, catalog coverage and demo tests. Still a development edition without hardware approval.

### 0.1.0 – 2026-09-15

- First portable PySide6 development edition with ten steps and a complete demo mode.
- Mandatory backup, optional eMMC backup, signed downloads, USB write verification, data restoration and recovery.
- Separate UPS image API and a clean CM4 test image prepared and checked in software.
- Five symbolic ImageGen illustrations. Physical-device and data-migration acceptance pending.
