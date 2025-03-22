from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize Database
def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vendors (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            firm_name TEXT, father_name TEXT, dob TEXT,
                            gender TEXT, nationality TEXT, mobile TEXT,
                            email TEXT, legal_status TEXT, gstin TEXT,
                            pan_number TEXT, pf_number TEXT, pan_image TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE, password TEXT)''')
        conn.commit()

init_db()

# Home Route
@app.route('/')
def home():
    return render_template("home.html")

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            if user:
                session['user'] = username
                return redirect(url_for('data_management'))
            else:
                return "Invalid Credentials"
    return render_template("login.html")

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Vendor Registration
@app.route('/vendor_registration', methods=['GET', 'POST'])
def vendor_registration():
    if request.method == 'POST':
        firm_name = request.form['firm_name']
        father_name = request.form['father_name']
        dob = request.form['dob']
        gender = request.form['gender']
        nationality = request.form['nationality']
        mobile = request.form['mobile']
        email = request.form['email']
        legal_status = request.form['legal_status']
        gstin = request.form['gstin']
        pan_number = request.form['pan_number']
        pf_number = request.form['pf_number']
        
        # Handle PAN Image Upload
        pan_image = request.files['pan_image']
        pan_image_path = os.path.join(UPLOAD_FOLDER, pan_image.filename)
        pan_image.save(pan_image_path)

        # Save Data to Database
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vendors (firm_name, father_name, dob, gender, nationality, mobile, email, legal_status, gstin, pan_number, pf_number, pan_image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                           (firm_name, father_name, dob, gender, nationality, mobile, email, legal_status, gstin, pan_number, pf_number, pan_image_path))
            conn.commit()
        return redirect(url_for('data_management'))
    return render_template('vendor_registration.html')

# Data Management System
@app.route('/data_management')
def data_management():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, firm_name, pan_number FROM vendors")
        vendors = cursor.fetchall()
    return render_template("data_management.html", vendors=vendors)

# PAN Verification Page
@app.route('/pan_verification')
def pan_verification():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, firm_name, pan_number, pan_image FROM vendors")
        vendors = cursor.fetchall()
    return render_template("pan_verification.html", vendors=vendors)

# AJAX PAN Verification
@app.route('/verify_pan_ajax', methods=['POST'])
def verify_pan_ajax():
    data = request.get_json()
    vendor_id = data.get('vendor_id')

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT pan_number, pan_image FROM vendors WHERE id=?", (vendor_id,))
        vendor = cursor.fetchone()
    
    if vendor:
        stored_pan, pan_image_path = vendor
        extracted_text = pytesseract.image_to_string(Image.open(pan_image_path)).strip().upper()

        stored_pan = stored_pan.strip().upper()  
        verification_status = "Matched" if stored_pan in extracted_text else "Not Matched"
        
        return jsonify({"status": verification_status})
    
    return jsonify({"status": "Error"})

if __name__ == "__main__":
    app.run(debug=True)