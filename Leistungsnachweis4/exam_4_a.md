# Leistungsnachweis 4 a - Analyse - Ski Ressort

## Intro

Diese Aufgabe befasst sich mit der Analyse mittels SQL.
Das heißt, weg vom Data Warehouse hin zur Datenanalyse.
Hierbei liegt der Fokus vor allem auf `SELECT` Statements.

## Vorbereitung

> Wir laden die Daten nun neu rein. Dabei sind diesmal keine künstlichen Fehler mehr enthalten.  
> Es kann dennoch vorkommen, dass Werte leer bleiben. Dies muss bei der Analyse berücksichtigt werden.

- Die Datei `ressorts.csv` neu in `land`.`ressorts` laden
- Die Datei `snow.csv` neu in `land`.`snow` laden

## Aufgaben / Fragestellungen

> Anforderung: Jede Fragestellung soll mit der entsprechenden SQL-Query und darunter als Kommentar die Antwort liefern.

### Ressort

- Wie viele Ski Ressorts gibt es?

```sql
SELECT COUNT(land.resorts.Resort)
FROM resorts

-- Antwort: 499
```

- Welches Land hat die meisten Ski Ressorts?

```sql
SELECT COUNT(land.resorts.Country), land.resorts.Country 
FROM resorts
GROUP BY Country 

-- Antwort: Österreich mit 89 Resorts
```

- Welches Ressort hat die günstigsten Preise?

```sql
SELECT land.resorts.Resort, land.resorts.Price
FROM resorts
WHERE price > 0
ORDER BY price ASC
LIMIT 1;

-- Antwort: Gudauri mit 14
```

- Welches Ressort hat die höchsten Preise?

```sql
SELECT land.resorts.Resort, land.resorts.Price 
FROM resorts
ORDER BY price DESC 
LIMIT 1;

-- Antwort: Beaver Creek
```

- Welches Land hat die günstigsten Preise?
  - Durchschnittspreis aller Ressorts
  - Median aller Ressorts

```sql
SELECT land.resorts.Country, AVG(price) as average_price
FROM resorts
WHERE price > 0
GROUP BY Country
ORDER BY price ASC

SELECT DISTINCT country, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price)
OVER (PARTITION by country) AS median
FROM resorts
WHERE price > 0
ORDER BY median ASC

-- Antwort: AVG: Georgia mit 14
            Median: Georgia mit 14
```

- Welches Land hat die höchsten Preise?
  - Durchschnittspreis aller Ressorts
  - Median aller Ressorts

```sql
SELECT land.resorts.Country, AVG(price) as average_price
FROM resorts
GROUP BY Country
ORDER BY price DESC

-- Antwort: AVG: United States mit 81,1667
```

- Welcher Kontinent hat die günstigsten Preise?
  - Durchschnittspreis aller Ressorts
  - Median aller Ressorts

```sql
SELECT land.resorts.Continent, AVG(price) as average_price
FROM resorts
GROUP BY Continent 
ORDER BY price ASC

-- Antwort: AVG: Europa mit 41,54
```

- Welcher Kontinent hat die höchsten Preise?
  - Durchschnittspreis aller Ressorts
  - Median aller Ressorts

```sql
SELECT land.resorts.Continent, AVG(price) as average_price
FROM resorts
GROUP BY Continent 
ORDER BY price DESC

-- Antwort: AVG: Oceania mit 63,3
```

- Welches Ressort ist am besten für Anfänger geeignet?

```sql
SELECT land.resorts.Resort, land.resorts.`Beginner slopes`
FROM resorts
ORDER BY land.resorts.`Beginner slopes` DESC

-- Antwort: Alle Resorts am Skigebiet Les 3 Valle?es (Alle 312 einfache Slopes)
```

- Welches Ressort ist am besten für Profis geeignet?
  
```sql
SELECT land.resorts.Resort, land.resorts.`Difficult slopes` 
FROM resorts
ORDER BY land.resorts.`Difficult slopes` DESC

-- Antwort: Big Sky Resort mit 126 schweren Slopes
```

- Welches Ressort hat die Längste Abfahrt?
  
```sql
SELECT land.resorts.Resort, land.resorts.`Longest run`  
FROM resorts
ORDER BY land.resorts.`Longest run` DESC

-- Antwort: Zermatt - Matterhorn, Les Deux alpes, Alpe d'Huez, Bansko mit jeweils 16
```

- Welches Ressort hat die meisten Lifts?
  
```sql
SELECT land.resorts.Resort, land.resorts.`Total lifts`  
FROM resorts
ORDER BY land.resorts.`Total lifts` DESC

-- Antwort: Les Gets, Avoriaz, Cha?tel mit jeweils 174 Lifts
```

- Welches Ressort hat die wenigsten Lifts?
  
```sql
SELECT land.resorts.Resort, land.resorts.`Total lifts`  
FROM resorts
WHERE `Total lifts` > 0
ORDER BY land.resorts.`Total lifts` ASC

-- Antwort: Fonna Glacier, Wasserngrat (Gstaad), Oppdal, Summit Ski Area at Mt. Hood mit jeweils 1 Lift
```

- Größte Ressort? (Kombination aus Abfahrten `slopes` und Lifts `lifts`)
  
```sql
SELECT land.resorts.Resort, (land.resorts.`Total slopes` + land.resorts.`Total lifts`) AS Summe
FROM resorts
ORDER BY Summe DESC

-- Antwort: Courchevel, Saint Martin de Belleville, La Tania-Val Thorens, Val Thorens, Me?ribel, ?Les Menuires mit jeweils 765
```

### Snow

- Punkt mit dem wenigsten Schnee über den gesamten Zeitraum?
  - Durchschnitt des Schneefalls
  - Median des Schneefalls

```sql
-- Query:
-- Antwort:
```

- Punkt mit dem meisten Schnee über den gesamten Zeitraum?
  - Durchschnitt des Schneefalls
  - Median des Schneefalls

```sql
-- Query:
-- Antwort:
```

### Eigene Fragestellungen

*Überlege dir nun 3 eigene Fragestellungen und beantworte diese selbst:*

- Frage 1

```sql
-- Query:
-- Antwort:
```

- Frage 2

```sql
-- Query:
-- Antwort:
```

- Frage 3

```sql
-- Query:
-- Antwort:
```

### Ressort + Snow

- Ordne zu jedem Ressort einen GPS Punkt einer Wetterstation zu
  - Tabelle `snow` enthält GPS Positionen mit Längen- und Breitengrad
  - Tabelle `ressort` enthält ebenfalls GPS Positionen mit Längen- und Breitengrad
  - Allerdings stimmen die exakten Punkte nicht überein
  - Ordne für jedes Ressort einen GPS Punkt zu
  - Ergebnistabelle: (Ausgabe des `SELECT`-Statements)
    - ID
    - Resort
    - Latitude *(Breitengrad)*
    - Longitude *(Längengrad)*
    - Country
    - Continent
    - Weather_Point *(nächster Punkt(Längengrad,Breitengrad) von Tabelle Snow)*

> Hinweis: Aufgabe bedarf etwas Testing, ich empfehle während der Entwicklung nur mit einem Ressort zu arbeiten und am Ende die Query auf alle Ressorts durchzuführen. Für 100 Ressorts hab meine Instanz knapp über eine Minute benötigt.

Geopunkte werden wie folgt definiert:

```sql
-- create sql point
POINT(longitude,latitude) -- POINT(Längengrad, Breitengrad)
POINT(13.404954,52.520007), -- Berlin
POINT(11.425754,48.766535) -- Ingolstadt
```

Die Distanz zwischen zwei Punkten wird näherungsweise auf einer Sphere (= Kugel) berechnet.
> Hinweis: Die Distanz zwischen zwei GPS-Punkten wird nicht über die euklidische Distanz berechnet.  
> Dabei würde eine Ungenauigkeit entstehen.  
> Eine Sphere berechnet die Distanz ausreichend für unseren Anwendungsfall.
> Siehe hierzu folgendes Bild: [Distanz auf einer Kugel](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fscilogs.spektrum.de%2Fhlf%2Ffiles%2Fsphere-distance.png&f=1&nofb=1&ipt=415a85490bb1ee08fc5413917f9e3d26d86fbe333a5dc03820d07ec2f0642cb3&ipo=images)

```sql
-- distance between points
SELECT
    ST_Distance_Sphere(
        POINT(13.404954,52.520007), -- Berlin
        POINT(11.425754,48.766535) -- Ingolstadt
    ) AS distance_in_meters,
    ST_Distance_Sphere(
        POINT(13.404954,52.520007), -- Berlin
        POINT(11.425754,48.766535) -- Ingolstadt
    )/1000 AS distance_in_kilometers;
    
-- RESULT:
-- distance_in_meters|distance_in_kilometers|
-- ------------------+----------------------+
-- 440036.93072888744|    440.03693072888746|
```

Das Ergebnis für 10 exemplarische Ressorts sieht wie folgt aus:

| ID  | Resort                            | Country     | Continent     | Latitude     | Longitude    | NEAREST_WEATHER_POINT   |
| --- | --------------------------------- | ----------- | ------------- | ------------ | ------------ | ----------------------- |
| 1   | Hemsedal                          | Norway      | Europe        | 60.9282437   | 8.38348693   | POINT (8.375 60.875)    |
| 2   | Geilosiden Geilo                  | Norway      | Europe        | 60.5345261   | 8.2063719    | POINT (8.125 60.625)    |
| 3   | Golm                              | Austria     | Europe        | 47.05781     | 9.8281668    | POINT (9.875 47.125)    |
| 4   | Red Mountain Resort-Rossland      | Canada      | North America | 49.1055201   | -117.8462801 | POINT (-117.875 49.125) |
| 5   | Hafjell                           | Norway      | Europe        | 61.2303686   | 10.52901357  | POINT (10.625 61.125)   |
| 6   | Voss                              | Norway      | Europe        | 60.6837065   | 6.407904807  | POINT (6.375 60.625)    |
| 7   | Porter                            | New Zealand | Oceania       | -39.67098835 | 176.8766681  | POINT (172.625 -40.875) |
| 8   | Nevados de Chilla?n               | Chile       | South America | -36.613844   | -72.0718055  | POINT (-71.375 -36.875) |
| 9   | Hochschwarzeck                    | Germany     | Europe        | 47.6283728   | 12.9205276   | POINT (12.875 47.625)   |
| 10  | Rossfeld - Berchtesgaden - Oberau | Germany     | Europe        | 47.6513062   | 13.0589774   | POINT (13.125 47.625)   |
