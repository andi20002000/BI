# Übung 1 - Data Definition Language

## Datenbanken

- Erzeuge eine Datenbank Namens `mydatabase`.

```sql
CREATE SCHEMA mydatabase;
```

- Lösche die Datenbank Namens `mydatabase`.

```sql
DROP SCHEMA mydatabase;
```

- Zeige alle Datenbanken an.

```sql
SHOW DATABASES;
```

- Erzeuge eine Datenbank Namens `thi`

```sql
CREATE SCHEMA thi;
```

- Benutze (`use`) die Datenbank `thi`

```sql
USE thi
```

## Tabellen

- Erzeuge eine Tabelle Namens `students`. Füge folgende Spalten hinzu:
  - `id` -> `Integer`
  - `forename` -> `String` (10 Zeichen)
  - `surname` -> `String` (10 Zeichen)
  - `title` -> `String` (10 Zeichen)

```sql
CREATE TABLE students
id INT
forename VARCHAR(10)
surname VARCHAR(10)
title VARCHAR(10);
```

- Lösche die Tabelle `students`

```sql
DROP TABLE students;
```

- Erzeuge eine Tabelle `students` erneut (gleiche Spalten)

```sql
CREATE TABLE students
id PRIMARY KEY INT
forename VARCHAR(10)
surname VARCHAR(10)
title VARCHAR(10);
```

- Lösche die Spalte `title` der Tabelle `students`

```sql
ALTER TABLE students
DROP COLUMN title;
```

- Füge die Spalte `age` als `Integer` hinzu. Hinweis: Lösche nicht die Tabelle, sondern ändere sie.

```sql
ALTER TABLE students
ADD COLUMN INT age;
```

- Ändere die maximal mögliche Zeichenanzahl für `forename` auf 20 Zeichen (zuvor waren es 10) (Nutze `MODIFY COLUMN`)

```sql
ALTER TABLE students
MODIFIY COLUMN forename VARCHAR(20);
```

- Benenne die Spalte `age` um auf `birth_year` und ändere den Datentyp auf `date`(Nutze `CHANGE COLUMN`)

```sql
ALTER TABLE students
RENAME COLUMN age TO birth_year
CHANGE COLUMN birth_year date;
```

- Schema überprüfen / Schema der Tabelle `students` anzeigen lassen (`DESCRIBE`)

```sql
DESCRIBE SCHEMA students;
```

- Lösche Spalte `title` von `students`.

```sql
ALTER TABLE students
DROP column title;
```

### Constraints

siehe [MySQL Constraints](https://www.w3schools.com/mysql/mysql_constraints.asp)

- Erzeuge eine Tabelle Namens `teachers` mit folgenden Spalten, Spalte `id` darf nie leer sein
  - `id` -> `Integer` (not null)
  - `forename` -> `String` (15 Zeichen)
  - `surname` -> `String` (15 Zeichen)

```sql
CREATE TABLE teachers
id INT NOT NULL
forename VARCHAR(15)
surname VARCHAR(15)
```

- Erzeuge eine Tabelle Namens `course` mit folgenden Spalten, die Spalte `name` muss eindeutig sein (darf nicht mehrfach vergeben werden)
  - `id` -> `Integer` (not null)
  - `name` -> `String` (15 Zeichen, unique)

```sql
CREATE TABLE course
id INT NOT NULL
`name` VARCHAR(15);
```

- ändere für die Tabellen `students`, `teachers` und `courses` die Spalte `id` auf einen Primärschlüssel (`ADD CONSTRAINT`)

```sql
ALTER TABLE students
ADD PRIMARY KEY (id);
ALTER TABLE teachers
ADD PRIMARY KEY (id);
ALTER TABLE courses
ADD PRIMARY KEY (id);
```