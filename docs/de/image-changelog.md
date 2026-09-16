# DLTNG-Image: Changelog

Diese Historie umfasst frühere Migrationsimages und das bereinigte Profil für DLTNG Upgrade. Historische Angaben beziehen sich auf das jeweilige Image. Das Windows-Tool hat ein [eigenes Changelog](changelog.md).

## Upgrade-Helfer 0.2.3 – 2026-09-16

Ältere NFC-Build- und uWSGI-Protokolle werden als Archiv gesichert und wiederhergestellt. Vorhandene Image-Dateien und UPS-Freigaben bleiben unverändert. Die App stellt den neuen Helfer nach Geräte-/Sitzungsprüfung bereit.

## Pilotbereitstellung – 2026-09-16

- Ergänzende signierte Freigabe für das geprüfte Originalimage mit Anwendungskennung `1`/`1.0`; benötigt die separate Testausgabe 0.2.2. Image-Datei unverändert, aktualisierter Sicherungs-/Migrationshelfer wird sitzungsgeprüft durch die App bereitgestellt.
- Datenbank-, Datei- und Konfigurationswiederherstellung isoliert geprüft; physische Geräteabnahme bleibt offen. Bei älteren Upload-Dateien ohne Übertragungsnachweise ist Offline-Modus erforderlich.
- Das bereinigte Image vom 15. September wird unverändert über UPS für ein ausdrücklich registriertes CM4-Testgerät bereitgestellt.
- Signiertes Manifest mit Ablaufdatum und separater Upgrade-Testausgabe 0.2.1. Die Freigabe ist an Testgerät, 32-GB-Hardwareprofil und Ausgangsversion gebunden.
- Ausgangsversionen der ersten Pilotfreigabe: 9.5, 10.0.0-rc.3 und 10.0.0-rc.4. Die ergänzende Freigabe ab Upgrade 0.2.2 unterstützt zusätzlich das geprüfte 1.0-Profil.
- Keine allgemeine Hardware- oder Kundenfreigabe. Ablauf und offene Prüfungen stehen unter [Pilottest](pilot.md).

## 10.0.0-rc.4-startup.1-clean-update – 2026-09-15

- Eigenes bereinigtes Profil für Neuinstallation mit anschließender Datenübernahme. Referenzkonfiguration, Logos, Berichte, Nutzdateien und SQL-Dumps werden ausgeschlossen.
- Dauerhafter Wartungszustand, sitzungsgebundene Startkonfiguration, Service-Netzwerk und Geräteidentitätsnachweis.
- Gerätehelfer für Sicherung, Wiederherstellung, Netzwerkrückkehr und Abschlussprüfung; Geschäftsdienste bleiben bis zum erfolgreichen Abschluss angehalten.
- Vollständig gebautes Image: 991.882.668 Bytes komprimiert, 4.647.288.832 Bytes roh. ARM64-Webprozesse, beide exportierten Startbilder, FAT/ext4 sowie vollständige Dekompression und Prüfsummenvergleich bestanden.
- Bauvorschrift `0cb6f9a`; korrigierte Abschlussprüfung `20e54c1`. Startbilder werden auf der ausgelieferten Bootpartition geprüft, da pi-gen die endgültigen Startdateien erst beim Export erstellt.
- Physischer CM4-Boot, Migration auf 16/32 GB, Stromausfallwiederanlauf und tatsächlicher Rückfallstart weiterhin offen. Keine Kundenfreigabe oder Produktionssignatur des Images.

## 10.0.0-rc.4-startup.1 – 2026-09-15

- Vorhandenen blauen Startbildschirm bereits im Kernel anzeigen; linksbündiger Text „DLTNG STARTET …“, normale und gedrehte Grafik im initramfs.
- Vollflächige Zwischenanzeige beim Xorg-/Chromium-Start. Start unabhängig von nginx; Hilfsprozess endet nach Erscheinen des Vollbildbrowsers.
- Firmware-Regenbogen, lokale Bootkonsole und systemd-Statusausgabe im normalen Start unterdrücken; SSH und Protokolle erhalten.
- Separater Image-Tag und Lieferordner; alle drei Anwendungen behalten ihre unveränderten rc.4-Commits. Vorherige veröffentlichte Images bleiben unverändert.
- Konfigurations-, Grafik- und X11-Übergangstests; reale Bildschirm-/Bootzeitabnahme weiterhin erforderlich. Siehe image/cm4/STARTUP.md.

## Bauwerkzeug nach 10.0.0-rc.4

- Bei wiederverwendeten Bauverzeichnissen das Rohimage über den Namen des aktuellen komprimierten Exports auswählen. Ältere Rohimages bleiben erhalten; der vollständige SHA256-Vergleich ist unverändert. Die veröffentlichte rc.4-Datei und ihre Versionsmarkierung bleiben unverändert.

## 10.0.0-rc.4 – 2026-09-15

- Bestätigte Referenzkonfiguration SFTP/Port 22 ins neue Image übernehmen; ursprüngliche private Sicherung unverändert erhalten.
- Gemeinsamer rc.4-Aufbau mit allen nach rc.3 geprüften Hotfixes, dauerhafter Diagnosehistorie und separatem Supportdienst unter pi.
- Geräteschlüssel erst auf dem Zielmodul erzeugen; kein Schlüssel im Image. Diagnosebudget innerhalb des Protokollbudgets, historienbewusste Wiederherstellung.
- Bereinigte manuelle UPS-Pakete, geprüfte KI-Empfehlungen, separate Wartungsverträge und firmenweites Jahreskontingent; siehe image/cm4/DIAGNOSTICS.md.
- Physische Ein-Sekunden- und 72-Stunden-Abnahme weiterhin offen; Softwaretests sind keine Hardwarefreigabe.

- Stiller Upload-Timer: ergänzender rc.3-Hotfix unterdrückt sämtliche timerbedingten Display-/Beschäftigt-Meldungen. Exklusive Verarbeitung, Fehlerprotokollierung, bestätigte Übertragung und sichtbarer Smartcard-/USB-Ablauf bleiben erhalten. Bestehende Image-Dateien und Pakete bleiben unverändert.
- Smartcard-Korrektur für rc.3: fehlendes Arbeitsverzeichnis im Image anlegen und beim Bau prüfen. Separates Paket für sichere Dateierstellung, einen Upload nach erfolgreichem Lesen und Belegung bis zur Kartenentnahme; auch Fehler-, Neustart- und USB-Regressionsfälle geprüft. Bestehende Image-Dateien bleiben unverändert.
- rc.3-Anzeigekorrektur: separater Hotfix verschiebt die RAM-Angaben in die System-Informationen und entfernt die doppelte Prozessortemperatur aus der LAN-Seite. Deutsch/Englisch und installierter Code auf dem CM4 geprüft; das veröffentlichte Image bleibt unverändert.
- Anmeldung/Weiterleitungen: eigene nginx-uWSGI-Parameter erhalten den normalisierten Hostnamen samt lokalem Port 8888 beziehungsweise 12005. Die bisherige Distributionsvorgabe übergab nur den Hostnamen und leitete nach Anmeldung auf den unbelegten Port 80. Kanonische Weiterleitungen beider Anwendungen werden nun beim Image-Laufzeittest auf unveränderten Ursprung geprüft.
- Kiosk: Starttext „DLTNG startet …“. Tastatursymbol unten rechts mit 12 Pixeln Abstand fixiert; Verschieben/Größenänderung gesperrt, Position aus tatsächlicher Bildschirmgeometrie berechnet. Separater Ergänzungs-Hotfix für rc.3.
- rc.3-Folgekorrektur: GNOME-Barrierefreiheit vor Onboard aktivieren, damit die Bildschirmtastatur ohne Rückfragedialog automatisch erscheint. Zusammen mit NFC-Dienstkorrektur, dauerhafter Fehleranzeige und linksbündigen Statusmeldungen als separater Hotfix bereitstellen.
- Kiosk-Startkorrektur für rc.3: `libglib2.0-bin` explizit als Laufzeitpaket erhalten. Das darin enthaltene `gsettings` fehlte nach der Paketbereinigung und beendete die grafische Sitzung vor dem Browserstart. Auf CM4 mit 4 GB RAM korrigiert und die DLT-Anzeige vom Anwender bestätigt.
- Bildschirmtastatur: benötigte GNOME-Schemata, AT-SPI-Bus und Atspi-Typelib explizit installieren und ihren tatsächlichen Import prüfen.
- Kiosk-Ausgaben im Systemjournal erfassen. Beim Stoppen die Grafik-Sitzung gezielt beenden, damit ein manueller Neustart nicht 90 Sekunden auf zurückbleibende Grafikprozesse wartet. Abschlussprüfung prüft Kioskprogramme und tatsächliche ARM64-Einstellungsschlüssel; separates Hotfixskript für bestehende rc.3-Installationen. Die veröffentlichten Image-Dateien bleiben unverändert.
- Prüfwerkzeug: deaktivierte EEPROM-Dienste anhand des Links selbst prüfen, ohne absolute Links außerhalb des geprüften Dateisystems aufzulösen. Das bereits gebaute rc.2-Image bleibt unverändert.

## 10.0.0-rc.3 – 2026-09-15

- Gemeinsamer rc.3-Baustand mit exklusiver Geräteverarbeitung, erhaltener Display-Textdatei und unabhängigem 100-ms-Statuszugriff über nginx.
- USB-Mountverwaltung, FAT/exFAT/NTFS-Unterstützung und begrenzte Systemhelfer für Freigabe und Bildschirmdrehung; Desktop-Automount unterdrückt.
- Eigener Kioskbenutzer ohne Administrationsgruppen, Chromium-Sandbox, eingeschränkte Openbox-Sitzung, Bildschirmtastatur und frühe Startanzeige; grafischer Wiederanlauf unabhängig von laufenden Importen.
- Automatische Paketprüfungen/-installationen und Systembenachrichtigungen abgeschaltet; Hersteller-App-Updates bleiben erhalten.
- Sicherung umfasst Übertragungsbestätigungen und Konfliktdateien; Wiederherstellung erhält aktuelle ausstehende Übertragungen und ergänzt vorhandene Bestätigungen.
- Isolierte Regressionstests und Browsermessungen ergänzt; physische Medienreaktion, USB-Portzuordnung, Touch, Bootzeitvergleich und 72-Stunden-Abnahme auf CM4 2 GB/16 GB bleiben offen.

## 10.0.0-rc.2 – 2026-09-14

- Konfigurierbare LAN-Geschwindigkeit und EEE mit Rücksetztimer, Wiederherstellung nach Neustart und Statusanzeige in der DLT-Webkonfiguration. Image-Standard: automatische Geschwindigkeit, EEE aus.
- Hardwarediagnose für Temperatur, RAM, Unterspannung, Drosselung und die EEPROM-Einstellung zur Abschaltung beim Herunterfahren.
- Raspberry-Pi-Diagnosewerkzeuge samt Gerätebaum-Abhängigkeit werden bei der Paketbereinigung erhalten und im fertigen Image geprüft.
- Optionales CM5-Testprofil für die vorhandene CM4-Trägerplatine: offizieller 2712-Kernel, RP1-I²C6 an GPIO38/39 als `/dev/i2c-10`, externe PCF85063A-RTC und PN7150. Der Standard bleibt CM4.
- CM5-Testprofil begrenzt den CPU-Takt zunächst auf 1,5 GHz und lädt keine Lüftersteuerung. Keine CM5-Hardwarefreigabe; GPIO_VREF bleibt ein gesonderter elektrischer Befund.
- Veröffentlichungswerkzeug: GitHub-Antworten ausdrücklich als UTF-8 lesen, damit Sonderzeichen auch mit der Windows-Standardkodierung korrekt verarbeitet werden. Zusätzlicher Regressionstest; das bereits gebaute Image bleibt unverändert.

## 10.0.0-rc.1 – 2026-09-14

- Gemeinsame Versionsnummer und Release-Tags für alle drei Anwendungen und das Image.
- Eigenes privates Image-Repository, festgehaltene Anwendungs-Commits und Versionsanzeige unabhängig von wiederhergestellten Konfigurationen.
- Privater GitHub-Download mit SHA256-Prüfung und zusätzlicher QNAP-Sicherung je Version.
- Raspberry Pi OS Lite Trixie, ARM64; neue Python-Umgebungen und neu gebaute NFC-/CCID-Komponenten.
- CM4 mit 2 GB RAM / 16 GB eMMC bestimmt die Ressourcenbudgets; dasselbe Image ist für 4 GB / 32 GB vorgesehen.
- NetworkManager, RTC-/Zeitkorrekturen, begrenzte Protokolle, serialisierte Berichte und sichere Datenwiederherstellung.
- Hardwareabnahme einschließlich 72-Stunden-Test noch offen. Keine CM5-Freigabe.

## Pre-Version 10

- 2026-09-14: Erstes CM4-Trixie-Testimage aus eingefrorenen Referenzquellen und Migrationspatches erstellt, softwareseitig geprüft.
- Dieses ursprüngliche Image wird unter `archive-cm4-20260914` unverändert einschließlich seiner ursprünglichen Prüfsumme archiviert.
- Die früheren Anwendungsversionen und ihre Entwicklung sind in den Changelogs der drei Anwendungs-Repositories dokumentiert.
- Die Git-Historien bleiben unverändert. Die lokale Weiterentwicklung mit zusätzlichen DLC-Funktionen wird im jeweiligen Zweig `codex/development-10.1` bewahrt.
