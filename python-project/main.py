# main.py

from service import DonationSystem
from login import login

def main():
   # --- AUTHENTICATION ---
   # Calls the login module to verify credentials before proceeding.
    is_success, role, username = login()

    if not is_success:
        return # Exit if authentication fails
    
     # --- SYSTEM INITIALIZATION & IDENTIFICATION ---
    system = DonationSystem()
    print(f" ΚΑΛΩΣΗΡΘΑΤΕ ({username}) - ΑΠΑΙΤΕΙΤΑΙ ΤΑΥΤΟΠΟΙΗΣΗ")
    print("Παρακαλώ συμπληρώστε τα στοιχεία σας για να εισέλθετε:")

    try:
        # Collecting real-world identity details to create the session
        full_name = input("Ονοματεπώνυμο: ")
        phone = int(input("Τηλέφωνο: "))
        email = input("Email: ")
        afm = int(input("ΑΦΜ: "))
    except ValueError:
        print("Σφάλμα: Το τηλέφωνο και το ΑΦΜ πρέπει να είναι αριθμοί.")
        return

    current_user = None
    current_provider = None
    
    # --- SESSION CREATION ---
    # Based on the role, we create the appropriate object in memory.
    if role == "user":
        current_user = system.create_user_session(username, full_name, phone, email, afm)
        print(f"\n Είσοδος Επιτυχής! Καλωσήρθες {current_user.full_name}.")
        
    elif role == "provider":
        current_provider = system.create_provider_session(username, full_name, phone, email, afm)
        print(f"\n Είσοδος Επιτυχής! Καλωσήρθες Πάροχε {current_provider.full_name}.")

         # --- MAIN APPLICATION ---

    while True:
        
        # UI: Display different options based on the active role
        if role == "user":
            print(f"\n--- ΜΕΝΟΥ ΔΩΡΗΤΗ (Πόντοι: {current_user.total_points}) ---")
            print("1. Προβολή Κατηγοριών (Προϊόντων)") 
            print("2. Νέα Δωρεά Προϊόντος")
            print("3. Οι Δωρεές μου")
            print("0. Έξοδος")    
        
        elif role == "provider":
            print("\n--- ΜΕΝΟΥ ΠΑΡΟΧΟΥ ---")
            print("1. Προβολή Κατηγοριών (Υπηρεσιών)") 
            print("2. Νέα Καταχώρηση Υπηρεσίας")
            print("3. Οι Υπηρεσίες μου")
            print("0. Έξοδος")

        choice = input("Επιλογή: ")

        # --- EXIT ---
        if choice == "0":
            print("Αντίο!")
            break

 # --- VIEW CATEGORIES ---
        elif choice == "1":
            if role == "user":
                print("\n--- Κατηγορίες Προϊόντων ---")
                # Fetches only relevant Product Categories
                for c in system.get_product_categories(): 
                    print(c)
            elif role == "provider":
                print("\n--- Κατηγορίες Υπηρεσιών ---")
                # Fetches only relevant Service Categories
                for c in system.get_service_categories(): 
                    print(c)

        # --- NEW REGISTRATION ---
        elif choice == "2":
            
            # User creates a Product
            if role == "user":
                print("\n--- Νέα Δωρεά Προϊόντος ---")
                # Show valid categories first
                for c in system.get_product_categories(): print(c)
                
                try:
                    category_id = int(input("ID Κατηγορίας: "))
                    name = input("Ονομασία: ")
                    brand = input("Μάρκα: ")
                    p_year = int(input("Έτος Αγοράς: "))
                    u_years = int(input("Έτη Χρήσης: "))
                    photo = input("Αρχείο φωτογραφίας: ")

                     # Registers the product to the current user
                    res = system.register_product(current_user, category_id, name, brand, p_year, u_years, photo)
                    
                    if res: 
                        print("\n Η δωρεά ολοκληρώθηκε!")
                  # If validation fails, the service class prints the error message.
                except ValueError:
                    print(" Λάθος είσοδος (δώστε αριθμούς όπου απαιτείται).")

                         # Provider creates a Service
            elif role == "provider":
                print("\n--- Νέα Υπηρεσία ---")
                # Show valid categories first
                for c in system.get_service_categories(): print(c)
                
                try:
                    category_id = int(input("ID Κατηγορίας: "))
                    s_name = input("Τίτλος Υπηρεσίας: ")
                    desc = input("Περιγραφή: ")
                    time = input("Διαθέσιμος Χρόνος: ")
                    
                    # Registers the service to the current provider
                    res = system.register_service(current_provider, category_id, s_name, desc, time)
                    
                    if res: 
                        print("\n Η υπηρεσία καταχωρήθηκε!")
                except ValueError:
                    print(" Λάθος είσοδος.")

                      # --- VIEW HISTORY ---
        elif choice == "3":
            
            if role == "user":
                print("\n--- Οι Δωρεές μου ---")
                # Retrieve items owned by this user
                items = system.get_user_products(current_user)
                if not items: print("Κανένα προϊόν.")
                else: 
                    for i in items: print(i)

            elif role == "provider":
                print("\n--- Οι Υπηρεσίες μου ---")
                # Retrieve services offered by this provider
                items = system.get_provider_services(current_provider)
                if not items: print("Καμία υπηρεσία.")
                else: 
                    for i in items: print(i)

        else:
            print("Μη έγκυρη επιλογή.")

if __name__ == "__main__":
    main()