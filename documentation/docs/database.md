# Služba Databáze

Služba databáze používá PostgreSQL pro ukládání všech dat souvisejících s případy COVID.

## Konfigurace

Služba je konfigurována pomocí následujících proměnných prostředí:

- `POSTGRES_DB`: Název databáze (výchozí: `covid_data`)
- `POSTGRES_USER`: Uživatelské jméno pro databázi (výchozí: `user`)
- `POSTGRES_PASSWORD`: Heslo pro databázi (výchozí: `password`)

## Svazky

- `db_data`: Ukládá datové soubory PostgreSQL.
- `pg_hba.conf`: Konfigurace pro autentizaci klienta.
- `postgresql.conf`: Konfigurace serveru PostgreSQL.

## Porty

- `5432`: Zpřístupňuje server PostgreSQL hostitelskému stroji.

## Konfigurace Docker Compose

```yaml
db:
  build: ./db
  volumes:
    - db_data:/var/lib/postgresql/data
    - ./db/pg_hba.conf:/etc/postgresql/pg_hba.conf
    - ./db/postgresql.conf:/etc/postgresql/postgresql.conf
  environment:
    - POSTGRES_DB=covid_data
    - POSTGRES_USER=user
    - POSTGRES_PASSWORD=password
  ports:
    - "5432:5432"
  networks:
    - mynetwork
