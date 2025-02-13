# Vítejte v dokumentaci projektu

Tato dokumentace vás provede nastavením a testováním projektu.

## Předpoklady

Než začnete, ujistěte se, že máte nainstalováno následující:

- Docker
- Docker Compose
- Python 3.8 nebo vyšší

## Pokyny k nastavení

1. **Sestavení a spuštění Docker kontejnerů:**

    Použijte Docker Compose k sestavení a spuštění potřebných kontejnerů:

    ```sh
    docker-compose up --build
    ```

2. **Přístup k dokumentaci:**

    Jakmile jsou kontejnery spuštěny, můžete k dokumentaci přistoupit na [http://localhost:8000](http://localhost:8000).

## Přehled služeb

Projekt se skládá z následujících služeb:

- [Databáze](database.md)
- [Nahrávač dat](data_loader.md)
- [Dokumentace](documentation.md)
- [Grafana](grafana.md)

## Testování projektu

1. **Nahrání dat:**

    Data můžete nahrát do databáze tak, že přejdete na stránku nahrávání v aplikaci a nahrajete CSV soubor.

2. **Zobrazení dat:**

    Přejděte na stránku s daty, abyste zobrazili nahraná data. Data je možné filtrovat.

3. **Generování CSV:**

    Použijte poskytované endpointy k vygenerování a stažení reportů.

4. **Grafické znázornění:**

    Použijte Grafanu k vizualizaci dat. Přístup ke Grafaně je na [http://localhost:3000](http://localhost:3000) s přihlašovacími údaji (uživatel: `admin`, heslo: `admin`).

## Závěr

Postupujte podle těchto kroků pro rychlé nastavení a testování projektu. Pokud narazíte na nějaké problémy, podívejte se do souboru `about.md` pro podrobné kroky řešení problémů.
