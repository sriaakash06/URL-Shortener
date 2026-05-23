from flask import Flask, request, jsonify, redirect, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
import string
import certifi

from pathlib import Path
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

# Load environment variables from .env file relative to this script
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

# MongoDB Connection
mongodb_uri = os.getenv("MONGODB_URI")

if not mongodb_uri or mongodb_uri == "your_mongodb_connection_string":
    print("WARNING: MONGODB_URI is not set or is set to a placeholder in your .env file.")
    print("Defaulting to local MongoDB (mongodb://localhost:27017/).")
    mongodb_uri = "mongodb://localhost:27017/"

try:
    client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
    db = client["url_shortener_db"]
    collection = db["urls"]
    
    # Verify connection on startup with a short timeout
    print(f"Connecting to MongoDB...")
    client.admin.command('ping', serverSelectionTimeoutMS=3000)
    print("MongoDB connection verified successfully!")
except Exception as e:
    print("\n" + "="*80)
    print("DATABASE CONNECTION ERROR:")
    print(f"Could not connect to MongoDB at: {mongodb_uri}")
    print("-"*80)
    if "localhost" in mongodb_uri or "127.0.0.1" in mongodb_uri:
        print("It looks like you are trying to connect to a local MongoDB instance, but it is not running.")
        print("Please make sure your MongoDB service is started:")
        print("  - On Windows: Run 'net start MongoDB' in an Administrator Command Prompt or start it via Services.")
        print("  - On Linux/WSL: Run 'sudo systemctl start mongod' or 'sudo service mongodb start'.")
    else:
        print("It looks like you are trying to connect to a remote MongoDB instance (e.g. MongoDB Atlas).")
        print("Please verify that:")
        print("  1. The MONGODB_URI in your .env file is correct (currently it uses a placeholder/fake domain).")
        print("  2. Your IP address is whitelisted in your MongoDB Atlas Network Access settings.")
        print("  3. Your database username and password are correct.")
    print("="*80 + "\n")
    raise e

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