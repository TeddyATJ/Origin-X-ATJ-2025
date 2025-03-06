import pandas as pd
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# 🔹 Replace with your actual Google Sheets CSV Export URL
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1ntwalsDfhc8xMfkcP3Sqx3FHZXL8pNSolYlqR5D5t2M/gviz/tq?tqx=out:csv"

@app.route('/data')
def get_data():
    try:
        # 🔹 Fetch data from Google Sheets CSV
        df = pd.read_csv(GOOGLE_SHEET_URL)

        # 🔹 Ensure no trailing spaces in column names
        df.columns = df.columns.str.strip()

        # 🔹 Drop any extra "Unnamed" columns
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        # 🔹 Replace NaN values with empty strings
        df = df.fillna("")

        # 🔹 Convert DataFrame to JSON
        data = df.to_dict(orient='records')

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
