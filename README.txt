# 🛡 SOC Analyst Dashboard

A Security Operations Center (SOC)-inspired network scanning dashboard built with Python and Streamlit.  
It performs port scanning, identifies high-risk services, tracks scan history, and provides real-time analytics through an interactive web interface.

---

## 📌 Overview

This project simulates a basic SOC environment where a user (analyst) can:

- Log into a secure dashboard  
- Scan a target IP address or domain for open ports  
- Identify risky or exposed services  
- View results in real-time  
- Analyze scan data visually  
- Track previous scans  

It demonstrates core cybersecurity concepts such as network scanning, threat identification, and monitoring workflows.

---

## 🚀 Features

- 🔐 **Login Authentication System**  
  Simple analyst login to access the dashboard

- 🔍 **Port Scanning Engine**  
  Multi-threaded scanning of common network ports

- 🚨 **Risk Detection**  
  Flags high-risk services like SSH, Telnet, SMB, RDP

- 📊 **Interactive Dashboard (Streamlit)**  
  Clean UI for scanning and results visualization

- 📈 **Analytics Charts**  
  Visual breakdown of risk levels

- 📜 **Scan History Tracking**  
  Stores previous scans for reference

- 📁 **Report Generation**  
  Saves scan results in structured JSON format

---

## 🧰 Technologies Used

- Python  
- Streamlit  
- Socket Programming  
- Threading (concurrent.futures)  
- JSON  

---

## 🖥 How It Works

1. User logs into the dashboard  
2. Inputs a target IP or domain  
3. The system scans common ports  
4. Open ports are detected  
5. Risk level is assigned (HIGH / LOW)  
6. Results are displayed in dashboard  
7. Scan is saved in history and reports  

---

## 🔐 Demo Login Credentials

Username: admin  
Password: soc123  

⚠️ This is my demo authentication system.

---

## 📸 Screenshots

### 🔐 Login Page
![Login](screenshots/login.png)

### 🛡 Dashboard View
![Dashboard](screenshots/dashboard.png)

### 🔍 Scan Results
![Results](screenshots/scan-results.png)

### 📊 Analytics
![Analytics](screenshots/analytics.png)

---

## ▶️ How to Run Locally

### 1. Clone the repository

git clonehttps://github.com/Chiwendu-sec/soc-analyst-dashboard.git
cd Soc-analyst-dashboard

### 2. Install dependencies

pip install -r requirements.txt
or
py -3.14 -m pip install -r requirements.txt

### 3. Run the application

streamlit run dashboard.py
or
py -3 -m pip install streamlit

### 🌐 Live Demo

## visit

https://soc-analyst-dashboard.streamlit.app/

### 📊 Example Use Case

This project can be used to:

Simulate SOC monitoring workflows
Detect exposed services on networks
Practice basic threat identification
Demonstrate cybersecurity portfolio skills
Learn network scanning fundamentals


### 🔥 Future Improvements


Email alert system for high-risk ports
Role-based authentication (Admin / Analyst)
Database integration (SQLite/PostgreSQL)
Advanced vulnerability detection
Real-time threat intelligence API integration

### ⚠️ Disclaimer

This tool is for educational purposes only.
Do not use it on systems without proper authorization.

### 👤 Author

Bright Chiwendu Goodluck
Cybersecurity Enthusiast | SOC Analyst Path


