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
| Netzwerk nach Neustart nicht erreichbar | Start abwarten, Strom und LAN prüfen; den vorgesehenen Servicezugang verwenden. |

## Download unterbrochen

Erneut versuchen. UPS prüft die Berechtigung erneut; ein geeigneter Teil-Download kann fortgesetzt werden. Das Gerät wird erst nach vollständigem Download und Prüfung angehalten.

## Sicherung unterbrochen

Keine unvollständige Datei als gültige Sicherung verwenden. Die Sitzung öffnen und den geführten Weg befolgen. Wird das Altgerät wieder für den Normalbetrieb freigegeben, vor dem Flashen erneut sichern.

## Schreiben unterbrochen

Arbeitsordner unverändert aufbewahren. Gerät anhand der freigegebenen Anleitung wieder in den Programmiermodus bringen, die gespeicherte Sitzung öffnen und das Image vollständig neu schreiben lassen. Anschließend wird wieder vollständig zurückgelesen. Nicht versuchen, an einer vermuteten Schreibposition manuell fortzusetzen.

## Wiederherstellung unterbrochen

Die bisherige Sitzung öffnen und dasselbe Gerät wieder verbinden. Geschäftliche Dienste bleiben während der Wiederherstellung angehalten. Dateikonflikte oder abweichende Datenbankbestände werden zur Klärung gemeldet.

## Zurück zum bisherigen System

Wenn eine geprüfte vollständige Gerätesicherung vorhanden ist, bietet der Assistent deren Rückschreiben und die anschließende Startprüfung an. Ohne diese vollständige Kopie besteht der Wiederherstellungsweg aus der erneuten Installation eines freigegebenen Images und dem Import der verpflichtenden Datensicherung.

## Sprache und Arbeitsordner

Die Sprachwahl gilt für den Arbeitsordner. Bei einem neuen Ordner startet der Assistent standardmäßig auf Deutsch. Die Flagge oben rechts wechselt auf Englisch. Eine Meldung über nicht speicherbare Spracheinstellungen bedeutet, dass Schreibrechte für diesen Ordner geprüft werden müssen.
