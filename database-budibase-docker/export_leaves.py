import os
import csv
import requests
from dotenv import load_dotenv

# Φόρτωση Μεταβλητών από το .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
TABLE_ID = os.getenv("TABLE_ID")
IP = os.getenv("SERVER_IP")
PORT = os.getenv("SERVER_PORT")

# Endpoint URL
URL = f"http://{IP}:{PORT}/api/public/v1/tables/{TABLE_ID}/rows/search"

headers = {
    "accept": "application/json",
    "x-budibase-app-id": APP_ID,
    "content-type": "application/json",
    "x-budibase-api-key": API_KEY
}

print("Γίνεται λήψη δεδομένων από τον server...")

try:
    # Λήψη δεδομένων
    response = requests.post(URL, headers=headers, json={})
    data = response.json()['data']
    
    # Ορισμός στηλών για το CSV
    columns = ['display_name', 'employee', 'no_days', 'status', 'reference_year', 'start_date', 'end_date']
    
    # Εξαγωγή στο αρχείο leaves_export.csv
    with open('leaves_export.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        
        
        for element in data:
            # Επεξεργασία του employee για την εμφάνιση μόνο του ονόματος)
            emp_data = element.get('employee', [])
            if isinstance(emp_info := emp_data, list) and len(emp_info) > 0:
                element['employee'] = emp_info[0].get('primaryDisplay', 'Unknown')
            
            writer.writerow(element)
            
            # Εκτύπωση επιβεβαίωσης στο τερματικό
            print(f"Εξαγωγή: {element.get('display_name')} | Υπάλληλος: {element.get('employee')} | Έτος: {element.get('reference_year')}")
            
    print(f"\nΕπιτυχία! Το αρχείο 'leaves_export.csv' ενημερώθηκε με {len(data)} εγγραφές.")

except Exception as e:
    print(f"Σφάλμα κατά την εξαγωγή: {e}")