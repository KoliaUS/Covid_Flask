# Grafana.md

## Co je Grafana?

Grafana je open-source platforma pro analýzu a vizualizaci dat. Umožňuje uživatelům vytvářet a sdílet dynamické a interaktivní dashboardy. Grafana podporuje širokou škálu zdrojů dat, jako jsou databáze, cloudové služby a další. Hlavní výhodou Grafany je její schopnost agregovat data z různých zdrojů a poskytovat je ve formě přehledných grafů a dashboardů, které lze snadno sdílet a integrovat do různých systémů.

## Použití Grafany ve vašem projektu

Ve vašem projektu bude Grafana sloužit k vizualizaci dat z PostgreSQL databáze. Data se zobrazí až po nahrání CSV souboru do databáze.

## Jak to funguje?

1. **Databáze (db)**: PostgreSQL databáze slouží k uložení dat. Konfigurace databáze je definována v `pg_hba.conf` a `postgresql.conf` souborech.
   
2. **Data Loader (data_loader)**: Tato služba zajišťuje nahrání dat z CSV souboru do databáze. Závisí na tom, že databáze je dostupná.

3. **Dokumentace (documentation)**: Tato služba slouží k zobrazení dokumentace a běží na portu 8000.

4. **Grafana**: Tato služba poskytuje webové rozhraní pro vizualizaci dat uložených v PostgreSQL databázi. Je přístupná na portu 3000 a po prvním přihlášení je heslo admin.

## Jak začít?

1. Ujistěte se, že máte nainstalovaný Docker a Docker Compose.
2. V kořenovém adresáři vašeho projektu spusťte příkaz `docker-compose up`.
3. Po spuštění všech služeb můžete přistupovat k jednotlivým komponentám:
   - Grafana: [http://localhost:3000](http://localhost:3000)
   - Dokumentace: [http://localhost:8000](http://localhost:8000)
   - Data Loader: bude dostupný na [http://localhost:5001](http://localhost:5001)

4. Nahrajte CSV soubor pomocí Data Loader služby, což zajistí nahrání dat do PostgreSQL databáze.
5. V Grafaně jsou následně zobrazeny grafy v dashboardu.

Tento postup zajistí, že data budou v Grafaně dostupná až po úspěšném nahrání CSV souboru do databáze.
