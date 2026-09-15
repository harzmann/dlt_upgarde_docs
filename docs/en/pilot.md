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

**Direct upgrading from DLTNG 1.0 has not been verified.** The application stops with `SRC-001` before installing a backup helper. The original image first needs assessment of its data layout, Python version and database migration.

The existing application update from 1.0 to 9.5 can be tested as a preparatory route. Its UPS download entitlement has been checked; actual installation and migration on the device remain pending. Start the image-upgrade test only after checking that version 9.5 is actually installed. Approving a version number alone does not replace migration assessment.

## Run the test

Use the supplied test executable; **“LAB”** appears at the top. Keep the complete device backup enabled and follow the [user guide](guide.md). The device administrator must confirm the boot-button and cable sequence on the actual carrier board. Record the serial, source/target versions, backup, result and recovery boot.

A successful pilot migration does not grant general approval for other devices or source versions.
