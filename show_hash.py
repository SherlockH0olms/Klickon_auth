import sqlite3

DB = "users.db"
email = "hqmbrli@inbox.ru"   # burada istədiyin e-maili dəyişə bilərsən

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT id, username, email, password_hash FROM users WHERE email = ? LIMIT 1;", (email,))
row = cur.fetchone()
conn.close()

if not row:
    print("Kayıt tapılmadı:", email)
else:
    id_, username, mail, phash = row
    print("id:", id_)
    print("username:", username)
    print("email:", mail)
    print("password_hash:", phash)
