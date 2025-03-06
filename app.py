from flask import Flask, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Google Sheets CSV URL
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQAMN08MkDCY1zHy7Whm7vRpJ5KC8z_0pxJuCcTcWawX-npveykePHMtgWN1UDQ45J-8IM9gFcHiD3E/pub?output=csv"

# Function to fetch data from Google Sheets
def get_data():
    try:
        df = pd.read_csv(GOOGLE_SHEET_CSV_URL)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

# API route to return JSON data
@app.route("/data")
def data():
    return jsonify(get_data())

# Route to render HTML page
@app.route("/")
def home():
    return render_template("index.html")

port = os.environ.get("PORT", 5000)  # Default to 5000 if not set

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(port))  # Ensure it binds to 0.0.0.0
