# Database-Activity-Monitoring-Intrusion-Detection


## Overview
This project aims to design a monitoring system to log and analyze SQL queries. It detects suspicious operations, such as `DROP` or `DELETE` statements without backup, and can identify potential SQL injection attempts. A machine learning classifier is included to differentiate between normal and malicious query patterns.

This system serves as a **proof-of-concept** for database activity monitoring and can be extended for cybersecurity applications in real-world database systems.

---

## Features
- Logs all executed SQL queries.
- Detects dangerous operations like `DROP`, `DELETE`, `TRUNCATE`.
- ML-based classifier to identify suspicious queries.
- Can be extended to monitor real database systems in real-time.
- Provides alerts for potentially malicious activities.

---



### Prerequisites
- Python 3.x
- Libraries: `pandas`, `scikit-learn`, `sqlparse`

Install required packages:
```bash
pip install -r requirements.txt

