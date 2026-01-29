from db_handler import init_db

DB_PATH = "hospital.db"
if __name__ == "__main__":
    init_db(DB_PATH)
    print(f"Database initialized at {DB_PATH}")