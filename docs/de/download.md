# DLTNG Upgrade herunterladen

**Version @@VERSION@@ · Windows 11 x64 · Portable · @@SIZE@@**

[DLTNG-Upgrade.exe herunterladen](@@DOWNLOAD@@){ .md-button .md-button--primary }
[Release und Prüfsummendatei](@@RELEASE@@){ .md-button }

Der Download ist öffentlich und erfordert kein GitHub-Konto. Die Datei wird als GitHub-Release-Anlage bereitgestellt. Es ist keine Python-Installation erforderlich. Entpacken oder Installieren der Anwendung ist nicht nötig; Sicherungen werden in einem dauerhaften Arbeitsordner gespeichert.

## Erste Schritte

1. EXE in einem eigenen lokalen Ordner speichern.
2. `DLTNG-Upgrade.exe` starten.
3. Über die Flagge oben rechts die Sprache wählen.
4. Zum Kennenlernen **„Demo ausprobieren“** auswählen.

!!! info "Entwicklungsausgabe"

    Diese Ausgabe ist noch nicht mit einem Codesignaturzertifikat signiert. Windows oder Unternehmensrichtlinien können den Start einschränken. Kunden-Flashvorgänge benötigen weiterhin eine dokumentierte Hardwarefreigabe und ein passendes signiertes Systemimage. Die bloße Verfügbarkeit des Downloads ist keine Gerätefreigabe.

## Was ist enthalten?

- Deutscher und englischer Assistent, lokal umschaltbar.
- Python-/Qt-Laufzeit, Bilder, Flaggen, Gerätehelfer und geprüftes Raspberry-Pi-USB-Paket.
- Die vereinbarte eingebettete interne Geräte-Zugangskonfiguration.
- Demomodus und Paket-Selbsttest.

USB-Treiber sowie privilegierte Datenträger- und Netzwerkeinstellungen können eine Einrichtung mit Administratorrechten erfordern. Das passende **Systemimage** wird im Assistenten über UPS bezogen. Hier wird ausschließlich das Windows-Tool angeboten.

## SHA-256 prüfen

```text
@@SHA256@@
```

Optional in PowerShell:

```powershell
Get-FileHash .\DLTNG-Upgrade.exe -Algorithm SHA256
```

Das Ergebnis muss mit der obigen Prüfsumme beziehungsweise der Datei `DLTNG-Upgrade.exe.sha256` im Release übereinstimmen.

[Anleitung](guide.md) · [Programmänderungen](changelog.md) · [Image-Änderungen](image-changelog.md)
