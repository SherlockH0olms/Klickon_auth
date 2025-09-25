import sqlite3
DB = "users.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("DELETE FROM users;")
conn.commit()

cur.execute("VACUUM;")
conn.close()
print("Tüm kullanıcı kayıtları silindi ve DB VACUUM yapıldı.")
