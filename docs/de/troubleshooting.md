# Hilfe bei Problemen

Die Fehlermeldung nennt das Problem und einen nächsten Schritt. Sicherungen und Sitzungszustand bleiben erhalten. Den angezeigten **Fehlercode** zusammen mit dem Sitzungsordner für den Support bereithalten.

| Situation | Nächster Schritt |
|---|---|
| Gerät nicht gefunden | IP-Adresse, Netzwerkkabel und Stromversorgung prüfen; Adresse bei Bedarf manuell eingeben. |
| Kein passendes freigegebenes Image | Geräteberechtigung und UPS-Freigabe prüfen lassen. Die Sperre nicht umgehen. |
| `REL-001`: keine Kundenfreigabe | Entwicklungsausgabe im Demomodus verwenden; echte Tests benötigen die eingerichtete Laborfreigabe. |
| `IMG-008`: vorbereitetes Image fehlt oder wurde verändert | Zum Download zurückkehren und das Image erneut laden. |
| Zu wenig Platz | Größeren lokalen Arbeitsordner auswählen; Sicherungen nicht löschen, solange der Vorgang offen ist. |
| Unbekannte Daten oder Datenbanken | Datenprofil beziehungsweise Migrationsregel prüfen lassen, bevor geflasht wird. |
| USB-Gerät fehlt oder ist mehrdeutig | Freigegebene Geräteanleitung, Boot-Taster, Programmierkabel und Treiber prüfen; nur das beabsichtigte Gerät anschließen. |
| Laufwerk wird verwendet | Explorer-Fenster oder andere Programme schließen, die auf das DLTNG-Laufwerk zugreifen. |
| Netzwerk nach Neustart nicht erreichbar (NET-003) | Start abwarten, Strom und LAN prüfen. Im Firmennetz die aktuelle Geräteadresse eingeben; siehe Hinweise zu Schritt 09 unten. |

## Korrekturen für den aktuellen Test

**Die für Ihren Test bereitgestellte Pilotversion verwenden.** Seit 0.2.6 sind Zugriffsfehler beim Austausch des Windows-Fortschritts behoben; laufende oder bereits erfolgreich abgeschlossene Systemhelfer können wieder aufgenommen werden. Die Oberfläche zeigt erledigte Schritte über **Zurück** an, ohne sie erneut auszuführen. Die kompakte Ansicht hält die Hauptaktion sichtbar; der Bildhinweis entfällt. **Diagnose** erklärt die Fehlercodes, exportiert ein bereinigtes ZIP und bietet nach Bestätigung den Versand an UPS an.

Lassen Sie das Gerät angeschlossen, solange ein Systemhelfer arbeitet. Falls ein Versionswechsel erforderlich ist, erst nach dessen Abschluss die alte EXE schließen, die bereitgestellte Pilotversion starten und **„Vorgang öffnen“** wählen. Die aktuelle `session.json` verwenden. Bei mehreren Vorgängen helfen Datum, Fortschritt und Ordner bei der Auswahl; der neueste steht oben. Bereits geprüfter Download und Sicherung bleiben erhalten. Ein erfolgreicher Schreibnachweis führt direkt zur Datenwiederherstellung. Falls das Altgerät nach der Sicherung wieder normal betrieben wurde, ist dagegen eine neue Sicherung erforderlich.

Im vorhandenen LAN genügt die normale Geräteverbindung. Die direkte Serviceverbindung ist für ein eigenes Ethernet-Kabel zwischen PC und DLTNG vorgesehen. Administratorrechte fordert die App bei der jeweiligen Windows-Aktion an.


## Download unterbrochen

Erneut versuchen. UPS prüft die Berechtigung erneut; ein geeigneter Teil-Download kann fortgesetzt werden. Das Gerät wird erst nach vollständigem Download und Prüfung angehalten.

## Sicherung unterbrochen

Keine unvollständige Datei als gültige Sicherung verwenden. Die Sitzung öffnen und den geführten Weg befolgen. Wird das Altgerät wieder für den Normalbetrieb freigegeben, vor dem Flashen erneut sichern.

## Schreiben unterbrochen

Arbeitsordner behalten und zuerst **Schreibstatus wieder aufnehmen**. Eine Fehlermeldung der Oberfläche bedeutet nicht zwingend, dass der Systemhelfer angehalten wurde. Während er arbeitet, Strom/USB angeschlossen lassen und keinen zweiten Versuch starten. Ein gespeicherter Erfolg führt zur Wiederherstellung ohne erneutes Schreiben. Erst bei tatsächlich fehlgeschlagenem/beendetem Helfer dem Wiederanlauf folgen, das USB-Gerät neu erkennen und das gesamte Image erneut schreiben und prüfen lassen.

## Schritt 09: Gerät nach Neustart nicht gefunden (NET-003)

1. Den bisherigen Vorgang und den Sicherungsordner behalten. Eine fehlende Netzwerkverbindung allein erfordert kein erneutes Schreiben des Systems.
2. USB-Admin entfernen, Admin-Taster freigeben und das Gerät entsprechend der Anleitung normal starten.
3. Im **Firmennetz / am Switch** die aktuelle, bestätigte IP-Adresse des DLTNG im Adressfeld eingeben und **Daten wiederherstellen** drücken. Nach dem Neuinstallieren kann DHCP eine andere Adresse vergeben.
4. **Direkte Serviceverbindung einrichten** nur verwenden, wenn das DLTNG mit einem eigenen Netzwerkkabel direkt an diesem PC angeschlossen ist. Diese Funktion ist nicht für den gemeinsamen Firmenanschluss vorgesehen.

Bleiben Display und Netzwerk im bisherigen Pilotimage vollständig aus, kann der inzwischen erkannte Startkonfigurationsfehler vorliegen. Das muss über die Diagnose geprüft werden; NET-003 allein beweist diese Ursache nicht. Den Sicherungsordner behalten und den Support zur gezielten Startkorrektur hinzuziehen. Der Fix ist am 32-GB-Testgerät geprüft und im neuen Pilotimage upgrade.2 enthalten. Für neue Durchläufe App 0.2.10 und dieses Image verwenden. Eine neue EXE allein repariert kein bereits geschriebenes altes Image; siehe [Image-Changelog](image-changelog.md).

## Wiederherstellung unterbrochen

Die bisherige Sitzung öffnen und dasselbe Gerät wieder verbinden. Geschäftliche Dienste bleiben während der Wiederherstellung angehalten. Dateikonflikte oder abweichende Datenbankbestände werden zur Klärung gemeldet.

## Zurück zum bisherigen System

Wenn eine geprüfte vollständige Gerätesicherung vorhanden ist, bietet der Assistent deren Rückschreiben und die anschließende Startprüfung an. Ohne diese vollständige Kopie besteht der Wiederherstellungsweg aus der erneuten Installation eines freigegebenen Images und dem Import der verpflichtenden Datensicherung.

## Sprache und Arbeitsordner

Die Sprachwahl gilt für den Arbeitsordner. Bei einem neuen Ordner startet der Assistent standardmäßig auf Deutsch. Die Flagge oben rechts wechselt auf Englisch. Eine Meldung über nicht speicherbare Spracheinstellungen bedeutet, dass Schreibrechte für diesen Ordner geprüft werden müssen.

## Fehlercodes und Diagnosepaket

Oben **Diagnose** wählen, nach dem Fehlercode suchen und den Handlungshinweis lesen. Der letzte technische Fehler lässt sich dort einsehen. **Diagnosepaket im Arbeitsordner erstellen** exportiert eine ZIP-Datei mit zeitlichem Verlauf einschließlich erreichbarer früherer Vorgänge desselben Geräts. Frühere Versionen haben technische Details teilweise nicht aufgezeichnet; diese können nicht nachträglich ergänzt werden.

Das Paket enthält Gerätekennung, Rechnerpfade, Prüfergebnisse und bereinigte App-/Systemhelfer-Protokolle. Passwörter und Sitzungstoken werden entfernt; Nutzdateien, Datenbanken und Images werden nicht beigefügt. **Diagnosepaket an UPS senden** verlangt eine ausdrückliche Bestätigung. Internet und aktuelle Geräte-/Imagefreigabe sind erforderlich. Bei Fehlern bleibt das ZIP lokal erhalten.

UPS bestätigt den Empfang mit einer Prüfsummenquittung. Pakete sind für angemeldete Administratoren unter **System-Images → Upgrade-Diagnose** verfügbar, werden 30 Tage aufbewahrt und nicht automatisch mit KI ausgewertet. Pro ZIP sind maximal 20 MiB zulässig.

| Code | Bedeutung und nächster Schritt |
|---|---|
| `APP-001`, `WIN-099` | Unerwarteter App-/Systemhelferfehler. Bei Schreibphase zuerst Status wieder aufnehmen; Diagnosepaket erstellen. |
| `WIN-010` | Windows-Administratorabfrage abgebrochen. Erneut starten und die eigene DLTNG-App freigeben. |
| `WIN-013` | Ein Systemhelfer schreibt bereits. Angeschlossen lassen, dessen Status wieder aufnehmen. |
| `WIN-016` | Systemhelfer ohne vollständiges Ergebnis beendet. Geführten Wiederanlauf verwenden. |
| `SES-007` | Schreibnachweis gehört nicht zur Sitzung. Richtige Sitzung wählen; Support einschalten. |
| `DIA-001` | Diagnosepaket über 20 MiB. Lokal behalten und Support kontaktieren. |
| `DIA-002` | UPS hat den Upload nicht angenommen. Lokales ZIP behalten, Verbindung und Freigabe prüfen. |
