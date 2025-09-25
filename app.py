from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3
from passlib.hash import bcrypt
from email_validator import validate_email, EmailNotValidError
import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(APP_DIR, "users.db")

app = Flask(__name__)
# NOT: session/token kullanılmıyor (görev koşuluna göre)


def get_db_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """DB oluştur / tabloları hazırla"""
    with get_db_conn() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            );
        """)
        conn.commit()


@app.route("/", methods=["GET"])
def index():
    # index.html içinde hem login hem register formları var
    return render_template("index.html", message=None)


@app.route("/register", methods=["POST"])
def register():
    # Güvenlik: sadece POST alıyoruz, parametreleri temizle
    username = (request.form.get("username") or "").strip()
    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password") or ""

    # Basic validation
    if not username or not email or not password:
        # genel mesaj: kullanıcıya fazla detay verme
        return render_template("index.html", message="Zəhmət olmasa bütün sahələri doldurun.")

    # email doğrula
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError:
        return render_template("index.html", message="E-mail formatı düzgün deyil.")

    # şifre uzunluğu kontrolü (temel)
    if len(password) < 8:
        return render_template("index.html", message="Şifrə ən az 8 simvol olmalıdır.")

    # password hashle
    pw_hash = bcrypt.hash(password)

    # DB'ye ekle (parametreli query, duplicate e-mail kontrolü)
    try:
        with get_db_conn() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?);",
                      (username, email, pw_hash))
            conn.commit()
    except sqlite3.IntegrityError as e:
        # muhtemelen UNIQUE constraint: email zaten var
        return render_template("index.html", message="Bu e-mail ilə artıq qeydiyyat mövcuddur.")
    except Exception as e:
        # gizli hata mesajı vermeyelim, sadece generic
        return render_template("index.html", message="Sistemdə xəta baş verdi. Yenidən cəhd edin.")

    # başarılı kayıt => giriş formunu göster (veya doğrudan başarılı sayfası)
    return render_template("index.html", message="Qeydiyyat uğurludur. İndi daxil ola bilərsiniz.")


@app.route("/login", methods=["POST"])
def login():
    # Görev: e-mail + password kontrolü, başarılıysa dashboard render et.
    email = (request.form.get("email_login") or "").strip().lower()
    password = request.form.get("password_login") or ""

    if not email or not password:
        # genel mesaj
        return render_template("index.html", message="E-mail və ya şifrə yanlışdır")

    try:
        with get_db_conn() as conn:
            c = conn.cursor()
            c.execute("SELECT id, username, email, password_hash FROM users WHERE email = ? LIMIT 1;", (email,))
            row = c.fetchone()
            if row is None:
                return render_template("index.html", message="E-mail və ya şifrə yanlışdır")

            pw_hash = row["password_hash"]
            # bcrypt verify
            if not bcrypt.verify(password, pw_hash):
                return render_template("index.html", message="E-mail və ya şifrə yanlışdır")

            # Başarılı giriş: görev talebine uygun olarak session/token kullanılmayacak.
            # Bu nedenle burada sadece POST isteğine karşılık dashboard render ediyoruz.
            # NOT: Direkt GET /dashboard erişimi kısıtlıdır (aşağıda).
            user = {"id": row["id"], "username": row["username"], "email": row["email"]}
            return render_template("dashboard.html", user=user)
    except Exception as e:
        # gizli hata mesajı
        return render_template("index.html", message="E-mail və ya şifrə yanlışdır")


@app.route("/dashboard", methods=["GET"])
def dashboard_get():
    # Görev: session/token kullanılmadığı için direkt GET ile dashboard'a erişimi engelle
    # Eğer ileride session eklenirse burayı düzenleyin.
    abort(403)


if __name__ == "__main__":
    # Eğer DB yoksa oluştur
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
