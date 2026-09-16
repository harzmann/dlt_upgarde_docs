# Änderungen am Upgrade-Tool

### 0.2.2 – 2026-09-16 · Originalimage 1.0

- Eigenes Profil für die im Originalimage gespeicherte Version `1` sowie `1.0`/`1.0.0`, Debian 11 und Python 3.9.
- Alte Zertifikate erhalten, NFC-Konfiguration als Archiv sichern und Entwicklungsrechner-Pfade für erzeugte Berichte korrigieren.
- MariaDB-Schema vor Sicherung und nach Import prüfen; fehlende lokale Datenbankwerkzeuge sperren die Sicherung. FTP-/SMB-Schreibdienste während der Sicherung anhalten.
- Bei älteren Upload-Dateien ohne sichere Übertragungsnachweise Offline-Modus verlangen, damit das Upgrade keine erneute Übertragung auslöst.
- Wiederherstellung mit der tatsächlichen Originaldatenbank, Konfiguration, Zertifikaten und zusätzlichen DDD-/CSV-Dateien einschließlich wiederholtem Import geprüft. Physische Geräteabnahme bleibt offen.

### 0.2.1 – 2026-09-16 · Pilotvorbereitung

- Signierte Pilotimages über UPS; an explizite CM4-Seriennummern und ein Ablaufdatum gebunden.
- Laborhinweis in der UI und Geräteabgleich vor der Installation des Sicherungshelfers.
- Nur lesende Prüfung von Seriennummer und Ausgangsversion; Version 1.0 wird vor Änderungen mit einer konkreten Handlungsempfehlung angehalten.
- Zusätzliche Tests für Gerätebegrenzung, Ablauf und den Downloadpfad. Direkte Migration aus 1.0 und Hardwareabnahme bleiben offen.

### 0.2.0 – 2026-09-15

- Produktname **DLTNG Upgrade**, Programmdatei `DLTNG-Upgrade.exe` und eigenes Repository `dlt_upgrade`.
- Deutsch/Englisch über eine Schaltfläche mit Landesflagge oben rechts; Auswahl dauerhaft im Arbeitsordner gespeichert.
- Sprachwechsel ohne Zurücksetzen von Gerätesitzung, Eingaben, Bestätigung oder Fortschritt. Auch Status, Fehler, Dialoge und Wiederherstellungsanzeigen werden übersetzt.
- Zweisprachige MkDocs-Dokumentation und öffentlicher Windows-Download im Repository `dlt_upgarde_docs`.
- Beschreibung, Schrittanleitung, Fehlerhilfe, Programm-Changelog und separates Image-Changelog in beiden Sprachen.
- Bestehendes Geräte-/UPS-Protokoll und gemeinsame Flash-Sperre für die Vorgängerausgabe bleiben kompatibel.
- Zusätzliche Sprach-, Persistenz-, Übersetzungsabdeckungs- und Demotests. Weiterhin Entwicklungsausgabe ohne Hardwarefreigabe.

### 0.1.0 – 2026-09-15

- Erste portable PySide6-Entwicklungsausgabe mit zehn Schritten und vollständigem Demomodus.
- Pflichtsicherung, optionale eMMC-Sicherung, signierter Download, USB-Schreibprüfung, Datenübernahme und Wiederanlauf.
- Separate UPS-Imageschnittstelle und bereinigtes CM4-Testimage vorbereitet und softwareseitig geprüft.
- Fünf symbolische ImageGen-Illustrationen. Physische Geräte- und Datenmigrationsabnahme offen.
