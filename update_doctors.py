import json
import sqlite3

def update_doctors():
    # Load JSON data
    with open('doctors_info.json', 'r', encoding='utf-8') as f:
        doctors_data = json.load(f)

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM doctors")
    
    # Reset auto-increment sequence (optional but cleaner)
    try:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='doctors'")
    except sqlite3.OperationalError:
        pass # sqlite_sequence might not exist if no autoincrement usage previously or different sqlite version quirks so we ignore

    print("Old data removed.")

    # Insert new data
    for doc in doctors_data:
        # Map fields
        name = doc.get('name')
        specialization = doc.get('department')
        
        # Handle available_days which is a list in JSON
        days = doc.get('available_days')
        if isinstance(days, list):
            available_days = ", ".join(days)
        else:
            available_days = str(days)
            
        available_times = doc.get('timings')
        
        # We are not using 'id' from JSON to let DB autoincrement or we can force it. 
        # Since JSON has IDs, let's try to keep them if possible, but the schema has AUTOINCREMENT.
        # It's usually safer to let DB handle ID if we don't strict foreign key dependencies yet.
        # However, to match the JSON exactly, let's insert provided values excluding ID and let SQLite generate new ones 
        # OR insert ID if we want consistency. Given the prompt "update data from ... json", 
        # let's just insert the content fields.
        
        cursor.execute("""
            INSERT INTO doctors (name, specialization, available_days, available_times)
            VALUES (?, ?, ?, ?)
        """, (name, specialization, available_days, available_times))

    conn.commit()
    print(f"Inserted {len(doctors_data)} records.")
    conn.close()

if __name__ == "__main__":
    update_doctors()
