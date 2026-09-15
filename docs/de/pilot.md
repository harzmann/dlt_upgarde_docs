# Einen Pilottest vorbereiten

Eine gesonderte Testausgabe ab Version 0.2.1 kann ein signiertes Laborimage über UPS beziehen. Die Freigabe gilt ausschließlich für eingetragene CM4-Seriennummern bis zum festgelegten Ablaufdatum. Die allgemeine Hardwarefreigabe bleibt aus. Der öffentliche Standarddownload 0.2.0 enthält diese konkrete Pilotkonfiguration nicht.

## Vorbereitung durch den Gerätebetreuer

1. Tatsächliche CM4-Seriennummer, eMMC-Größe und installierte Anwendungsversion auslesen.
2. Das Gerät beim richtigen UPS-Kunden eintragen und dessen wirksame Berechtigung prüfen.
3. Eine Testausgabe mit öffentlichem Signaturschlüssel und genau dieser Testseriennummer bereitstellen.
4. Das passende Image signieren: Hardwareprofil, erlaubte Ausgangsversionen, Seriennummer und Ablaufdatum gehören zur Signatur.
5. In UPS Pilotbetrieb aktivieren, Image importieren und **„Für diese Testgeräte freigeben“** wählen.
6. Download, Prüfsummen und Ablehnung anderer Geräte prüfen. Das Gerät dabei noch nicht anhalten oder flashen.

## Ausgangsversion 1.0

**Ein direktes Upgrade aus DLTNG 1.0 ist noch nicht geprüft.** Die App hält diese Version vor Installation eines Sicherungshelfers mit `SRC-001` an. Das Originalimage muss zunächst auf Datenstruktur, Python-Version und Datenbankmigration geprüft werden.

Als vorbereitender Weg kann das vorhandene Softwareupdate von 1.0 auf 9.5 verwendet werden. Erst nach Kontrolle der tatsächlich installierten Version 9.5 beginnt der Image-Upgrade-Test. Die Freigabe einer Versionsnummer allein ersetzt keine Migrationsprüfung.

## Test durchführen

Die bereitgestellte Test-EXE verwenden; oben erscheint **„LABOR“**. Die vollständige Gerätesicherung aktiviert lassen und die [Schrittanleitung](guide.md) befolgen. Der Gerätebetreuer muss die Boot-Taster- und Kabelfolge an der tatsächlichen Trägerplatine bestätigen. Seriennummer, Ausgangs-/Zielversion, Sicherung, Ergebnis und Rückfall-Boot dokumentieren.

Eine erfolgreiche Pilotmigration ist noch keine allgemeine Freigabe für andere Geräte oder Ausgangsversionen.
