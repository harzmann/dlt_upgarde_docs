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
| Network unavailable after restart (NET-003) | Wait for startup and check power and Ethernet. On a company LAN, enter the current device address; see step 09 below. |

## Fixes for the current test

**Use the pilot build provided for your test.** Since 0.2.6, Windows progress-file access errors are handled and active or successfully completed helpers can resume. **Back** reviews completed steps without repeating operations. The compact view keeps the primary action visible and removes the picture caption. **Diagnostics** explains error codes, exports a redacted ZIP and offers user-confirmed upload to UPS.

Keep the device connected while a helper is working. If a version change is required, wait for the helper to finish before closing the old EXE, starting the provided pilot build and choosing **“Open session”** with the current `session.json`. If multiple sessions exist, choose using their date, progress and folder; newest is listed first. Verified downloads and backups are retained. A successful saved write result leads directly to data restoration. If the original device resumed normal operation after backup, a fresh backup is required.

On an existing LAN, use the normal device connection. The direct service connection is intended for a dedicated Ethernet cable between the PC and DLTNG. The app requests administrator rights for the relevant Windows operation.


## Interrupted download

Try again. UPS rechecks authorization; a suitable partial download can resume. The device is paused only after the complete download has been verified.

## Interrupted backup

Never treat an incomplete file as a valid backup. Open the session and follow the guided recovery path. If the original device is resumed for normal use, create a new backup before flashing.

## Interrupted writing

Keep the work folder and first choose **Resume write monitoring**. A UI error does not necessarily mean the helper stopped. While it is running, keep power/USB connected and do not start another attempt. A saved success leads to restoration without writing again. Only after an actual helper failure/exit should you follow recovery, rediscover USB and write and verify the entire image again.

## Step 09: Device not found after restart (NET-003)

1. Keep the existing session and backup folder. A missing network connection alone does not require writing the system again.
2. Remove USB Admin, release the Admin button and start the device normally as described in the guide.
3. On a **company LAN / switch**, enter the DLTNG's confirmed current IP address and click **Restore data**. DHCP may assign a different address after reinstallation.
4. Use **Set up direct service connection** only when a dedicated Ethernet cable connects the DLTNG directly to this PC. This function is not intended for the shared company connection.

If both display and network remain unavailable in the earlier pilot image, the newly identified startup configuration fault may be responsible. Diagnosis is required; NET-003 alone does not prove this cause. Keep the backup folder and contact support for a targeted startup correction. The fix has been tested on the 32-GB device and is included in new pilot image upgrade.2. Use app 0.2.10 and this image for new runs. A new EXE alone does not repair an already written old image; see the [image changelog](image-changelog.md).

## Interrupted restoration

Open the existing session and reconnect the same device. Business services remain paused during restoration. File conflicts or differing database contents are reported for review.

## Recover the original system

If a verified complete device backup exists, the wizard offers to write it back and check startup afterwards. Without that complete copy, recovery consists of installing an approved image again and importing the mandatory data backup.

## Language and work folder

The language preference belongs to the work folder. A new folder defaults to German. Use the flag at the top right to switch to English. A message saying the language preference cannot be saved means the folder's write permissions need checking.

## Error codes and diagnostic package

Select **Diagnostics** at the top, search for the error code and read its next action. The latest technical error is shown there. **Create diagnostic package in working folder** exports a ZIP timeline including available earlier sessions for the same device. Older versions did not record all technical details; missing details cannot be recreated.

Packages contain device IDs, computer paths, check results and redacted app/helper logs. Passwords and session tokens are removed; customer files, databases and images are excluded. **Send diagnostic package to UPS** requires explicit confirmation, Internet access and current device/image authorisation. Failed uploads retain the local ZIP.

UPS returns a checksum receipt. Logged-in administrators find packages under **System Images → Upgrade diagnostics**. Packages are retained for 30 days, are not automatically processed by AI, and have a 20 MiB upload limit.

| Code | Meaning and next action |
|---|---|
| `APP-001`, `WIN-099` | Unexpected app/helper error. During writing, resume monitoring first; create a diagnostic package. |
| `WIN-010` | Windows administrator prompt cancelled. Retry and approve your DLTNG app. |
| `WIN-013` | A helper is already writing. Keep the device connected and resume monitoring. |
| `WIN-016` | Helper exited without a complete result. Use guided recovery. |
| `SES-007` | Write record belongs to another session. Choose the correct session; contact support. |
| `DIA-001` | Package exceeds 20 MiB. Keep it locally and contact support. |
| `DIA-002` | UPS rejected the upload. Keep the local ZIP; check connection and authorisation. |
