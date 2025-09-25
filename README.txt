Klickon Auth Demo – INT-SEC-02

This project is a secure and minimal Login/Register system designed to demonstrate how authentication systems are safely implemented in real-world applications. It provides a foundation for later penetration testing and security exercises.

Features

Register

Users can register with a username, email, and password

Passwords are hashed using bcrypt or argon2 before being stored

Duplicate email registration is not allowed

Login

Users can log in using email and password

Successful login redirects to the dashboard

Failed login shows a generic message: "Email or password is incorrect"

No sessions or tokens are used (as per task requirements)

Dashboard

Accessible only after successful login

Can display user-specific content

Technologies

Backend: Python + Flask

Database: SQLite (MySQL is also supported)

Password Hashing: bcrypt / argon2

Security measures: SQL injection protection, password hashing, and duplicate email checks

Installation and Running

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open your browser:

http://127.0.0.1:5000

Notes

Passwords are never stored in plain text; they are securely hashed.

This version is a secure baseline, ready for further development with sessions, tokens, or advanced security features.

The project serves as a foundation for penetration testing and security learning exercises.
