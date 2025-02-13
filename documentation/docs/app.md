# Služba Nahrávač Dat

Služba nahrávače dat je zodpovědná za nahrávání dat do databáze PostgreSQL pomocí webové aplikace postavené na Flasku.

## Popis

Tato služba umožňuje uživatelům nahrávat CSV soubory, které jsou poté zpracovány a uloženy do databáze. Dále poskytuje různé endpointy pro prohlížení, stahování a mazání dat.

## Endpoints

### 1. Hlavní stránka

- **URL:** `/`
- **Metoda:** `GET`
- **Popis:** Zobrazuje domovskou stránku aplikace.

### 2. Nahrání souboru

- **URL:** `/upload`
- **Metody:** `GET`, `POST`
- **Popis:** Umožňuje uživatelům nahrát CSV soubor. Při odeslání souboru pomocí metody POST je obsah CSV souboru nahrán do databáze.

### 3. Zobrazení dat

- **URL:** `/data`
- **Metoda:** `GET`
- **Popis:** Zobrazuje data uložená v databázi s možností filtrování a řazení.

### 4. Stažení dat

- **URL:** `/download-data`
- **Metoda:** `GET`
- **Popis:** Umožňuje uživatelům stáhnout data z databáze ve formátu CSV.

### 5. Přidání nového záznamu

- **URL:** `/add`
- **Metody:** `GET`, `POST`
- **Popis:** Poskytuje formulář pro přidání nového záznamu do databáze. ID je generováno náhodně pomocí UUID.

### 6. Smazání dat

- **URL:** `/delete`
- **Metoda:** `GET`
- **Popis:** Zobrazuje formulář pro zadání data pro smazání záznamů.

- **URL:** `/delete_data`
- **Metoda:** `POST`
- **Popis:** Smaže záznamy v databázi na základě zadaného data.

### 7. Zobrazení grafu

- **URL:** `/graph`
- **Metoda:** `GET`
- **Popis:** Přesměruje na Grafana dashboard pro vizualizaci dat.

## Porty

- `5001`: Zpřístupňuje službu nahrávače dat hostitelskému stroji.

## Závislosti

- **db**: Služba nahrávače dat závisí na databázové službě.

## Konfigurace Docker Compose

Níže je konfigurace této služby v souboru `docker-compose.yml`:

```yaml
data_loader:
  build: ./data_loader
  ports:
    - "5001:5000"
  depends_on:
    - db
  networks:
    - mynetwork
