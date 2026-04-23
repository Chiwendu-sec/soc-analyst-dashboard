
🛡 SOC Analyst Dashboard

A Security Operations Center (SOC)-inspired network scanning dashboard built with Python and Streamlit.
It performs port scanning, identifies high-risk services, tracks scan history, and provides real-time analytics through an interactive web interface.

👤 AUTHOR

Bright Chiwendu Goodluck
🛡 Cybersecurity Enthusiast | SOC Analyst Path

📌 OVERVIEW

This project simulates a basic SOC environment where a user (analyst) can:

🔐 Log into a secure dashboard
🔍 Scan a target IP address or domain for open ports
🚨 Identify risky or exposed services
📊 View results in real-time
📈 Analyze scan data visually
📜 Track previous scans

It demonstrates core cybersecurity concepts such as network scanning, threat identification, and monitoring workflows.



🚀 FEATURES

🔐 Login Authentication System
Simple analyst login to access the dashboard

🔍 Port Scanning Engine
Multi-threaded scanning of common network ports

🚨 Risk Detection
Flags high-risk services like SSH, Telnet, SMB, RDP

📊 Interactive Dashboard (Streamlit)
Clean UI for scanning and results visualization

📈 Analytics Charts
Visual breakdown of risk levels

📜 Scan History Tracking
Stores previous scans for reference

📁 Report Generation
Saves scan results in structured JSON format



🧰 TECHNOLOGIES USED

🐍 Python
⚡ Streamlit
🔌 Socket Programming
🧵 Threading (concurrent.futures)
📄 JSON



🖥 HOW IT WORKS

1️⃣ User logs into the dashboard
2️⃣ Inputs a target IP or domain
3️⃣ System scans common ports
4️⃣ Open ports are detected
5️⃣ Risk level is assigned (HIGH / LOW)
6️⃣ Results are displayed in dashboard
7️⃣ Scan is saved in history and reports



🔐 DEMO LOGIN CREDENTIALS

👤 Username: admin
🔑 Password: soc123

⚠ This is a demo authentication system.



📸 SCREENSHOTS

🔐 Login Page
screenshots/login.png

🛡 Dashboard View
screenshots/dashboard.png

🔍 Scan Results
screenshots/scan-results.png

📊 Analytics
screenshots/analytics.png



▶️ HOW TO RUN LOCALLY

1️⃣ Clone the repository
git clone [https://github.com/Chiwendu-sec/soc-analyst-dashboard.git](https://github.com/Chiwendu-sec/soc-analyst-dashboard.git)
cd Soc-analyst-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt
or
py -3.14 -m pip install -r requirements.txt

3️⃣ Run the application
streamlit run dashboard.py
or
py -3 -m streamlit run dashboard.py



🌐 LIVE DEMO

👉 https://soc-analyst-dashboard.streamlit.app


📊 USE CASES

This project can be used to:

🛡 Simulate SOC monitoring workflows
🔍 Detect exposed services on networks
🧠 Practice basic threat identification
💼 Demonstrate cybersecurity portfolio skills
📡 Learn network scanning fundamentals



🔥 FUTURE IMPROVEMENTS

📧 Email alert system for high-risk ports
👥 Role-based authentication (Admin / Analyst)
🗄 Database integration (SQLite/PostgreSQL)
🧪 Advanced vulnerability detection
📡 Real-time threat intelligence API integration



⚠ DISCLAIMER

This tool is for educational purposes only.
Do not use it on systems without proper authorization.


