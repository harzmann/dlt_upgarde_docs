# Einen Pilottest vorbereiten

Eine gesonderte Testausgabe ab Version 0.2.1 kann ein signiertes Laborimage über UPS beziehen. Die Freigabe gilt ausschließlich für eingetragene CM4-Seriennummern bis zum festgelegten Ablaufdatum. Die allgemeine Hardwarefreigabe bleibt aus. Der öffentliche Standarddownload 0.2.0 enthält diese konkrete Pilotkonfiguration nicht.

## Korrekturen für den aktuellen Test

**Testausgabe 0.2.3 verwenden.** Sie korrigiert den Start des Windows-Helfers für USB-Treiber und direkte Ethernet-Verbindungen, die Lesbarkeit im dunklen Windows-Design und die Rückmeldungen der Gerätesuche. Die bekannten älteren NFC-/uWSGI-Protokolle werden mitgesichert; ein eigenes Anwendungssymbol ist enthalten.

Die vorherige EXE schließen, die neue EXE starten und **„Vorgang öffnen“** wählen. Dazu die bisherige `session.json` im dauerhaften Arbeitsordner auswählen. Das heruntergeladene Image kann weiterverwendet werden. Die Sicherung erneut ausführen; der Assistent prüft die Geräteidentität und aktualisiert den Sicherungshelfer. Den bisherigen Arbeitsordner aufbewahren. Falls das Altgerät zwischendurch wieder normal betrieben wurde, eine neue Sicherung erstellen.

Im vorhandenen LAN genügt die normale Geräteverbindung. Die direkte Serviceverbindung ist für ein eigenes Ethernet-Kabel zwischen PC und DLTNG vorgesehen. Administratorrechte fordert die App bei der jeweiligen Windows-Aktion an.


## Vorbereitung durch den Gerätebetreuer

1. Tatsächliche CM4-Seriennummer, eMMC-Größe und installierte Anwendungsversion auslesen.
2. Das Gerät beim richtigen UPS-Kunden eintragen und dessen wirksame Berechtigung prüfen.
3. Eine Testausgabe mit öffentlichem Signaturschlüssel und genau dieser Testseriennummer bereitstellen.
4. Das passende Image signieren: Hardwareprofil, erlaubte Ausgangsversionen, Seriennummer und Ablaufdatum gehören zur Signatur.
5. In UPS Pilotbetrieb aktivieren, Image importieren und **„Für diese Testgeräte freigeben“** wählen.
6. Download, Prüfsummen und Ablehnung anderer Geräte prüfen. Das Gerät dabei noch nicht anhalten oder flashen.

## Ausgangsversion 1.0

**Die gesonderte Pilotversion 0.2.2 unterstützt den direkten Test aus dem geprüften Originalimage 1.0.** Das Image `CM4_DLT_231119_V9_X.img` speichert die Anwendungskennung `1`. Debian 11, Python 3.9, Konfigurationen und die tatsächliche MariaDB-Datenbank wurden untersucht. Sicherung und Wiederherstellung mit 19 Tabellen, sechs Ansichten, Zertifikaten und DDD-/CSV-Testdateien einschließlich wiederholtem Import wurden isoliert geprüft. Die physische Geräteabnahme bleibt offen.

Für diesen Pilottest ist kein Zwischenupdate auf 9.5 erforderlich. Die neue signierte Freigabe verlangt mindestens Upgrade 0.2.2. Die frühere Pilot-EXE 0.2.1 und der öffentliche Standarddownload 0.2.0 eignen sich nicht für diesen direkten Weg.

**Wenn Upload-Dateien vorhanden sind:** Am Altgerät zunächst die Übertragung auf **Offline** stellen und klären, welche Dateien bereits gesendet wurden. Version 1 führt noch keine zuverlässigen Übertragungsnachweise. Alle Dateien werden gesichert und wiederhergestellt; Offline bleibt aktiv. Erst nach Prüfung des Versandstatus die Übertragung wieder einschalten. Der Assistent erzeugt keine erfundenen Versandbestätigungen.

## Test durchführen

Die bereitgestellte Test-EXE verwenden; oben erscheint **„LABOR“**. Die vollständige Gerätesicherung aktiviert lassen und die [Schrittanleitung](guide.md) befolgen. Der Gerätebetreuer muss die Boot-Taster- und Kabelfolge an der tatsächlichen Trägerplatine bestätigen. Seriennummer, Ausgangs-/Zielversion, Sicherung, Ergebnis und Rückfall-Boot dokumentieren.

Eine erfolgreiche Pilotmigration ist noch keine allgemeine Freigabe für andere Geräte oder Ausgangsversionen.
