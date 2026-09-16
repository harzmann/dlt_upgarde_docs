# Schritt für Schritt

Diese Anleitung beschreibt den vorgesehenen Ablauf. In der aktuellen Entwicklungsausgabe lässt er sich vollständig im **Demomodus** ausprobieren. Ein echter Flashvorgang setzt ein ausdrücklich freigegebenes Gerät und ein passendes signiertes Image voraus.

Diese Anleitung berücksichtigt die **Testausgabe 0.2.5**, einschließlich der neuen Bestätigungsanzeige, Anschlussbilder und Explorer-Unterdrückung. Der öffentliche Standarddownload bleibt 0.2.0; die Testausgabe wird für das freigegebene Laborgerät bereitgestellt.

## Vor dem Start

- Windows 11 x64 verwenden; ein Gerät pro Vorgang.
- Netzteil, Ethernet-Kabel und das zur DLTNG-Trägerplatine passende USB-Programmierkabel bereithalten.
- Einen lokalen Arbeitsordner mit genügend Platz wählen. Zusätzlich zur Datensicherung benötigen Image und optionale vollständige Gerätesicherung mehrere Gigabyte; die vollständige Kopie allein umfasst etwa 16–32 GB.
- Internet für den Image-Download bereithalten. Das Image wird vor dem Anhalten des Geräts vollständig heruntergeladen und geprüft.
- Für USB-Treiber sowie Datenträger- und Netzwerkeinstellungen können Windows-Administratorrechte erforderlich sein.

## Sprache wählen

Oben rechts auf die **Landesflagge mit Sprachname** klicken und **Deutsch** oder **English** wählen. Alternativ öffnet **Alt+L** die Auswahl. Der Wechsel ist auch während einer Aktion möglich und setzt weder Fortschritt noch Eingaben zurück. Die Auswahl wird im Arbeitsordner gespeichert.

![Sprachwahl und Startseite](assets/ui-de.png)

*Abbildung: Demomodus der Testausgabe 0.2.4.*

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

![Symbolische DLTNG-Front nach Originalfoto](assets/dltng-front-v1.png)

## 6 · USB vorbereiten

**„Gerät herunterfahren“** wählen. Anschließend die **freigegebene Anleitung für die tatsächliche Trägerplatine** zum Boot-Taster und Programmierkabel befolgen. Danach **„USB-Gerät erkennen“** wählen.

### Die Anschlüsse erkennen

![DLTNG-Anschlüsse nach Originalfoto, mit Nummern](assets/dltng-connectors-numbered.png)

Von links nach rechts:

| Nummer | Anschluss |
|---|---|
| 1 | Stromversorgung, mit gestecktem schwarzem Kabel |
| 2 | RJ45 Ethernet / Netzwerk, mit gestecktem blauem Kabel |
| 3 | Zwei übereinanderliegende USB-Anschlüsse |
| 4 | HDMI |
| 5 | USB-Admin für das Programmierkabel, mit gestecktem rotem Kabel |
| 6 | Versenkter Admin-Taster; lässt sich leicht mit einem Kugelschreiber betätigen |

In der App öffnet **„Anschlüsse größer anzeigen“** die Detailansicht. Die Legende wechselt mit der Sprache. Die Symbolbilder basieren auf den gelieferten Fotos dieses DLTNG. Die genaue Folge von Tasterbetätigung, Stromversorgung und Kabelanschluss ist weiterhin anhand der Geräteanleitung am realen Gerät zu prüfen.

### Automatisches Explorer-Fenster verhindern

Während der USB-Schritte den Assistenten im Vordergrund lassen. Ab Testausgabe **0.2.4** unterdrückt er dann das automatische Öffnen der Bootpartition, auch bei geöffneter Anschlussvergrößerung und während der Rückfallwiederherstellung. Dafür sind keine dauerhaften Windows-Einstellungen erforderlich. Bereits offene Explorer-Fenster bleiben geöffnet. Der Demomodus unterdrückt AutoPlay nicht.

Windows stellt diese [AutoPlay-Abfrage an das Vordergrundfenster](https://learn.microsoft.com/en-us/windows/win32/shell/autoplay-reg). Wenn eine andere Anwendung im Vordergrund ist, kann sich der Explorer weiterhin öffnen.

## 7 · Neuinstallation bestätigen

Gerätekennung, Zielversion und Sicherungsstatus kontrollieren. Nur für das richtige Gerät das Kästchen **„Gerätekennung und Sicherung stimmen“** aktivieren. Danach wird **„Weiter zur Neuinstallation“** freigegeben. Dieser Klick öffnet Schritt 8; er startet noch keinen Schreibvorgang.

![Sichtbare Bestätigung in Testausgabe 0.2.5](assets/confirmation-de.png)

Fehlt das Häkchen, bleibt die Schaltfläche grau und der Status fordert zur Bestätigung auf. Vor dem eigentlichen Start steht der Fortschritt auf null.

## 8 · System schreiben

**„System jetzt schreiben“** startet den Vorgang. Eine ausgewählte vollständige Gerätesicherung wird zuerst erstellt und geprüft; danach folgen Schreiben und Rücklesen. Die jeweilige Phase wird als Text angezeigt, bei messbaren Dateioperationen zusätzlich mit Prozentangabe. Stromversorgung und USB-Verbindung bestehen lassen. Das Programm liest den gesamten geschriebenen Bereich zurück und vergleicht ihn mit dem Image. Währenddessen ist kein normaler Abbruch vorgesehen.

Bei Unterbrechung den [geführten Wiederanlauf](troubleshooting.md) verwenden. Eine ursprüngliche vollständige Gerätesicherung wird bei Wiederholung nicht überschrieben.

## 9 · Daten wiederherstellen

Programmierkabel entfernen, Boot-Taster freigeben und DLTNG normal starten. Die angezeigte Zieladresse verwenden beziehungsweise den direkten Servicezugang einrichten. **„Daten wiederherstellen“** verbindet sich mit demselben Gerät, prüft den Sitzungsnachweis und importiert die Sicherung.

## 10 · Abschluss

Zuerst **„Netzwerkeinstellungen übernehmen“**, danach **„Abschluss prüfen“** wählen. Erst nach Prüfung von Dateien, Datenbanken, Einstellungen, Diensten und Weboberflächen wird der Vorgang erfolgreich abgeschlossen. Über **„DLTNG öffnen“** lässt sich die Weboberfläche öffnen.

Den Sicherungsordner aufbewahren. Er enthält Sicherung, Sitzungszustand und Protokoll und wird für einen Wiederanlauf benötigt.

## Wieder aufnehmen oder zurückkehren

Über **„Vorgang öffnen“** die `session.json` im bisherigen Arbeitsordner auswählen. Das Programm setzt an der passenden Stelle fort. Wenn das Altgerät nach der Sicherung wieder normal gearbeitet hat, ist eine neue Sicherung notwendig. Eine vorhandene vollständige Gerätesicherung kann über **„Ursprüngliches System wiederherstellen“** auf dasselbe Gerät zurückgeschrieben werden; danach muss dessen Start geprüft werden.
