from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

# Replace these with your Azure SQL details
server = 'inventoryserver01.database.windows.net'
database = 'InventoryDB'
username = 'adminuser'
password = 'Purple@12345!'

# Connection string
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

@app.route('/')
def index():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [dbo].[Inventory]")
        items = cursor.fetchall()
        return render_template("index.html", items=items)
    except Exception as e:
        return f"❌ Error: {e}"

# ✅ Add this to run the app
if __name__ == '__main__':
    app.run(debug=True)
