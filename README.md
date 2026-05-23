# 🔗 Simple URL Shortener

A modern, fast, and professional web application that converts long, cumbersome URLs into short, clean, and shareable links. Built with **Flask** and backed by **MongoDB**, it features a responsive, premium glassmorphic dark-themed interface with vibrant glow effects and interactive user features.

---

## ✨ Features

- **Instant URL Shortening**: Enter any long URL and instantly generate a 5-character alphanumeric short code link.
- **Glassmorphic Dark UI**: Premium design aesthetics featuring animated neon gradient borders, card hover effects, and a modern layout.
- **One-Click Copy**: Built-in clipboard integration to copy generated short links instantly.
- **Robust Database Connectivity**: Automated connection tests with graceful error handling and clear troubleshooting guides for local and remote (MongoDB Atlas) instances.
- **Environment Driven Configuration**: Secure credentials management using `.env` environment variables.
- **Production Ready**: Configured with `gunicorn` and a `Procfile` for rapid deployment to platforms like Heroku, Render, or Railway.

---

## 🛠️ Technology Stack

- **Backend Framework**: [Flask](https://flask.palletsprojects.com/) (Python 3)
- **Database**: [MongoDB](https://www.mongodb.com/) (using PyMongo driver)
- **Environment Management**: `python-dotenv`
- **Security & SSL/TLS**: `certifi` (ensures secure connections to MongoDB Atlas)
- **Styling & Presentation**: HTML5, Vanilla CSS3 (custom dark/neon glow animations)
- **WSGI Server**: [Gunicorn](https://gunicorn.org/) (for production environments)

---

## 📁 Project Structure

```text
Simple URL Shortener/
├── .env                  # Local environment configuration file (ignored by git)
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore file
├── Procfile              # Process file for Heroku/Render hosting
├── app.py                # Core Flask backend server and DB logic
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Custom premium CSS layout and keyframe animations
└── templates/
    └── index.html        # Glassmorphic frontend landing page
```

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 1. Prerequisites

- **Python**: Version 3.8 or higher installed.
- **MongoDB**: Either a local MongoDB instance running on your machine, or a remote cluster on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

### 2. Clone the Repository

```bash
git clone https://github.com/sriaakash06/URL-Shortener.git
cd "Simple URL Shortener"
```

### 3. Create a Virtual Environment & Install Dependencies

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### 4. Configuration

1. Duplicate the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and specify your **MongoDB Connection URI**:
   - For a local MongoDB instance:
     ```env
     MONGODB_URI=mongodb://localhost:27017/url_shortener_db
     ```
   - For MongoDB Atlas:
     ```env
     MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority
     ```

### 5. Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will start, perform a connection ping test with your database, and output debug logs:
```text
DEBUG: Checking Database Connection...
DEBUG: Resolved Mongo URI -> mongodb://localhost:****@localhost:27017/url_shortener_db
MongoDB Connected Successfully!
 * Running on http://127.0.0.1:5000
```
Open your browser and navigate to `http://127.0.0.1:5000` to start shortening URLs!

---

## ☁️ Deployment

This project includes a `Procfile` ready for hosting on platforms like **Heroku**, **Render**, or **Railway**.

### Example: Deploying to Heroku / Render
1. Make sure to define the `MONGODB_URI` in your host's environment settings (Config Vars / Environment Variables).
2. The platform will automatically detect the `Procfile` and launch the application using `gunicorn`:
   ```text
   web: gunicorn app:app
   ```

---

## 🔒 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Sri Aakash**
- 🎓 B.Tech Information Technology Student
- 💡 Passionate about Full Stack Development & AI Projects 🚀

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/sriaakash06)
