# Duplicate Cleaner Web Application

A simple Flask-based web application to upload Excel or CSV files, remove duplicate rows based on **ID**, **Name**, and **Mobile** columns, and download the cleaned file.

---

## Features

- Upload Excel (.xls, .xlsx) or CSV files
- Automatically remove duplicates based on `ID`, `Name`, and `Mobile`
- Download cleaned file
- Clean and user-friendly interface with Bootstrap styling
- Custom background image support

---

## Requirements

- Python 3.7+
- Flask
- pandas
- openpyxl (for Excel support)

---

## Installation

1. Clone the repository or download the source code.

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
