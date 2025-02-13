# COVID-19 Data Management Application

Tento projekt je webová aplikace postavená na frameworku Flask, která slouží ke správě a analýze dat o COVID-19. Aplikace umožňuje nahrávání dat, zobrazování, filtrování, stahování, přidávání a mazání záznamů v databázi.

## Funkce

- **Inicializace databáze**: Vytvoření tabulky `cases` pro ukládání dat o COVID-19.
- **Nahrání souboru**: Umožňuje nahrání CSV souboru s daty do databáze.
- **Zobrazení dat**: Zobrazuje data z databáze v tabulkové formě s možností filtrování a řazení.
- **Stažení dat**: Umožňuje stažení dat ve formátu CSV.
- **Přidání dat**: Umožňuje ruční přidání nového záznamu do databáze přes webový formulář.
- **Smazání dat**: Umožňuje smazání záznamů z databáze na základě zadaných kritérií.
- **Zobrazení grafu**: Přesměruje uživatele na externí Grafana dashboard pro vizualizaci dat.

## Použité technologie

- **Flask**: Webový framework pro Python.
- **PostgreSQL**: Databázový systém pro ukládání dat.
- **Pandas**: Knihovna pro manipulaci a analýzu dat.
- **Grafana**: Nástroj pro vizualizaci dat.

## Instalace a spuštění

1. **Klonování repozitáře**:
   ```bash
   git clone https://github.com/vaserepozitar/covid-data-app.git
   cd covid-data-app
   ```

2. **Instalace závislostí**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurace databáze**:
   Upravte soubor `app.py` a nastavte správné údaje pro připojení k databázi (`dbname`, `user`, `password`, `host`, `port`).

4. **Spuštění aplikace**:
   ```bash
   python app.py
   ```

5. **Přístup k aplikaci**:
   Otevřete prohlížeč a přejděte na adresu [http://localhost:5000](http://localhost:5000).

## Použití

- **Domovská stránka**: Základní informace a možnosti pro práci s daty.
- **Nahrání souboru**: Nahrání CSV souboru s daty.
- **Zobrazení dat**: Prohlížení a filtrování dat.
- **Stažení dat**: Stažení dat ve formátu CSV.
- **Přidání dat**: Ruční přidání nového záznamu.
- **Smazání dat**: Smazání záznamů na základě kritérií.
- **Zobrazení grafu**: Přesměrování na Grafana dashboard.

## Příklady použití

- **Nahrání dat**:
  - Přejděte na `/upload` a nahrajte CSV soubor s daty.

- **Zobrazení dat**:
  - Přejděte na `/data` a použijte filtry pro zobrazení požadovaných dat.

- **Stažení dat**:
  - Přejděte na `/download-data` a stáhněte si data ve formátu CSV.

- **Přidání dat**:
  - Přejděte na `/add` a vyplňte formulář pro přidání nového záznamu.

- **Smazání dat**:
  - Přejděte na `/delete` a zadejte kritéria pro smazání záznamů.
