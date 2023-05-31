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

-- Antwort: 115 Kunden
```

- Besitzt die Pizzeria Stoßzeiten?
  - Bei welchen Uhrzeiten handelt es sich um Stoßzeiten?

```sql
-- Query:
SELECT HOUR(land.orders.time) AS hour, COUNT(land.orders.order_id) AS num_orders
FROM land.orders
GROUP BY HOUR(land.orders.time)
ORDER BY num_orders DESC;
-- Antwort:
12 Uhr 2520 Kunden
13 Uhr 2455 Kunden
18 Uhr 2399 Kunden
17 Uhr 2336 Kunden
19 Uhr 2009 Kunden
16 Uhr 1920 Kunden
20 Uhr 1642 Kunden
```

- Wie viele Pizzas sind üblicherweise in einer Bestellung?
  - Durchschnitt der Bestellungen
  - Median der Bestellungen

```sql
-- Query:
-- Average number of pizzas per order
SELECT AVG(num_pizzas) AS avg_pizzas_per_order
FROM (
  SELECT order_id, COUNT(*) AS num_pizzas
  FROM land.order_details
  GROUP BY order_id
) AS pizza_counts;
-- Antwort:
2.2773

-- Median number of pizzas per order  ###########Funktioniert nicht
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY num_pizzas) 
OVER (PARTITION by num_pizzas) AS median_pizzas_per_order
FROM (
  SELECT order_id, COUNT(*) AS num_pizzas
  FROM land.orders
  GROUP BY order_id
) AS pizza_counts;
-- Antwort: ???
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
SELECT orders.`date`, SUM(order_details.quantity * pizzas.price) OVER (PARTITION BY orders.`date`) AS daily_revenue
FROM land.orders
JOIN land.order_details ON orders.order_id = order_details.order_id
JOIN land.pizzas ON order_details.pizza_id = pizzas.pizza_id;

SELECT date, daily_revenue, daily_revenue - LAG(daily_revenue) OVER (ORDER BY date) AS revenue_diff
FROM (
  SELECT land.orders.`date`, SUM(order_details.quantity * pizzas.price) AS daily_revenue
  FROM land.orders
  JOIN land.order_details ON orders.order_id = order_details.order_id
  JOIN land.pizzas ON order_details.pizza_id = pizzas.pizza_id
  GROUP BY date
) AS subquery;

-- Antwort: NIX ANTWORT... KAPUTT
```
