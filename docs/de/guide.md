# Schritt für Schritt

Diese Anleitung beschreibt den vorgesehenen Ablauf. In der aktuellen Entwicklungsausgabe lässt er sich vollständig im **Demomodus** ausprobieren. Ein echter Flashvorgang setzt ein ausdrücklich freigegebenes Gerät und ein passendes signiertes Image voraus.

## Vor dem Start

- Windows 11 x64 verwenden; ein Gerät pro Vorgang.
- Netzteil, Ethernet-Kabel und das zur DLTNG-Trägerplatine passende USB-Programmierkabel bereithalten.
- Einen lokalen Arbeitsordner mit genügend Platz wählen. Zusätzlich zur Datensicherung benötigen Image und optionale vollständige Gerätesicherung mehrere Gigabyte; die vollständige Kopie allein umfasst etwa 16–32 GB.
- Internet für den Image-Download bereithalten. Das Image wird vor dem Anhalten des Geräts vollständig heruntergeladen und geprüft.
- Für USB-Treiber sowie Datenträger- und Netzwerkeinstellungen können Windows-Administratorrechte erforderlich sein.

## Sprache wählen

Oben rechts auf die **Landesflagge mit Sprachname** klicken und **Deutsch** oder **English** wählen. Alternativ öffnet **Alt+L** die Auswahl. Der Wechsel ist auch während einer Aktion möglich und setzt weder Fortschritt noch Eingaben zurück. Die Auswahl wird im Arbeitsordner gespeichert.

![Sprachwahl und Startseite](assets/ui-de.png)

## 1 · Vorbereiten

`DLTNG-Upgrade.exe` starten. Bei Bedarf den Arbeits- und Sicherungsordner wählen und **„USB-Treiber einrichten“** verwenden. **„Vorbereitung prüfen“** kontrolliert die PC-Voraussetzungen. Zum gefahrlosen Kennenlernen **„Demo ausprobieren“** wählen.

## 2 · Gerät verbinden

PC und DLTNG an dasselbe LAN anschließen. Die IP-Adresse des DLTNG eingeben oder **„DLTNG im Netzwerk suchen“** wählen. **„Gerät prüfen“** liest Gerätekennung, Hardware und Version.

Bei einem direkten Ethernet-Kabel den ausdrücklich dafür verwendeten PC-Adapter auswählen. Bei fester Geräteadresse auch die Netzgröße angeben, beispielsweise `192.168.1.25/24`. Für ein Gerät mit DHCP steht die begrenzte Hilfe **„Direktverbindung: DLTNG ohne feste IP finden“** zur Verfügung. Diese nur auf einer direkten Kabelverbindung ohne Firmennetz oder Switch aktivieren.

## 3 · Upgrade laden

**„Upgrade herunterladen“** wählen. UPS prüft Geräteberechtigung und passende freigegebene Version. Die Anwendung kontrolliert Signatur, Größe und Prüfsummen. Bis zum Ende dieses Schritts die Internetverbindung bestehen lassen.

Eine fehlende Freigabe ist kein überspringbarer Hinweis. Für Laborgeräte ist eine gesonderte, an die Seriennummer gebundene Freigabe erforderlich.

## 4 · Sicherung wählen

Sicherungsordner kontrollieren. Die verpflichtende Datensicherung bleibt immer aktiv. Die zusätzliche **vollständige Gerätesicherung** ist vorausgewählt; sie ermöglicht später die Rückkehr zum ursprünglichen System. **„Auswahl übernehmen“** bestätigt die Wahl.

## 5 · Daten sichern

Karten und USB-Datenträger entfernen und das Ende laufender Vorgänge abwarten. **„Daten sichern“** hält relevante Schreibdienste an, erstellt die Sicherung und überträgt sie auf den PC. Erst eine vollständig geprüfte Sicherung erlaubt den nächsten Schritt.

Gesichert werden die bekannten Konfigurationen, Nutzdateien, lokalen Datenbanken, Übertragungsnachweise und Geräteidentitätsdaten. Unbekannte dauerhafte Datenbestände stoppen den Ablauf zur Klärung. Bei externen Datenbankservern werden die Verbindungseinstellungen übernommen; deren Daten werden nicht zurückgeschrieben.

![Datensicherung](assets/backup.png)

## 6 · USB vorbereiten

**„Gerät herunterfahren“** wählen. Anschließend die **freigegebene Anleitung für die tatsächliche Trägerplatine** zum Boot-Taster und Programmierkabel befolgen. Danach **„USB-Gerät erkennen“** wählen.

!!! note "Symbolische Bilder"

    Die Bilder zeigen keine verbindliche Tasterposition oder Steckerbelegung. Reale Anschlussfotos und die genaue Handgriffreihenfolge müssen für die Kundenfreigabe noch am Gerät geprüft werden. Bei Unklarheit hier anhalten und den Gerätebetreuer hinzuziehen.

## 7 · Neuinstallation bestätigen

Gerätekennung, Zielversion und Sicherungsstatus kontrollieren. Nur für das richtige Gerät die Bestätigung aktivieren und **„Neuinstallation vorbereiten“** wählen. Eine ausgewählte vollständige Gerätesicherung wird vor dem Überschreiben erstellt und geprüft.

## 8 · System schreiben

**„System jetzt schreiben“** startet den Schreibvorgang. Stromversorgung und USB-Verbindung bestehen lassen. Das Programm liest den gesamten geschriebenen Bereich zurück und vergleicht ihn mit dem Image. Währenddessen ist kein normaler Abbruch vorgesehen.

Bei Unterbrechung den [geführten Wiederanlauf](troubleshooting.md) verwenden. Eine ursprüngliche vollständige Gerätesicherung wird bei Wiederholung nicht überschrieben.

## 9 · Daten wiederherstellen

Programmierkabel entfernen, Boot-Taster freigeben und DLTNG normal starten. Die angezeigte Zieladresse verwenden beziehungsweise den direkten Servicezugang einrichten. **„Daten wiederherstellen“** verbindet sich mit demselben Gerät, prüft den Sitzungsnachweis und importiert die Sicherung.

## 10 · Abschluss

Zuerst **„Netzwerkeinstellungen übernehmen“**, danach **„Abschluss prüfen“** wählen. Erst nach Prüfung von Dateien, Datenbanken, Einstellungen, Diensten und Weboberflächen wird der Vorgang erfolgreich abgeschlossen. Über **„DLTNG öffnen“** lässt sich die Weboberfläche öffnen.

Den Sicherungsordner aufbewahren. Er enthält Sicherung, Sitzungszustand und Protokoll und wird für einen Wiederanlauf benötigt.

## Wieder aufnehmen oder zurückkehren

Über **„Vorgang öffnen“** die `session.json` im bisherigen Arbeitsordner auswählen. Das Programm setzt an der passenden Stelle fort. Wenn das Altgerät nach der Sicherung wieder normal gearbeitet hat, ist eine neue Sicherung notwendig. Eine vorhandene vollständige Gerätesicherung kann über **„Ursprüngliches System wiederherstellen“** auf dasselbe Gerät zurückgeschrieben werden; danach muss dessen Start geprüft werden.
