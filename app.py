from flask import Flask, request, jsonify, redirect, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
import string
import certifi

load_dotenv()

app = Flask(__name__)

# MongoDB Connection

mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())

# Database
db = client["url_shortener_db"]
collection = db["urls"]

# Generate Short Code

def generate_short_code(length=5):

    characters = string.ascii_letters + string.digits

    return ''.join(random.choice(characters) for _ in range(length))

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Create Short URL
@app.route('/shorten', methods=['POST'])
def shorten_url():

    original_url = request.form['url']

    short_code = generate_short_code()

    collection.insert_one({
        "original_url": original_url,
        "short_code": short_code
    })

    short_url = request.host_url + short_code

    return render_template(
        'index.html',
        short_url=short_url
    )

# Redirect Route
@app.route('/<short_code>')
def redirect_url(short_code):

    data = collection.find_one({
        "short_code": short_code
    })

    if data:
        return redirect(data['original_url'])

    return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)