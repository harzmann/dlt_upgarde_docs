# Download DLTNG Upgrade

**Version @@VERSION@@ · Windows 11 x64 · Portable · @@SIZE@@**

[Download DLTNG-Upgrade.exe](@@DOWNLOAD@@){ .md-button .md-button--primary }
[Release and checksum file](@@RELEASE@@){ .md-button }

The download is public and does not require a GitHub account. The file is provided as a GitHub release asset. No Python installation is required. You do not need to unpack or install the application; backups are stored in a permanent work folder.

## First steps

1. Save the EXE in a dedicated local folder.
2. Start `DLTNG-Upgrade.exe`.
3. Choose your language using the flag at the top right.
4. Select **“Try the demo”** to explore the tool.

!!! info "Development edition"

    This edition is not yet signed with a code-signing certificate. Windows or company policies may restrict startup. Customer flashing still requires documented hardware approval and a matching signed system image. Availability of the download does not approve a device for flashing.

## What is included?

- German and English wizard with local language switching.
- Python/Qt runtime, illustrations, flags, device helper and verified Raspberry Pi USB package.
- The agreed embedded internal device-access configuration.
- Demo mode and package self-test.

USB drivers and privileged disk/network operations may require administrator setup. The matching **system image** is obtained through UPS inside the wizard. This page provides only the Windows tool.

## Verify SHA-256

```text
@@SHA256@@
```

Optionally use PowerShell:

```powershell
Get-FileHash .\DLTNG-Upgrade.exe -Algorithm SHA256
```

The result must match the checksum above or the `DLTNG-Upgrade.exe.sha256` file in the release.

[User guide](guide.md) · [Application changes](changelog.md) · [Image changes](image-changelog.md)
