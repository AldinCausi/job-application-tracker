# Bewerbungsverwaltung mit Python und SQLite

Dieses Projekt ist eine einfache Konsolenanwendung zur Verwaltung von Bewerbungen. Die Daten werden lokal in einer SQLite-Datenbank gespeichert. Nutzer können Bewerbungen hinzufügen, anzeigen, aktualisieren und löschen.

## Funktionen

* Hinzufügen neuer Bewerbungen
* Anzeige aller gespeicherten Bewerbungen
* Aktualisierung des Bewerbungsstatus
* Validierte Statusübergänge
  * APPLIED → INTERVIEWED
  * APPLIED → REJECTED
  * INTERVIEWED → ACCEPTED
  * INTERVIEWED → REJECTED
* Filtern von Bewerbungen nach Status
* Löschen von Bewerbungen anhand von ID, Unternehmen oder Rolle
* Persistente Datenspeicherung mittels SQLite

## Verwendete Technologien

* Python 3
* SQLite (`sqlite3`)
* Konsolenbasierte Benutzeroberfläche (CLI)

## Projektstruktur

Die Anwendung verwendet eine lokale SQLite-Datenbank (`bewerbungen.db`) zur Speicherung der Bewerbungsdaten. Jede Bewerbung enthält folgende Informationen:

* **Company**: Name des Unternehmens
* **Role**: Bezeichnung der Stelle
* **Status**: Aktueller Bewerbungsstatus (Standardwert: `pending`)

## Ausführung des Programms

Repository klonen:

```bash
git clone <repository-url>
cd <repository-name>
```

Programm starten:

```bash
python main.py
```

## Ziel des Projekts

Das Projekt wurde entwickelt, um grundlegende Kenntnisse im Umgang mit relationalen Datenbanken in Python zu vertiefen. Dabei werden insbesondere folgende Konzepte angewendet:

* Datenbankoperationen mit SQLite
* CRUD-Funktionalitäten (Create, Read, Update, Delete)
* Strukturierung eines Python-Programms mit Funktionen
* Entwicklung einer einfachen terminalbasierten Anwendung
