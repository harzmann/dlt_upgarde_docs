# Troubleshooting

Error messages describe the problem and the next action. Backups and session state are retained. Keep the displayed **error code** and session folder available for support.

| Situation | Next action |
|---|---|
| Device not found | Check the IP address, network cable and power; enter the address manually if needed. |
| No matching approved image | Have device entitlement and UPS approval checked. Do not bypass the block. |
| `REL-001`: no customer approval | Use the development edition in demo mode; actual tests require configured lab approval. |
| `IMG-008`: prepared image missing or changed | Return to the download step and download the image again. |
| Not enough space | Select a larger local work folder; do not delete backups while the session is incomplete. |
| Unknown data or databases | Have the data profile or migration rule checked before flashing. |
| USB device missing or ambiguous | Check the approved device instructions, boot button, programming cable and driver; connect only the intended device. |
| Drive is in use | Close File Explorer or other programs accessing the DLTNG drive. |
| Network unavailable after restart | Wait for startup, check power and Ethernet, and use the intended service connection. |

## Fixes for the current test

**Use test build 0.2.4.** It fixes Windows helper startup for USB drivers and direct Ethernet connections, readability with dark Windows settings, and device-search feedback. Known legacy NFC/uWSGI logs are included in the backup; a dedicated application icon is included.From 0.2.4, USB steps in the foreground suppress automatic opening of the boot partition. New, enlargeable device and connector illustrations are based on original photos.

Close the previous EXE, start the new one and choose **“Open session”**. Select the existing `session.json` in the permanent work folder. The downloaded image can be reused. Run the backup again; the wizard verifies device identity and refreshes the backup helper. Keep the existing work folder. If the old device has since resumed normal operation, create a fresh backup.

On an existing LAN, use the normal device connection. The direct service connection is intended for a dedicated Ethernet cable between the PC and DLTNG. The app requests administrator rights for the relevant Windows operation.


## Interrupted download

Try again. UPS rechecks authorization; a suitable partial download can resume. The device is paused only after the complete download has been verified.

## Interrupted backup

Never treat an incomplete file as a valid backup. Open the session and follow the guided recovery path. If the original device is resumed for normal use, create a new backup before flashing.

## Interrupted writing

Keep the work folder intact. Follow the approved instructions to return the device to programming mode, open the saved session and let the wizard write the entire image again. Full read-back verification follows. Do not try to resume manually at a guessed write position.

## Interrupted restoration

Open the existing session and reconnect the same device. Business services remain paused during restoration. File conflicts or differing database contents are reported for review.

## Recover the original system

If a verified complete device backup exists, the wizard offers to write it back and check startup afterwards. Without that complete copy, recovery consists of installing an approved image again and importing the mandatory data backup.

## Language and work folder

The language preference belongs to the work folder. A new folder defaults to German. Use the flag at the top right to switch to English. A message saying the language preference cannot be saved means the folder's write permissions need checking.
