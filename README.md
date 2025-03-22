**OCR-Based Data Extraction Module

Overview**

This project is an OCR-Based Data Extraction Module designed for the Ministry of New and Renewable Energy, Government of India. The system automates vendor registration and PAN card verification using Flask, Tesseract OCR, Bootstrap, and SQLite. It provides an interactive web-based experience for uploading, extracting, and validating PAN card details.

**Features**

User Authentication: Secure login/logout system.

Vendor Registration: Stores vendor details, including PAN number and uploaded PAN image.

OCR-Based PAN Verification: Extracts and validates PAN numbers from uploaded images.

Interactive UI: Modern, responsive, and easy-to-navigate design.

Instant Pop-up Notifications: Displays success/error messages in a centered, visually appealing toast notification.

View PAN Image: Opens the PAN image in a new tab.

Export Options: Allows exporting data in PDF, CSV, and Excel formats.

Navigation: Includes a "Back to Home" button for better user experience.

**Technology Stack**

Frontend: HTML, CSS, Bootstrap, JavaScript, jQuery

Backend: Flask (Python)

Database: SQLite

OCR Processing: Tesseract OCR

Installation

Install dependencies:

pip install -r requirements.txt

Initialize the database:

python init_db.py

Run the Flask application:

python app.py

Open the application in your browser:

http://127.0.0.1:5000/

**Usage**

Login: Enter credentials to access the system.

Vendor Registration: Fill out the form and upload the PAN image.

Data Management: View registered vendors and their PAN details.

PAN Verification:Click Verify to check if extracted PAN matches the stored one.

A pop-up notification displays verification status.

View PAN Image: Click View to open the image in a new tab.

Export Data: Download vendor records in PDF, CSV, or Excel formats.

Navigation: Use the Back to Home button to return to the homepage.

**Folder Structure**


├── static/

│   ├── css/           # Stylesheets

│   ├── js/            # JavaScript files

│   ├── uploads/       # Uploaded PAN images

├── templates/         # HTML templates

│   ├── home.html

│   ├── login.html

│   ├── vendor_registration.html

│   ├── data_management.html

│   ├── pan_verification.html

├── app.py             # Main Flask application

├── init_db.py         # Database initialization script

├── requirements.txt   # Python dependencies

├── README.md          # Project documentation

**Dependencies**

Flask

SQLite

Tesseract OCR

Bootstrap

jQuery

pandas (for exporting data)

**Contribution**
Feel free to contribute by submitting pull requests or reporting issues.

**License**
This project is licensed under the MIT License.

**Contact**
For any inquiries, contact your nkishansaireddy16@egmail.com.

