import sqlite3
from passlib.hash import bcrypt

DB = "users.db"

def list_users():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, username, email, password_hash FROM users;")
    rows = cur.fetchall()
    for r in rows:
        id_, u, e, h = r
        print(f"id={id_} | user={u} | email={e} | hash_prefix={h[:6]}... | len={len(h)}")
    conn.close()

def verify_sample(email, plain_password):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE email = ? LIMIT 1;", (email,))
    row = cur.fetchone()
    conn.close()
    if not row:
        print("Kullanıcı bulunamadı.")
        return
    stored_hash = row[0]
    ok = bcrypt.verify(plain_password, stored_hash)
    print("Password match?" , ok)

if __name__ == "__main__":
    list_users()

