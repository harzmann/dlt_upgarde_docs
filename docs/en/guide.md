# Step by step

This guide describes the intended workflow. You can try every step in **demo mode** in the current development edition. Actual flashing requires an explicitly approved device and a matching signed image.

This guide covers **test build 0.2.7**, including the new confirmation display, connector illustrations and Explorer suppression. The public standard download remains 0.2.0; the test build is supplied for the approved lab device.

## Before you start

- Use Windows 11 x64; connect one device per operation.
- Have the power supply, Ethernet cable and USB programming cable suitable for the DLTNG carrier board ready.
- Choose a local work folder with sufficient space. The image and optional complete device backup need several gigabytes in addition to the data backup; the complete copy alone is about 16–32 GB.
- Keep Internet access available for the image download. The complete image is downloaded and checked before backup. Business services pause when the device is checked.
- USB drivers and disk/network settings may require Windows administrator privileges.

## Choose your language

Click the **country flag and language name** at the top right and select **Deutsch** or **English**. **Alt+L** also opens the menu. You can switch during an operation without resetting progress or inputs. Your choice is saved in the work folder.

![Language selection and start page](assets/ui-en.png)

*Screenshot: test build 0.2.4 in demo mode.*

## 1 · Prepare

Start `DLTNG-Upgrade.exe`. Choose the work and backup folder if needed and use **“Set up USB driver”** when required. **“Check preparation”** checks the PC prerequisites. Select **“Try the demo”** to explore the workflow without changing a device.

## 2 · Connect device

Connect the PC and DLTNG to the same LAN. Enter the DLTNG IP address or select **“Find DLTNG on the network”**. **“Check device”** reads its identity, hardware and version.

Open **“Show direct cable connection options”** for additional settings. For a direct Ethernet cable, select the PC adapter used specifically for that connection. For a static device address, include the network prefix, for example `192.168.1.25/24`. For a DHCP device, limited assistance is available through **“Direct connection: find DLTNG without a static IP”**. Enable this only on a direct cable connection without a company network or switch.

## 3 · Download upgrade

Select **“Download upgrade”**. UPS checks device entitlement and the matching approved version. The application verifies the signature, size and checksums. Keep the Internet connection active until this step finishes.

Missing approval cannot be skipped. Lab devices require separate approval tied to their serial number.

## 4 · Choose backup

Check the backup folder. The mandatory data backup is always enabled. The additional **complete device backup** is selected by default and allows recovery of the original system. **“Use these settings”** confirms your choice.

## 5 · Back up data

Remove cards and USB storage devices and wait for active operations to finish. **“Back up data”** pauses relevant writers, creates the backup and transfers it to the PC. Only a completely verified backup permits the next step.

Known configuration, data files, local databases, transfer records and device identity data are included. Unknown persistent data stops the workflow for review. For external database servers, connection settings are retained; their data is not restored to the device.

![Symbolic DLTNG front based on the original photo](assets/dltng-front-v1.png)

## 6 · Prepare USB

Select **“Shut down device”**, wait until the display is completely off, then unplug power. Unplugging power is not a substitute for controlled shutdown. Then follow the **approved instructions for the actual carrier board** for its boot button and programming cable. Select **“Detect USB device”** afterwards.

### Identify the connectors

![DLTNG connectors based on the original photo, with numbers](assets/dltng-connectors-numbered.png)

From left to right:

| Number | Connector |
|---|---|
| 1 | Power supply, with black cable connected |
| 2 | RJ45 Ethernet / network, with blue cable connected |
| 3 | Two vertically stacked USB ports |
| 4 | HDMI |
| 5 | USB-Admin for the programming cable, with red cable connected |
| 6 | Recessed Admin pushbutton; can be pressed gently with a ballpoint pen |

In the app, **“Enlarge connector illustration”** opens the detailed view. The legend follows the selected language. These symbolic illustrations are based on the supplied photos of this DLTNG. The exact button, power and cable sequence still needs to be checked on the physical device using its instructions.

### Prevent the automatic Explorer window

Keep the wizard in the foreground during the USB steps. From test build **0.2.4**, it then suppresses automatic opening of the boot partition, including while viewing the enlarged connector illustration and during full-image recovery. No persistent Windows setting changes are required. Existing Explorer windows remain open. Demo mode does not suppress AutoPlay.

Windows sends this [AutoPlay query to the foreground window](https://learn.microsoft.com/en-us/windows/win32/shell/autoplay-reg). If another application is in the foreground, Explorer may still open.

## 7 · Confirm installation

Check the device identity, target version and backup status. For the correct device only, tick **“The device identity and backup are correct”**. A warning explains interruption, possible boot failure, own risk and User Account Control. The checkbox remains ticked only if you accept. This enables **“Continue to installation”**. That click opens step 8; it does not start writing yet.

![Visible confirmation in test build 0.2.6](assets/confirmation-en.png)

Without the checkmark, the button stays grey and the status asks for confirmation. Progress stays at zero before the operation starts.

## 8 · Write system

**“Write system now”** starts the operation. If selected, the complete device backup is created and verified first; writing and read-back follow. The current phase is shown as text, with percentages for measurable file operations. Keep power and USB connected. The application reads back the entire written region and compares it with the image. Normal cancellation is unavailable during this operation.

If interrupted, use [guided recovery](troubleshooting.md). Retrying never overwrites an existing original complete device backup.

## 9 · Restore data

Disconnect the programming cable, release the boot button and start the DLTNG normally. Use the displayed target address or establish direct service access. **“Restore data”** reconnects to the same device, verifies the session proof and imports the backup.

## 10 · Finish

Select **“Apply network settings”**, then **“Run final checks”**. Completion is reported only after files, databases, settings, services and web interfaces are checked. **“Open DLTNG”** opens the web interface.

Keep the backup folder. It contains your backup, session state and log and is needed for recovery.

## Resume or recover

Use **“Open session”** to select `session.json` in the previous work folder. The application resumes at the appropriate step. If the original device resumed normal operation after backup, create a new backup. An available complete device backup can be written back to the same device using **“Restore original system”**; its startup must then be checked.


**Back** reviews completed steps. **Next** moves forward without repeating operations. See [Troubleshooting](troubleshooting.md) for diagnostic packages and resuming write monitoring.

## DLTNG display during the upgrade

From **Check device**, the device shows **BUSY** and the current stage. Remove cards and USB storage and let current work finish first. The display uses the language of the most recent device action.

![Maintenance display during backup](assets/display-en.png)

Smartcard, USB, RFID, upload and ordinary idle remain inhibited. A dedicated display service reads the seven-line `display.log` without processing business data. Losing the PC connection does not release processing. On the source, use **Release the old device and back up again**; the target requires restoration and final checks before release.

No operating system is running for the display while powered off or in USB programming mode. Follow the PC wizard then. The new pilot image shows BUSY from normal maintenance startup; older images show it after verified SSH reconnection. This view was tested at 480 × 320 pixels; physical display/boot acceptance remains pending.
