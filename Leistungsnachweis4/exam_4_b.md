# Leistungsnachweis 4 b - Analyse - Pizza Place Sales

## Intro

Diese Aufgabe befasst sich mit der Analyse mittels SQL.
Das heißt, weg vom Data Warehouse hin zur Datenanalyse.
Hierbei liegt der Fokus vor allem auf `SELECT` Statements.

## Vorbereitung

> Wir laden die Daten nun neu rein. Dabei sind diesmal keine künstlichen Fehler mehr enthalten.  
> Es kann dennoch vorkommen, dass Werte leer bleiben. Dies muss bei der Analyse berücksichtigt werden.

- Die Datei `order_details.csv` neu in `land`.`order_details` laden
- Die Datei `orders.csv` neu in `land`.`orders` laden
- Die Datei `pizza_types.csv` neu in `land`.`pizza_types` laden
- Die Datei `pizzas.csv` neu in `land`.`pizzas` laden

## Aufgaben / Fragestellungen

> Anforderung: Jede Fragestellung soll mit der entsprechenden SQL-Query und darunter als Kommentar die Antwort liefern.

### Normale Auswertung

- Wie viele Kunden haben wir jeden Tag?

```sql
SELECT land.orders.`date` , COUNT(land.orders.order_id) AS datesum
FROM land.orders
GROUP BY land.orders.`date`
ORDER BY datesum DESC

-- Antwort: 
```

- Besitzt die Pizzeria Stoßzeiten?
  - Bei welchen Uhrzeiten handelt es sich um Stoßzeiten?

```sql
-- Query:
-- Antwort:
```

- Wie viele Pizzas sind üblicherweise in einer Bestellung?
  - Durchschnitt der Bestellungen
  - Median der Bestellungen

```sql
-- Query:
-- Antwort:
```

- Wie viel Geld hat die Pizzeria verdient?
  - dieses Jahr
  - pro Monat

```sql
-- Query:
-- Antwort:
```

- Welche Pizzas sind
  - pro Kategorie (Beispiel: Chicken, Supreme, ..)
    - am Beliebtesten
    - am Unbeliebtesten
  - pro Pizzatyp (Beispiel: bbq_ckn)
    - am Beliebtesten
    - am Unbeliebtesten
  - pro Pizza (Beispiel: bbq_ckn_s)
    - am Beliebtesten
    - am Unbeliebtesten

```sql
-- Query:
-- Antwort:
```

### Window Functions

> Oftmals möchte man für eine aktuelle Zeile die Vorgänger- oder Folgezeilen berücksichtigen.  
> Hierfür wurden sogenannte Window-Functions implementiert.

#### Einarbeitung Window Functions

Aufgabe:

Arbeite dich mit folgender URL in Window-Functions ein: [Window Functions Overview](https://mariadb.com/kb/en/window-functions-overview/)

#### Anwendung

1. Aggregiere Umsatz pro Tag
2. Berechne die Differenz des Umsatzes zum Vortag

```sql
-- Query:
-- Antwort:
```
