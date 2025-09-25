🚀 Klickon Auth Demo – INT-SEC-02

A secure and minimal Login/Register system built with Python and Flask, designed to demonstrate safe authentication practices in real-world applications. This project serves as a foundation for security testing and penetration exercises.

✨ Features
🔐 Register

Users can register with:

Username

Email

Password

Passwords are hashed using bcrypt or argon2 for security.

Duplicate email registration is prevented.

🔑 Login

Users can log in with email and password.

Successful login redirects to a dashboard page.

Failed login shows a generic error message:

Email or password is incorrect


No sessions or tokens are used (task requirement).

📊 Dashboard

Accessible only after successful login.

Can display user-specific content.

🛠 Technologies
Component	Technology
Backend	Python + Flask
Database	SQLite (MySQL optional)
Password Hashing	bcrypt / argon2
Security Measures	SQL injection prevention, password hashing, duplicate email check
⚡ Installation & Running

Create and activate a virtual environment:

python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open in your browser:

http://127.0.0.1:5000

📝 Endpoints
Route	Method	Description
/register	GET/POST	User registration page/form
/login	GET/POST	User login page/form
/dashboard	GET	Dashboard page, protected
🔒 Security Notes

Passwords are never stored in plain text – always hashed.

Duplicate email registrations are blocked.

SQL injection is mitigated through parameterized queries.

Session or token management is intentionally excluded for this task.

🎯 Project Goal

This project demonstrates:

How to create a secure authentication system.

How to handle user data safely.

A baseline system for future penetration testing exercises.
