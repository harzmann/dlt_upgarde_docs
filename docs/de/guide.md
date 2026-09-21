# Schritt für Schritt

Diese Anleitung beschreibt den vorgesehenen Ablauf. In der aktuellen Entwicklungsausgabe lässt er sich vollständig im **Demomodus** ausprobieren. Ein echter Flashvorgang setzt ein ausdrücklich freigegebenes Gerät und ein passendes signiertes Image voraus.

Diese Anleitung berücksichtigt die **Testausgabe 0.2.10**, einschließlich eindeutiger Klickanweisungen, blinkender Warnanzeige, Anschlussbilder und Explorer-Unterdrückung. Der öffentliche Standarddownload bleibt 0.2.0; die Testausgabe wird für das freigegebene Laborgerät bereitgestellt.

## Vor dem Start

- Windows 11 x64 verwenden; ein Gerät pro Vorgang.
- Netzteil, Ethernet-Kabel und das zur DLTNG-Trägerplatine passende USB-Programmierkabel bereithalten.
- Einen lokalen Arbeitsordner mit genügend Platz wählen. Zusätzlich zur Datensicherung benötigen Image und optionale vollständige Gerätesicherung mehrere Gigabyte; die vollständige Kopie allein umfasst etwa 16–32 GB.
- Internet für den Image-Download bereithalten. Das Image wird vor der Datensicherung vollständig heruntergeladen und geprüft. Die Geschäftsdienste werden ab der Geräteprüfung gesperrt.
- Für USB-Treiber sowie Datenträger- und Netzwerkeinstellungen können Windows-Administratorrechte erforderlich sein.

## Sprache wählen

Oben rechts auf die **Landesflagge mit Sprachname** klicken und **Deutsch** oder **English** wählen. Alternativ öffnet **Alt+L** die Auswahl. Der Wechsel ist auch während einer Aktion möglich und setzt weder Fortschritt noch Eingaben zurück. Die Auswahl wird im Arbeitsordner gespeichert.

![Sprachwahl und Startseite](assets/ui-de.png)

*Abbildung: Demomodus der Testausgabe 0.2.6.*

## 1 · Vorbereiten

`DLTNG-Upgrade.exe` starten. Bei Bedarf den Arbeits- und Sicherungsordner wählen und **„USB-Treiber einrichten“** verwenden. **„Vorbereitung prüfen“** kontrolliert die PC-Voraussetzungen. Zum gefahrlosen Kennenlernen **„Demo ausprobieren“** wählen.

## 2 · Gerät verbinden

PC und DLTNG an dasselbe LAN anschließen. Die IP-Adresse des DLTNG eingeben oder **„DLTNG im Netzwerk suchen“** wählen. Karten und USB-Datenträger entfernen und laufende Vorgänge beenden lassen. **„Gerät prüfen“** liest Gerätekennung, Hardware und Version und aktiviert anschließend die Upgrade-Anzeige mit BUSY.

Über **„Optionen für direkte Kabelverbindung anzeigen“** die zusätzlichen Einstellungen öffnen. Bei einem direkten Ethernet-Kabel den ausdrücklich dafür verwendeten PC-Adapter auswählen. Bei fester Geräteadresse auch die Netzgröße angeben, beispielsweise `192.168.1.25/24`. Für ein Gerät mit DHCP steht die begrenzte Hilfe **„Direktverbindung: DLTNG ohne feste IP finden“** zur Verfügung. Diese nur auf einer direkten Kabelverbindung ohne Firmennetz oder Switch aktivieren.

## 3 · Upgrade laden

**„Upgrade herunterladen“** wählen. UPS prüft Geräteberechtigung und passende freigegebene Version. Die Anwendung kontrolliert Signatur, Größe und Prüfsummen. Bis zum Ende dieses Schritts die Internetverbindung bestehen lassen.

Eine fehlende Freigabe ist kein überspringbarer Hinweis. Für Laborgeräte ist eine gesonderte, an die Seriennummer gebundene Freigabe erforderlich.

## 4 · Sicherung wählen

Sicherungsordner kontrollieren. Die verpflichtende Datensicherung bleibt immer aktiv. Die zusätzliche **vollständige Gerätesicherung** ist vorausgewählt; sie ermöglicht später die Rückkehr zum ursprünglichen System. **„Auswahl übernehmen“** bestätigt die Wahl.

## 5 · Daten sichern

Karten und USB-Datenträger sind bereits entfernt und bleiben bis zum Abschluss entfernt. Das Display zeigt weiterhin die Upgrade-Anzeige und **BUSY**; nicht auf **„Bereit“** warten. Nach dem Download erscheint ab 0.2.10 **„Systemdatei geprüft. Am PC fortfahren“**. Jetzt unten rechts **„Daten sichern“** klicken. Der Assistent sichert und überträgt die Daten und wechselt erst nach vollständiger Prüfung automatisch zu Schritt 06.

Gesichert werden die bekannten Konfigurationen, Nutzdateien, lokalen Datenbanken, Übertragungsnachweise und Geräteidentitätsdaten. Unbekannte dauerhafte Datenbestände stoppen den Ablauf zur Klärung. Bei externen Datenbankservern werden die Verbindungseinstellungen übernommen; deren Daten werden nicht zurückgeschrieben.

![Symbolische DLTNG-Front nach Originalfoto](assets/dltng-front-v1.png)

## 6 · USB vorbereiten

**„Gerät herunterfahren“** wählen und warten, bis das Display vollständig aus ist. Erst danach das Stromkabel abziehen. Das Ausstecken ersetzt kein geregeltes Herunterfahren. Anschließend die **freigegebene Anleitung für die tatsächliche Trägerplatine** zum Boot-Taster und Programmierkabel befolgen. **Nachdem der Strom wieder angeschlossen ist, unten rechts auf „USB-Gerät erkennen“ klicken.** Warten, bis der Assistent automatisch zur Bestätigung weitergeht.

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

Gerätekennung, Zielversion und Sicherungsstatus kontrollieren. Nur für das richtige Gerät das Kästchen **„Gerätekennung und Sicherung stimmen“** aktivieren. Es erscheint ein Hinweis zu Unterbrechung, möglicher Startunfähigkeit, eigenem Risiko und Benutzerkontensteuerung. Nur nach dessen Zustimmung bleibt das Häkchen gesetzt. Danach wird **„Weiter zur Neuinstallation“** freigegeben. Dieser Klick öffnet Schritt 8; er startet noch keinen Schreibvorgang.

![Sichtbare Bestätigung in Testausgabe 0.2.6](assets/confirmation-de.png)

Fehlt das Häkchen, bleibt die Schaltfläche grau und der Status fordert zur Bestätigung auf. Vor dem eigentlichen Start steht der Fortschritt auf null.

## 8 · System schreiben

**„System jetzt schreiben“** startet den Vorgang. Eine ausgewählte vollständige Gerätesicherung wird zuerst erstellt und geprüft; danach folgen Schreiben und Rücklesen. Die jeweilige Phase wird als Text angezeigt, bei messbaren Dateioperationen zusätzlich mit Prozentangabe. Stromversorgung und USB-Verbindung bestehen lassen. Das Programm liest den gesamten geschriebenen Bereich zurück und vergleicht ihn mit dem Image. Währenddessen ist kein normaler Abbruch vorgesehen.

Bei Unterbrechung den [geführten Wiederanlauf](troubleshooting.md) verwenden. Eine ursprüngliche vollständige Gerätesicherung wird bei Wiederholung nicht überschrieben.

### Rote Warnanzeige im PC-Assistenten

Ab Testausgabe 0.2.9 blinkt während laufender Upgrade-Arbeiten oben groß **„UPGRADE-VORGANG LÄUFT - NICHT AUSSCHALTEN!“**. Die Warnung bleibt beim Scrollen sichtbar und auch dann aktiv, wenn der Schreibstatus unklar ist. Gerät, PC und Kabel angeschlossen lassen und die angezeigte Wiederaufnahme verwenden.

Für die ausdrücklich angeleiteten Pausen zum Umstecken und Neustarten nach geprüftem Schreiben wird sie ausgeblendet. Ausschließlich dann den jeweiligen Handgriffen folgen. Nach jedem abgeschlossenen Teilschritt nennt der Status die nächste zu drückende Schaltfläche.

![Warnanzeige im Demomodus, Testausgabe 0.2.9](assets/upgrade-warning-de.png)

## 9 · Daten wiederherstellen

Nach dem vollständig geprüften Schreiben das DLTNG **neu starten**:

1. Stromkabel abziehen.
2. USB-Programmierkabel vollständig entfernen und Admin-Taster loslassen.
3. Zehn Sekunden warten, dann Strom wieder anschließen, ohne den Admin-Taster zu drücken. Das Netzwerkkabel bleibt angeschlossen.
4. Unten rechts **„Daten wiederherstellen“** klicken. Der Assistent wartet auf das Gerät, prüft den Sitzungsnachweis und importiert die Sicherung.

Im Firmennetz die aktuelle Geräteadresse verwenden; ab 0.2.10 wird auch die zuvor bekannte LAN-Adresse versucht. Den direkten Servicezugang nur für ein eigenes Kabel zwischen PC und DLTNG einrichten. Bei dunklem Display oder NET-003 die [Fehlerhilfe](troubleshooting.md) beachten.

## 10 · Abschluss

Zuerst **„Netzwerkeinstellungen übernehmen“**, danach **„Abschluss prüfen“** wählen. Erst nach Prüfung von Dateien, Datenbanken, Einstellungen, Diensten und Weboberflächen wird der Vorgang erfolgreich abgeschlossen. Über **„DLTNG öffnen“** lässt sich die Weboberfläche öffnen.

Den Sicherungsordner aufbewahren. Er enthält Sicherung, Sitzungszustand und Protokoll und wird für einen Wiederanlauf benötigt.

## Wieder aufnehmen oder zurückkehren

Über **„Vorgang öffnen“** die `session.json` im bisherigen Arbeitsordner auswählen. Das Programm setzt an der passenden Stelle fort. Wenn das Altgerät nach der Sicherung wieder normal gearbeitet hat, ist eine neue Sicherung notwendig. Eine vorhandene vollständige Gerätesicherung kann über **„Ursprüngliches System wiederherstellen“** auf dasselbe Gerät zurückgeschrieben werden; danach muss dessen Start geprüft werden.


**Zurück** zeigt bereits erledigte Schritte zur Ansicht. **Weiter** führt vorwärts, ohne Aktionen zu wiederholen. Diagnosepakete und Wiederaufnahme laufender Schreibvorgänge sind in der [Fehlerhilfe](troubleshooting.md) beschrieben.

## Anzeige am DLTNG während des Upgrades

Ab **Gerät prüfen** zeigt das Gerät **BUSY** und den aktuellen Schritt. Vorher Karten und USB-Datenträger entfernen und laufende Vorgänge beenden lassen. Die Anzeige übernimmt die Sprache der zuletzt gestarteten Geräteaktion.

![Wartungsanzeige bei der Datensicherung](assets/display-de.png)

Smartcard, USB, RFID, Upload und der normale Idle-Dienst bleiben gesperrt. Ein eigener Anzeigedienst liest die siebenzeilige `display.log`, ohne Geschäftsdaten zu verarbeiten. Ein Verbindungsverlust gibt die Verarbeitung nicht frei. Am Quellgerät können Sie **Altgerät wieder freigeben und neu sichern** wählen; am Zielgerät ist die vollständige Wiederherstellung mit Abschlussprüfung erforderlich.

Während Ausschalten und USB-Programmiermodus läuft kein Betriebssystem für die Geräteanzeige. In dieser Zeit gelten die Hinweise des PC-Assistenten. Das neue Pilotimage zeigt BUSY ab dem normalen Wartungsstart; bei älteren Images beginnt die Anzeige nach der geprüften SSH-Wiederverbindung. Ab 0.2.8 wird das Vollbild auf dem Originalsystem vor dem Beenden von Chrome geöffnet. Es verdeckt auch die schwebenden Tastatursymbole. Der Assistent prüft, ob die Anzeige tatsächlich sichtbar ist. Dateizähler und Prozentwerte zeigen den Fortschritt des aktuellen Teilschritts; bei Datenbanksicherung und anderen Aufgaben ohne bekannte Gesamtmenge bewegt sich ein Aktivitätsbalken. Nach der Sicherung steht dort „Am PC fortfahren“.

Die Abbildung ist ein Darstellungstest mit 37 % Übertragungsfortschritt. Deutsch und Englisch wurden bei 480 × 320 und 1024 × 600 geprüft. Der Wechsel vom Browser zur Vollbildanzeige wurde auch auf dem Original-1.0-Testgerät bei gesperrten Lesediensten geprüft; anschließend wurde der Normalbetrieb wiederhergestellt. Die vollständige Geräte-Migration bleibt offen.

![Anzeige auf dem Original-1.0-Testgerät](assets/display-cm4.png)

*Gerätetest während der Vorbereitung, 1024 × 600 Pixel.*
