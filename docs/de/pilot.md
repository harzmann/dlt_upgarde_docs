# Einen Pilottest vorbereiten

Eine gesonderte Testausgabe ab Version 0.2.1 kann ein signiertes Laborimage über UPS beziehen. Die Freigabe gilt ausschließlich für eingetragene CM4-Seriennummern bis zum festgelegten Ablaufdatum. Die allgemeine Hardwarefreigabe bleibt aus. Der öffentliche Standarddownload 0.2.0 enthält diese konkrete Pilotkonfiguration nicht.

## Korrekturen für den aktuellen Test

**Testausgabe 0.2.8 verwenden.** Sie zeigt ab der Geräteprüfung den Upgrade-Schritt und **BUSY** auf dem DLTNG an. Smartcard, USB, RFID und Übertragung bleiben bis zur geprüften Freigabe gesperrt. Die Korrekturen aus 0.2.6 bleiben enthalten: wiederaufnehmbare Windows-Systemhelfer, **Zurück** zum Betrachten erledigter Schritte, kompakte Ansicht und **Diagnose** mit Fehlercode-Erklärung, bereinigtem ZIP und bestätigtem Versand an UPS.

**Bestehenden Vorgang fortsetzen:** Lassen Sie das Gerät angeschlossen, solange ein Systemhelfer arbeitet. Nach dessen Abschluss die alte EXE schließen, 0.2.8 starten und **„Vorgang öffnen“** wählen. Die aktuelle `session.json` verwenden. Bei mehreren Vorgängen helfen Datum, Fortschritt und Ordner bei der Auswahl; der neueste steht oben. Bereits geprüfter Download und Sicherung bleiben erhalten. Ein erfolgreicher Schreibnachweis führt direkt zur Datenwiederherstellung. Falls das Altgerät nach der Sicherung wieder normal betrieben wurde, ist dagegen eine neue Sicherung erforderlich.

**Nach erneuter Installation des Originalimages 1.0 von vorne beginnen:** Das DLTNG normal starten und seine Bereitschaft abwarten. Testausgabe 0.2.8 starten und einen neuen Vorgang mit neuer Sicherung anlegen; keine alte `session.json` öffnen. Einen neuen dauerhaften Arbeitsordner verwenden und frühere Sicherungsordner aufbewahren. Karten und USB-Datenträger vor **„Gerät prüfen“** entfernen. Die App lädt das passende signierte Pilotimage über UPS. Der Normalablauf benötigt keine manuelle Image-Auswahl.

Die neue Image-Ausgabe `10.0.0-rc.4-upgrade.1-clean-update` benötigt mindestens Testausgabe 0.2.7. Ihre Wartungsanzeige startet nach der Prüfung der Sitzung beim ersten normalen Start. Ohne Strom und im USB-Programmiermodus erfolgt die Anleitung auf dem PC. Die Original-1.0-Anzeige wurde am CM4 geprüft; die vollständige Migration bleibt offen. Ab App 0.2.8 deckt der eigenständige Bildschirm den Desktop ab und zeigt messbaren Fortschritt. Das vorhandene UPS-Image bleibt unverändert; der neue Helfer wird nach Geräte-/Sitzungsprüfung übernommen.

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
