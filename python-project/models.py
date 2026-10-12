# models.py

class User: # Represents a user
    def __init__(self, user_id: int, username: str, password: str, full_name: str, phone: int, email: str, AFM: int, total_points: int = 0):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.AFM = AFM
        self.total_points = total_points
        
    def add_points(self) -> None:
        # TODO: αύξησε τον αριθμό των πόντων κατά 10
        self.total_points += 10
        print(f"Προστέθηκαν 10 πόντοι στον χρήστη {self.full_name}.")
        print(f"Νέο σύνολο πόντων: {self.total_points}")
        
    def __str__(self) -> str: # String representation of the user
        return f"{self.user_id}: {self.username}, {self.password}, {self.full_name}, {self.phone}, {self.email}, {self.AFM} ,{self.total_points}"
    
class Provider: # Represents a provider
    def __init__(self, provider_id: int, username: str, password: str, full_name: str, phone: int, email: str, AFM: int):
        self.provider_id = provider_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.AFM = AFM
        
    def __str__(self) -> str: # String representation of the provider
        return f"{self.provider_id}: {self.username}, {self.password}, {self.full_name}, {self.phone}, {self.email}, {self.AFM}"


class Category: # Represents a Product Category or a Service Category
    def __init__(self, category_id: int, category_name: str ,category_type: str):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type # product ή service

    def __str__(self) -> str:
            return f"{self.category_id}. {self.category_name} "
    
class Product: # Represents a product
    def __init__(self, product_id: int, prod_name: str, prod_brand: str, purchase_year: int, usage_years: int , prod_photo: str , category: Category , user: User, is_available: bool = True):
        self.product_id = product_id
        self.prod_name = prod_name
        self.prod_brand = prod_brand
        self.purchase_year = purchase_year
        self.usage_years = usage_years
        self.prod_photo = prod_photo
        self.category = category 
        self.user = user       
        self.is_available = is_available

    def check_availability(self) -> bool:
        # TODO: επιστρέψτε True αν είναι διαθέσιμο το προϊόν
        return self.is_available >= 1 


    def __str__(self) -> str: # String representation of the class product
        return (f"Όνομα: {self.prod_name}, Μάρκα: {self.prod_brand}, Έτος αγορας: {self.purchase_year}, Χρόνια χρήσης: {self.usage_years}")
   
class Service: # Represents a service
    def __init__(self, service_id: int, service_name: str, service_description: str, available_time: str,  category: Category , provider: Provider, is_available: bool = True):
        self.service_id = service_id
        self.service_name = service_name
        self.service_description = service_description
        self.available_time = available_time
        self.category = category
        self.provider = provider
        self.is_available = is_available    
    
    
    def check_availability(self) -> bool:
        # TODO: επιστρέψτε True αν είναι διαθέσιμη η υπηρεσία
        return self.is_available 
    
    
    def __str__(self) -> str:
        return f" Όνομα: {self.service_name}, Περιγραφή: {self.service_description}, Διαθέσιμος Χρόνος: {self.available_time}"
