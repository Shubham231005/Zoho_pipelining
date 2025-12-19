# Real-Time User Analytics Pipeline (Flask + SQLite)

## 📌 Project Overview
This project demonstrates an **end-to-end user analytics pipeline** that captures real-time website interactions, stores them in a database, processes the data, and prepares it for business intelligence (BI) analysis.

The focus of this project is on **backend analytics engineering**, including data collection, preprocessing, and pipeline design.

---

## 🏗️ Architecture


---

## ✨ Features Implemented

### ✅ Web Tracking
- Tracks page visits automatically
- Captures:
  - Page name
  - Device type
  - Browser type
  - Timestamp
  - Time spent on page

### ✅ Backend API
- Built using **Flask**
- Custom endpoints for:
  - Visitor tracking
  - Event tracking

### ✅ Database Layer
- Uses **SQLite** for simplicity
- Structured schema for:
  - Visitors
  - User events
- Automatic table creation on app startup

### ✅ Data Cleaning & Normalization
- Timestamp normalization
- Data validation before export
- Ready for BI ingestion

### ✅ ETL Pipeline (Python)
- Reads data from SQLite
- Converts data into BI-compatible formats (JSON / CSV)
- Designed for scheduled or automated runs

---

## 🧪 Technologies Used

- **Python**
- **Flask**
- **SQLite**
- **Requests**
- **OAuth 2.0 (Explored for BI integration)**
- **HTML / CSS (Basic frontend)**

---

## 📁 Project Structure


---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Zoho_pipelining.git
cd Zoho_pipelining
pip install flask requests user-agents
3️⃣ Run the Flask App
python app.py


Open in browser:

http://127.0.0.1:5000

