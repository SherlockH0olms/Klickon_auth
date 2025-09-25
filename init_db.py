# opsiyonel: ayrı init script
from app import init_db
if __name__ == "__main__":
    init_db()
    print("DB initialized.")