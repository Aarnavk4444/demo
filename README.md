# DataBite ⚡
> Live Expiry Telemetry & NPR Financial Analytics Suite

DataBite is a specialized web application built with **Django** designed to help businesses and individuals manage inventory assets, track expiration timelines in real-time, audit financial leakage, and optimize capital allocation in Nepalese Rupees (NPR).

---

## 🌟 Key Features

* **Live Expiry Telemetry:** Real-time monitoring of item viability status (Safe, Expiring Soon, Expired) powered by dynamic health calculations.
* **NPR Financial Suite:** Advanced analytics covering gross portfolio valuation, waste leakage auditing, and depreciation forecasting simulators.
* **Interactive Dashboard:** Instant client-side search filtering, visual metrics, and interactive charts built with Chart.js.
* **Hazard Alerts:** Automated alert stacks highlighting expired stock and offering quick-action asset removal.
* **Asset Detail Insights:** Deep-dive pages for every registered inventory item.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3 (Glassmorphism design system), JavaScript, Chart.js
* **Database:** SQLite (Development) / Relational DB (Production ready)

---

## 🚀 Getting Started Locally

🚀 Step-by-Step Guide: Running on Another PC (Local Server)
If you or another developer want to clone this repository and spin up a local development server on a brand new computer, follow these exact steps:

Prerequisites
Make sure the new computer has the following installed:

Python (version 3.8 or higher recommended) - Download Python

Git - Download Git

Step 1: Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Terminal on macOS/Linux) and clone the project repository from GitHub:

Bash
git clone [https://github.com/your-username/databite.git](https://github.com/your-username/databite.git)
cd databite
Step 2: Create a Virtual Environment
It is best practice to run Python apps inside an isolated virtual environment:

Bash
python -m venv venv
Activate the virtual environment:

On Windows (Command Prompt / PowerShell):

Bash
venv\Scripts\activate
On macOS / Linux:

Bash
source venv/bin/activate
Step 3: Install Required Dependencies
Install all required Python packages (such as Django, Gunicorn, etc.) listed in the requirements.txt file:

Bash
pip install -r requirements.txt
Step 4: Run Database Migrations
Set up the local SQLite database schema by running the migration commands:

Bash
python manage.py makemigrations
python manage.py migrate
Step 5: Start the Local Development Server
Launch the local server using Django's built-in development command:

Bash
python manage.py runserver
Step 6: Access the Local Website
Open your web browser (Chrome, Firefox, Edge, etc.).

Copy and paste the local link shown in your terminal:

Plaintext
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
