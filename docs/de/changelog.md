# Programmänderungen

## 0.2.8 – 2026-09-17 · Vollbild und Fortschritt auf dem Gerät

- Eigenständiger Upgrade-Bildschirm über dem gesamten Desktop, einschließlich schwebender Tastatursymbole. Auf dem Originalsystem wird die Anzeige vor dem Beenden von Chrome geöffnet.
- Sichtbaren Vollbildstart prüfen; bei fehlender Anzeige die Aktion mit konkretem Hinweis anhalten und die Geschäftsdienste gesperrt lassen.
- Schrittanzeige, Dateizähler und tatsächlich übertragene Bytes; Aktivitätsanzeige für Vorgänge ohne messbare Gesamtmenge. Fortschrittsmeldungen sind sitzungsgebunden und begrenzt, Übertragungsdaten bleiben bei Ausfall einer Meldung erhalten.
- Deutscher/englischer Bildschirm bei 480 × 320 und 1024 × 600 geprüft. Wechsel bei angehaltenem Chrome und gesperrten Lesediensten auf dem Original-1.0-CM4 geprüft, anschließend Normalbetrieb wiederhergestellt. Vollständiger Flash-/Wiederherstellungstest bleibt offen.
- Vorhandenes UPS-Image bleibt unverändert; der Assistent aktualisiert den Gerätehelfer nach Identitäts-/Sitzungsprüfung.

## 0.2.7 – 2026-09-17 · Wartungsanzeige

- Display mit BUSY und deutschen/englischen Phasentexten ab Geräteprüfung.
- Eigene Wartungsanzeige; Smartcard, USB, RFID, Upload und normaler Idle-Dienst bleiben bis zur Freigabe gesperrt.
- Sperre bleibt bei PC-Absturz und Verbindungsverlust erhalten. Quellgerät bereits vor dem Download ausdrücklich wieder freigeben können.
- Neues Pilotimage zeigt die Meldung ab Wartungsstart. Die physische Geräteabnahme steht noch aus.

### 0.2.6 – 2026-09-16 · Wiederaufnahme und Diagnose

- Windows-Fortschrittsaustausch gegen kurzzeitige Dateisperren absichern; Anzeigeausfälle unterbrechen keinen Schreibvorgang.
- Laufende/abgeschlossene Systemhelfer wieder aufnehmen; mehrere Sitzungen nach Datum und Gerätebezug auswählen. Zurückblättern ohne erneute Ausführung.
- Kompakte Oberfläche ohne Bildunterschrift, sichtbare Hauptaktionen, vergrößerbare Anschlussbilder und direkte Netzwerkoptionen bei Bedarf.
- Risiko-/UAC-Dialog vor Freigabe; erst nach Herunterfahren und ausgeschaltetem Display den Stromstecker ziehen.
- Zweisprachige Fehlercode-Hilfe, bereinigte zeitliche Protokolle, Diagnose-ZIP und bestätigter UPS-Versand.

### 0.2.5 – 2026-09-16 · Bestätigung und Fortschritt

- Gut sichtbare Bestätigungskästchen mit Rahmen und Häkchen; gesperrte Hauptschaltflächen klar grau darstellen.
- Im Bestätigungsschritt die Freigabe und Geräteübersicht direkt anzeigen. Ohne Bestätigung bleibt „Weiter zur Neuinstallation“ gesperrt; auch direkte Aktionsaufrufe können die Freigabe nicht überspringen.
- Vor dem Start keinen abgeschlossenen Fortschritt aus der USB-Erkennung anzeigen. Klar zwischen Bestätigung, Startbereitschaft und laufender Neuinstallation unterscheiden.
- Prozentangaben und eigene Statusmeldungen für Prüfung der Pflichtsicherung, der vollständigen Gerätesicherung und des Images vor dem Schreiben. Version im Fenstertitel anzeigen.
- Bestätigung per Maus/Tastatur, genau einen Start pro Vorgang und Fortschritt mit temporären Testdateien geprüft; kein reales Gerät beschrieben.

### 0.2.4 – 2026-09-16 · USB-Anzeige und Gerätebilder

- Automatisches Öffnen der Bootpartition während der USB-Schritte und Rückfallwiederherstellung unterdrücken, solange der Assistent oder sein vergrößertes Anschlussbild im Vordergrund ist. Keine dauerhafte Änderung der Windows-Einstellungen.
- Symbolische DLTNG-Front- und Anschlussdarstellung anhand der Originalfotos; sechs nummerierte Anschlussgruppen, übersetzbare Legende und vergrößerte Ansicht.
- USB-Admin und versenkten Admin-Taster getrennt kennzeichnen; Hinweis zur leichten Betätigung mit einem Kugelschreiber.
- Echte Windows-Nachrichten für Assistent und Bilddialog geprüft; Demomodus und Schritte außerhalb des USB-Vorgangs bleiben ausgenommen. Physischer USB-Anstecktest bleibt Teil der Geräteabnahme.

### 0.2.3 – 2026-09-16 · Pilotkorrekturen

- Abschlussmeldungen aus Hintergrundarbeiten ausschließlich im Oberflächenthread verarbeiten; gelegentlichen Absturz bei Schrittwechseln beheben.
- Systemhelfer aus der tatsächlichen portablen EXE starten: USB-Treiber und direkte Ethernet-Einrichtung benötigen keine separate `python.exe` mehr. Abgebrochene Administratorabfragen und Startfehler getrennt erklären.
- Lesbare Eingaben, Auswahllisten und Ordnerdialoge auch bei dunklem Windows-Design; kleinere Anschlussillustration und Schrittwechsel zum Seitenanfang.
- Gerätesuche mit sichtbaren Phasen, Fortschritt und eindeutiger Ergebnisanzeige; kürzere Wartezeiten bei nicht passenden SSH-Geräten.
- Eigenes Anwendungssymbol in Fenster, Taskleiste und EXE.
- Ältere NFC-Build- und uWSGI-Protokolle vollständig archivieren und wiederherstellen; unbekannte Nutzdaten weiterhin sperren.
- Bei wiederaufgenommenen Sicherungen Geräteidentität prüfen und Sicherungshelfer aktualisieren. Download und bestehende Sitzung bleiben verwendbar.
- Paket-Selbsttest startet den echten Helfer lesend aus der gebauten EXE. Treiberinstallation, Netzwerkänderungen und physischer Flash-/Rückfalltest bleiben Teil der Geräteabnahme.

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
