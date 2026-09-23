# Prepare a pilot test

A separately configured test build, version 0.2.1 or later, can retrieve a signed lab image through UPS. Approval applies exclusively to registered CM4 serials until the specified expiry. General hardware approval stays disabled. The public standard download, version 0.2.0, does not contain this specific pilot configuration.

## Fixes for the current test

**Use [test build 0.2.12](https://github.com/harzmann/dlt_upgrade/releases/tag/v0.2.12-pilot.1).** From the device check onwards, DLTNG displays the upgrade stage and **BUSY**. Smartcard, USB, RFID and uploads remain inhibited until verified release. The fixes from 0.2.6 remain included: resumable Windows helpers, **Back** to review completed steps, compact layout and **Diagnostics** with error-code explanations, a redacted ZIP and confirmed upload to UPS.

**Resume an existing session:** Keep the device connected while a helper is working. After it finishes, close the old EXE, start 0.2.12 and choose **“Open session”** with the current `session.json`. If multiple sessions exist, choose using their date, progress and folder; newest is listed first. Verified downloads and backups are retained. A successful saved write result leads directly to data restoration. If the original device resumed normal operation after backup, a fresh backup is required.

**Start over after reinstalling the original 1.0 image:** Boot DLTNG normally and wait until it is ready. Launch test build 0.2.12 and create a new session with a fresh backup; do not open an old `session.json`. Select a new persistent working folder and retain previous backup folders. Remove cards and USB storage before **“Check device”**. The app downloads the matching signed pilot image from UPS; the normal procedure does not require manual image selection.

New flashing requires **10.0.0-rc.4-upgrade.2-clean-update** and test build **0.2.12**. It retains the required boot console and DHCP alongside the service address. Do not reuse faulty earlier pilot images. A new EXE alone does not repair an already written old image; for a dark display, contact support for a targeted startup correction and retain the session. After that correction, the existing backup can be restored. Complete migration and 16-GB acceptance remain pending.

On an existing LAN, use the normal device connection. The direct service connection is intended for a dedicated Ethernet cable between the PC and DLTNG. The app requests administrator rights for the relevant Windows operation.

From 0.2.11, steps 01 and 05 show the current backup folder. In step 09, remove USB-Admin and restart as instructed, then click **Restore data**. Only that click starts automatic discovery. The IP field may remain empty; discovered addresses require device/session proof before transfers. [Discovery limits and USB networking](troubleshooting.md#discovery-limits-and-usb-admin).


In 0.2.11 every step names the next button. After reconnecting power in step 06, click **“Detect USB device”** at the bottom right. During operations, the PC wizard shows a blinking red **“UPGRADE IN PROGRESS - DO NOT POWER OFF!”** warning. It also remains active for uncertain write status; it is hidden for guided cable changes and restart.

## Starting from version 9.6

From **0.2.12**, the pilot supports assessed 9.6 application package revision 3. Discovery also shows identifiable DLTNGs whose version has no approved backup profile yet; “Check device” retains the compatibility gate.

After reinstalling or changing from 1.0 to 9.6, start a **new session with a fresh backup**. Do not reuse a session from a different installation; retain previous backup folders. The additional UPS approval applies to the registered 32-GB test device, exactly 9.6 and app 0.2.12 or later. Image upgrade.2 bytes are unchanged.

Read-only device inspection, discovery and backup preflight passed. Isolated restoration checked database rows, configuration, file hashes and repeated import; the full physical 9.6 upgrade remains pending. Legacy NFC settings are archived. Existing upload files without transfer receipts require Offline mode. The 9.6 USB wait setting is preserved, but target 10.x uses a different USB mounting implementation that currently does not consume this fixed wait setting.

## Device administrator preparation

1. Read the actual CM4 serial, eMMC capacity and installed application version.
2. Register the device under the correct UPS customer and check its effective entitlement.
3. Provide a test build with the public signing key and this exact device serial.
4. Sign the matching image: hardware profile, permitted source versions, serial and expiry are covered by the signature.
5. Enable pilot operation in UPS, import the image and select **“Approve for these test devices”** (German UI: **“Für diese Testgeräte freigeben”**).
6. Check downloads, checksums and rejection of other devices without pausing or flashing the device.

## Starting from version 1.0

**The current pilot build supports a direct test from the assessed original 1.0 image.** `CM4_DLT_231119_V9_X.img` stores application version `1`. Debian 11, Python 3.9, configuration and the real MariaDB database were inspected. Isolated backup/restoration of 19 tables, six views, certificates and DDD/CSV fixtures passed, including repeated import. Physical-device acceptance remains pending.

Updating to 9.5 first is unnecessary for this pilot. The current signed approval requires Upgrade 0.2.10 or later. The previous 0.2.1 pilot executable and public standard download 0.2.0 do not support this direct path.

**If upload files exist:** Set transmission to **Offline** on the old device and review which files were already sent. Version 1 has no reliable transfer receipts. All files are backed up and restored; Offline remains active. Enable transmission only after reviewing the queue. The wizard never invents acknowledgements.

## Run the test

Use the supplied test executable; **“LAB”** appears at the top. Keep the complete device backup enabled and follow the [user guide](guide.md). The device administrator must confirm the boot-button and cable sequence on the actual carrier board. Record the serial, source/target versions, backup, result and recovery boot.

A successful pilot migration does not grant general approval for other devices or source versions.
