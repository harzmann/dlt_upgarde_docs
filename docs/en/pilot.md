# Prepare a pilot test

A separately configured test build, version 0.2.1 or later, can retrieve a signed lab image through UPS. Approval applies exclusively to registered CM4 serials until the specified expiry. General hardware approval stays disabled. The public standard download, version 0.2.0, does not contain this specific pilot configuration.

## Device administrator preparation

1. Read the actual CM4 serial, eMMC capacity and installed application version.
2. Register the device under the correct UPS customer and check its effective entitlement.
3. Provide a test build with the public signing key and this exact device serial.
4. Sign the matching image: hardware profile, permitted source versions, serial and expiry are covered by the signature.
5. Enable pilot operation in UPS, import the image and select **“Approve for these test devices”** (German UI: **“Für diese Testgeräte freigeben”**).
6. Check downloads, checksums and rejection of other devices without pausing or flashing the device.

## Starting from version 1.0

**The separate 0.2.2 pilot build supports a direct test from the assessed original 1.0 image.** `CM4_DLT_231119_V9_X.img` stores application version `1`. Debian 11, Python 3.9, configuration and the real MariaDB database were inspected. Isolated backup/restoration of 19 tables, six views, certificates and DDD/CSV fixtures passed, including repeated import. Physical-device acceptance remains pending.

Updating to 9.5 first is unnecessary for this pilot. The new signed approval requires Upgrade 0.2.2 or later. The previous 0.2.1 pilot executable and public standard download 0.2.0 do not support this direct path.

**If upload files exist:** Set transmission to **Offline** on the old device and review which files were already sent. Version 1 has no reliable transfer receipts. All files are backed up and restored; Offline remains active. Enable transmission only after reviewing the queue. The wizard never invents acknowledgements.

## Run the test

Use the supplied test executable; **“LAB”** appears at the top. Keep the complete device backup enabled and follow the [user guide](guide.md). The device administrator must confirm the boot-button and cable sequence on the actual carrier board. Record the serial, source/target versions, backup, result and recovery boot.

A successful pilot migration does not grant general approval for other devices or source versions.
