from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scraper.summarizer import summarize_text
from scraper.scraper import scrape_url
from scraper.utils import validate_url
import os

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route("/")
def index():
    # Serve the HTML frontend
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_url():
    try:
        data = request.json
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # Validate URL
        if not validate_url(url):
            return jsonify({"error": "Invalid URL"}), 400

        # Scrape content from the URL
        content = scrape_url(url)
        if not content:
            return jsonify({"error": "Failed to scrape content from the URL"}), 500

        # Summarize the scraped content
        summary = summarize_text(content)
        return jsonify({"summary": summary}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
