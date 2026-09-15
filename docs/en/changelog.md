# Upgrade tool changelog

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
