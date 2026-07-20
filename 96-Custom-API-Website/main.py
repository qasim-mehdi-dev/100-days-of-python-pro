import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.coingecko.com/api/v3/search"

def fetch_api_data(query_params):
    params = {
        "x_cg_demo_api_key": API_KEY,  
        **query_params
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"API request failed: {error}")
        return None

def process_raw_response(raw_json):
    if raw_json is None:
        return {"error": "No data received from API"}
    
    cleaned_data = []
    raw_items = raw_json.get("coins", [])

    for item in raw_items:
        cleaned_item = {
            "id": item.get("id"),
            "name": item.get("name"),
            "symbol": item.get("symbol"),
            "market_cap_rank": item.get("market_cap_rank"),
            "thumb": item.get("thumb")
        }
        cleaned_data.append(cleaned_item)

    return cleaned_data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form.get("search", "").strip()
    else:
        search_term = request.args.get("search", "").strip()

    query_params = {
        "query": search_term
    }

    raw_json = fetch_api_data(query_params)
    cleaned_data = process_raw_response(raw_json)

    return jsonify(cleaned_data)

if __name__ == "__main__":
    app.run(debug=True)