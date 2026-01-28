import json
import sqlite3

def update_patients():
    # Load JSON data
    with open('pseudo_patients_info.json', 'r', encoding='utf-8') as f:
        patients_data = json.load(f)

    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM patients")
    try:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='patients'")
    except sqlite3.OperationalError:
        pass

    print("Old data removed.")

    # Insert new data
    for patient in patients_data:
        name = patient.get('name')
        dob = patient.get('dob')
        contact_info = patient.get('contact_info')
        
        # Consistent unique_key generation
        unique_key = f"{name}_{contact_info}"
        
        cursor.execute("""
            INSERT INTO patients (name, dob, contact_info, unique_key)
            VALUES (?, ?, ?, ?)
        """, (name, dob, contact_info, unique_key))

    conn.commit()
    print(f"Inserted {len(patients_data)} records.")
    conn.close()

if __name__ == "__main__":
    update_patients()
