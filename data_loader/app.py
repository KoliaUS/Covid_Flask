from flask import Flask, flash, make_response, redirect, render_template, request, url_for
import psycopg2
import pandas as pd
from io import StringIO
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def connect_to_db():
    return psycopg2.connect(
        dbname="covid_data",
        user="user",
        password="password",
        host="db",
        port="5432"
    )

def initialize_db():
    conn = connect_to_db()
    cursor = conn.cursor()
    # Smaže tabulku, pokud existuje
    cursor.execute('DROP TABLE IF EXISTS cases;')
    # Vytvoří tabulku znovu
    cursor.execute('''
    CREATE TABLE cases (
        id UUID PRIMARY KEY,
        tyden_od DATE,
        tyden_do DATE,
        tyden VARCHAR,
        nove_pripady_celkem INT,
        primoinfekce INT,
        prvni_reinfekce INT,
        druhe_reinfekce INT,
        treti_a_dalsi_reinfekce INT
    );
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            df = pd.read_csv(file)
            conn = connect_to_db()
            cursor = conn.cursor()
            buffer = StringIO()
            df.to_csv(buffer, index=False, header=False)
            buffer.seek(0)
            cursor.copy_from(buffer, 'cases', sep=',', columns=list(df.columns))
            conn.commit()
            conn.close()
            return render_template('home.html')
    else:
        return render_template('upload.html')
    
def order_choice(direction):
    return 'DESC' if direction == 'desc' else 'ASC'


@app.route('/data')
def show_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Base query to select all data, with additional columns for average and reinfection ratio calculations
    query = """
    SELECT *,
           (prvni_reinfekce + druhe_reinfekce + treti_a_dalsi_reinfekce)::float / NULLIF(nove_pripady_celkem, 0) AS reinfection_ratio
    FROM cases
    """

    # Applying filters
    filters = []
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    min_cases = request.args.get('min_cases')
    if from_date:
        filters.append(f"tyden_od >= '{from_date}'")
    if to_date:
        filters.append(f"tyden_do <= '{to_date}'")
    if min_cases:
        filters.append(f"nove_pripady_celkem >= {min_cases}")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    # Order by logic remains the same
    order_by = request.args.get('order_by', 'id')
    order_direction = request.args.get('order_direction', 'asc')
    query += f" ORDER BY {order_by} {order_choice(order_direction)}"

    df = pd.read_sql(query, conn)
    average_cases = df['nove_pripady_celkem'].mean()
    average_reinfection_ratio = df['reinfection_ratio'].mean()

    data_html = df.to_html(index=False, columns=['id', 'tyden_od', 'tyden_do', 'tyden', 'nove_pripady_celkem', 'primoinfekce', 'prvni_reinfekce', 'druhe_reinfekce', 'treti_a_dalsi_reinfekce'])

    conn.close()
    return render_template('data.html', data=data_html, average_cases=average_cases, average_reinfection_ratio=average_reinfection_ratio)



@app.route('/download-data')
def download_data():
    conn = connect_to_db()
    query = "SELECT * FROM cases"
    filters = []

    # Přidání validace sloupců
    valid_columns = ['id', 'tyden_od', 'tyden_do', 'tyden', 'nove_pripady_celkem', 'primoinfekce', 'prvni_reinfekce', 'druhe_reinfekce', 'treti_a_dalsi_reinfekce']
    order_by = request.args.get('order_by', 'id')
    order_direction = request.args.get('order_direction', 'asc') if request.args.get('order_direction', 'asc') == 'asc' else 'desc'

    if order_by not in valid_columns:
        order_by = 'id'  # Fallback to a default column if invalid column is provided

    # Získání filtrů z URL parametrů
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    min_cases = request.args.get('min_cases')
    infaction = request.args.get('infaction')
    first_reinfection = request.args.get('first_reinfection')
    second_reinfection = request.args.get('second_reinfection')

    # Přidání filtrů do dotazu, pokud existují
    if from_date:
        filters.append(f"tyden_od >= '{from_date}'")
    if to_date:
        filters.append(f"tyden_do <= '{to_date}'")
    if min_cases:
        filters.append(f"nove_pripady_celkem >= {min_cases}")
    if infaction:
        filters.append(f"primoinfekce >= {infaction}")
    if first_reinfection:
        filters.append(f"prvni_reinfekce >= {first_reinfection}")
    if second_reinfection:
        filters.append(f"druhe_reinfekce >= {second_reinfection}")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += f" ORDER BY {order_by} {order_choice(order_direction)}"

    df = pd.read_sql(query, conn)
    csv_data = df.to_csv(index=False)

    # Nastavení HTTP response headers pro odeslání souboru
    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-Type'] = 'text/csv'
    return response


@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        try:
            id = str(uuid.uuid4())
            tyden_od = request.form['tyden_od']
            tyden_do = request.form['tyden_do']
            tyden = request.form['tyden']
            nove_pripady_celkem = int(request.form['nove_pripady_celkem'])
            primoinfekce = int(request.form['primoinfekce'])
            prvni_reinfekce = int(request.form['prvni_reinfekce'])
            druhe_reinfekce = int(request.form['druhe_reinfekce'])
            treti_a_dalsi_reinfekce = int(request.form['treti_a_dalsi_reinfekce'])

            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO cases (id, tyden_od, tyden_do, tyden, nove_pripady_celkem, primoinfekce, prvni_reinfekce, druhe_reinfekce, treti_a_dalsi_reinfekce)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''', (id, tyden_od, tyden_do, tyden, nove_pripady_celkem, primoinfekce, prvni_reinfekce, druhe_reinfekce, treti_a_dalsi_reinfekce))
            conn.commit()
            cursor.close()
            flash("Data byla úspěšně přidána.", "success")
        except Exception as e:
            flash(f"Chyba při přidávání dat: {e}", "error")
        return redirect(url_for('add_data'))
    return render_template('add.html')



@app.route('/delete', methods=['GET', 'POST'])
def delete_data():
    if request.method == 'POST':
        tyden_od = request.form.get('tyden_od')
        id = request.form.get('id')
        tyden = request.form.get('tyden')
        conditions = []

        if tyden_od:
            conditions.append(f"tyden_od = '{tyden_od}'")
        if id:
            conditions.append(f"id = '{id}'")
        if tyden:
            conditions.append(f"tyden = '{tyden}'")

        if not conditions:
            flash("Zadejte alespoň jedno kritérium pro odstranění.", "error")
            return redirect(url_for('delete_data'))

        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            delete_query = f"DELETE FROM cases WHERE {' AND '.join(conditions)}"
            cursor.execute(delete_query)
            conn.commit()
            deleted_rows = cursor.rowcount
            cursor.close()
            conn.close()
            if deleted_rows:
                flash(f"Bylo úspěšně odstraněno {deleted_rows} záznamů.", "success")
            else:
                flash("Žádné záznamy neodpovídají zadaným kritériím.", "info")
        except Exception as e:
            flash(f"Chyba při odstraňování dat: {e}", "error")
        return redirect(url_for('delete_data'))

    return render_template('delete.html')


@app.route('/graph')
def show_graph():
    grafana_url = "http://localhost:3000/d/cdmgptyvtkem8b/grafy?orgId=1"
    return redirect(grafana_url)


if __name__ == '__main__':
    initialize_db()  # Tato funkce se zavolá při startu aplikace
    app.run(debug=True, host='0.0.0.0', port=5000)
