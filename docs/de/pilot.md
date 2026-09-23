# Einen Pilottest vorbereiten

Eine gesonderte Testausgabe ab Version 0.2.1 kann ein signiertes Laborimage über UPS beziehen. Die Freigabe gilt ausschließlich für eingetragene CM4-Seriennummern bis zum festgelegten Ablaufdatum. Die allgemeine Hardwarefreigabe bleibt aus. Der öffentliche Standarddownload 0.2.0 enthält diese konkrete Pilotkonfiguration nicht.

## Korrekturen für den aktuellen Test

**Testausgabe 0.2.12 verwenden.** Sie zeigt ab der Geräteprüfung den Upgrade-Schritt und **BUSY** auf dem DLTNG an. Smartcard, USB, RFID und Übertragung bleiben bis zur geprüften Freigabe gesperrt. Die Korrekturen aus 0.2.6 bleiben enthalten: wiederaufnehmbare Windows-Systemhelfer, **Zurück** zum Betrachten erledigter Schritte, kompakte Ansicht und **Diagnose** mit Fehlercode-Erklärung, bereinigtem ZIP und bestätigtem Versand an UPS.

**Bestehenden Vorgang fortsetzen:** Lassen Sie das Gerät angeschlossen, solange ein Systemhelfer arbeitet. Nach dessen Abschluss die alte EXE schließen, 0.2.12 starten und **„Vorgang öffnen“** wählen. Die aktuelle `session.json` verwenden. Bei mehreren Vorgängen helfen Datum, Fortschritt und Ordner bei der Auswahl; der neueste steht oben. Bereits geprüfter Download und Sicherung bleiben erhalten. Ein erfolgreicher Schreibnachweis führt direkt zur Datenwiederherstellung. Falls das Altgerät nach der Sicherung wieder normal betrieben wurde, ist dagegen eine neue Sicherung erforderlich.

**Nach erneuter Installation des Originalimages 1.0 von vorne beginnen:** Das DLTNG normal starten und seine Bereitschaft abwarten. Testausgabe 0.2.12 starten und einen neuen Vorgang mit neuer Sicherung anlegen; keine alte `session.json` öffnen. Einen neuen dauerhaften Arbeitsordner verwenden und frühere Sicherungsordner aufbewahren. Karten und USB-Datenträger vor **„Gerät prüfen“** entfernen. Die App lädt das passende signierte Pilotimage über UPS. Der Normalablauf benötigt keine manuelle Image-Auswahl.

Für neue Flashvorgänge Image **10.0.0-rc.4-upgrade.2-clean-update** mit Testausgabe **0.2.12** verwenden. Es enthält die korrigierte Startkonsole und DHCP zusätzlich zur festen Serviceadresse. Die fehlerhaften älteren Pilotimages werden nicht erneut verwendet. Ein bereits geschriebenes altes Image wird durch eine neue EXE allein nicht repariert; bei dunklem Display den Support zur gezielten Startkorrektur hinzuziehen und die Sitzung behalten. Nach der Korrektur lässt sich die vorhandene Sicherung wiederherstellen. Vollständige Migration und 16-GB-Abnahme bleiben offen.

Im vorhandenen LAN genügt die normale Geräteverbindung. Die direkte Serviceverbindung ist für ein eigenes Ethernet-Kabel zwischen PC und DLTNG vorgesehen. Administratorrechte fordert die App bei der jeweiligen Windows-Aktion an.

Ab 0.2.11 zeigen Schritt 01 und 05 den aktuellen Sicherungsordner. In Schritt 09 zuerst USB-Admin entfernen und wie beschrieben neu starten, danach **Daten wiederherstellen** drücken. Erst dieser Klick startet die automatische Suche. Das IP-Feld kann leer bleiben; gefundene Adressen werden vor der Übertragung mit Geräte- und Sitzungsnachweis geprüft. [Suchgrenzen und USB-Netzwerk](troubleshooting.md#grenzen-der-suche-und-usb-admin).


In 0.2.11 nennt jeder Schritt die nächste Schaltfläche. Nach dem Wiederanschließen des Stroms in Schritt 06 unten rechts auf **„USB-Gerät erkennen“** klicken. Während laufender Arbeiten blinkt oben im PC-Assistenten die rote Warnung **„UPGRADE-VORGANG LÄUFT - NICHT AUSSCHALTEN!“**. Sie bleibt auch bei unklarem Schreibstatus aktiv; in den angeleiteten Pausen zum Umstecken und Neustarten wird sie ausgeblendet.

## Vorbereitung durch den Gerätebetreuer

1. Tatsächliche CM4-Seriennummer, eMMC-Größe und installierte Anwendungsversion auslesen.
2. Das Gerät beim richtigen UPS-Kunden eintragen und dessen wirksame Berechtigung prüfen.
3. Eine Testausgabe mit öffentlichem Signaturschlüssel und genau dieser Testseriennummer bereitstellen.
4. Das passende Image signieren: Hardwareprofil, erlaubte Ausgangsversionen, Seriennummer und Ablaufdatum gehören zur Signatur.
5. In UPS Pilotbetrieb aktivieren, Image importieren und **„Für diese Testgeräte freigeben“** wählen.
6. Download, Prüfsummen und Ablehnung anderer Geräte prüfen. Das Gerät dabei noch nicht anhalten oder flashen.

## Ausgangsversion 1.0

**Die aktuelle Pilotversion unterstützt den direkten Test aus dem geprüften Originalimage 1.0.** Das Image `CM4_DLT_231119_V9_X.img` speichert die Anwendungskennung `1`. Debian 11, Python 3.9, Konfigurationen und die tatsächliche MariaDB-Datenbank wurden untersucht. Sicherung und Wiederherstellung mit 19 Tabellen, sechs Ansichten, Zertifikaten und DDD-/CSV-Testdateien einschließlich wiederholtem Import wurden isoliert geprüft. Die physische Geräteabnahme bleibt offen.

Für diesen Pilottest ist kein Zwischenupdate auf 9.5 erforderlich. Die aktuelle signierte Freigabe verlangt mindestens Upgrade 0.2.10. Die frühere Pilot-EXE 0.2.1 und der öffentliche Standarddownload 0.2.0 eignen sich nicht für diesen direkten Weg.

**Wenn Upload-Dateien vorhanden sind:** Am Altgerät zunächst die Übertragung auf **Offline** stellen und klären, welche Dateien bereits gesendet wurden. Version 1 führt noch keine zuverlässigen Übertragungsnachweise. Alle Dateien werden gesichert und wiederhergestellt; Offline bleibt aktiv. Erst nach Prüfung des Versandstatus die Übertragung wieder einschalten. Der Assistent erzeugt keine erfundenen Versandbestätigungen.

## Test durchführen

Die bereitgestellte Test-EXE verwenden; oben erscheint **„LABOR“**. Die vollständige Gerätesicherung aktiviert lassen und die [Schrittanleitung](guide.md) befolgen. Der Gerätebetreuer muss die Boot-Taster- und Kabelfolge an der tatsächlichen Trägerplatine bestätigen. Seriennummer, Ausgangs-/Zielversion, Sicherung, Ergebnis und Rückfall-Boot dokumentieren.

Eine erfolgreiche Pilotmigration ist noch keine allgemeine Freigabe für andere Geräte oder Ausgangsversionen.

## Ausgangsversion 9.6

Ab **0.2.12** unterstützt der Pilot auch das geprüfte 9.6-Anwendungspaket Revision 3. Die automatische Suche zeigt identifizierbare DLTNGs auch dann an, wenn ihre Version noch kein freigegebenes Sicherungsprofil besitzt; erst „Gerät prüfen“ entscheidet über die Zulässigkeit.

Nach Neuinstallation oder Wechsel von 1.0 auf 9.6 einen **neuen Vorgang mit neuer Sicherung** beginnen. Keine frühere Sitzung einer anderen Installation übernehmen; bisherige Sicherungsordner behalten. Die zusätzliche UPS-Freigabe gilt für das registrierte 32-GB-Testgerät, exakt 9.6 und App ab 0.2.12. Das Image upgrade.2 bleibt bytegleich.

Lesende Geräteprüfung, automatische Suche und Sicherungsvorprüfung sind erfolgreich. Isolierte Wiederherstellung einschließlich Datenbankzeilen, Konfiguration, Dateiprüfsummen und wiederholtem Import bestanden; der vollständige physische 9.6-Upgradeversuch bleibt offen. Alte NFC-Konfigurationen werden archiviert. Bei vorhandenen Upload-Dateien ohne Versandnachweise ist Offline-Modus erforderlich. Die 9.6-USB-Wartezeit wird als Einstellung erhalten; das Zielsystem 10.x verwendet eine andere USB-Einbindelogik, die diese feste Wartezeit derzeit nicht auswertet.

