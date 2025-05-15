from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
CLEANED_FOLDER = 'cleaned'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CLEANED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    if filename.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)

    # Remove duplicates based on ID, Name, and Mobile Number
    df_cleaned = df.drop_duplicates(subset=['ID', 'Name', 'Mobile'], keep='first')

    cleaned_path = os.path.join(CLEANED_FOLDER, f'cleaned_{filename}')
    if filename.endswith('.csv'):
        df_cleaned.to_csv(cleaned_path, index=False)
    else:
        df_cleaned.to_excel(cleaned_path, index=False)

    return send_file(cleaned_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
