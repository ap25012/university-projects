import os
import requests
from dotenv import load_dotenv

# Φόρτωση των μεταβλητών από το αρχείο .env
load_dotenv()

# Ορισμός των παραμέτρων σύνδεσης
KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
TABLE_ID = os.getenv("TABLE_ID")
IP = os.getenv("SERVER_IP")
PORT = os.getenv("SERVER_PORT")

# Παράμετρος έτους για τον υπολογισμό
YEAR = 2026

# endpoint URL 
URL = f"http://{IP}:{PORT}/api/public/v1/tables/{TABLE_ID}/rows/search"

headers = {
    "accept": "application/json",
    "x-budibase-app-id": APP_ID,
    "content-type": "application/json",
    "x-budibase-api-key": KEY
}

print(f"--- Έναρξη ανάλυσης δεδομένων για το έτος {YEAR} ---")

try:
    # Λήψη δεδομένων από τον server
    response = requests.post(URL, headers=headers, json={})
    data = response.json()['data'] # Μετατροπή σε Python dictionary
    
    results = {}

    # Επανάληψη σε κάθε στοιχείο του πίνακα 
    for element in data:
        # Έλεγχος αν η άδεια είναι approved και αν ανήκει στο σωστό έτος
        status = str(element.get('status')).lower()
        ref_year = str(element.get('reference_year'))

        if status == 'approved' and ref_year == str(YEAR):
            # Λήψη ονόματος υπαλλήλου από το relationship
            emp_data = element.get('employee', [])
            name = emp_data[0].get('primaryDisplay') if emp_data else "Unknown"
            
            # Πρόσθεση ημερών στο σύνολο
            days = float(element.get('no_days', 0))
            results[name] = results.get(name, 0) + days

    # Εκτύπωση αποτελεσμάτων στην κονσόλα
    print("-" * 55)
    if not results:
        print(f"Δεν βρέθηκαν εγκεκριμένες άδειες για το {YEAR}.")
    else:
        for name, total in results.items():
            print(f"Εργαζόμενος: {name:<20} | Σύνολο Αδειών: {total} ημέρες")
    print("-" * 55)

except Exception as e:
    print(f"Παρουσιάστηκε πρόβλημα: {e}")