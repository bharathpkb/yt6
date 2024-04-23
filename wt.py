class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.customers = []  # Assuming this list is used to store customer objects
    
    def add(self):
        customer_info = {
            "name": self.name,
            "email": self.email,
            "address": self.address
        }
        self.customers.append(customer_info)
        print(f"Customer '{self.name}' added successfully.")
    
    def update(self, name, new_email=None, new_address=None):
        for customer in self.customers:
            if customer["name"] == name:
                if new_email:
                    customer["email"] = new_email
                if new_address:
                    customer["address"] = new_address
                print(f"Customer '{name}' details updated.")
                return
        print(f"Customer '{name}' not found.")
    
    def delete(self, name):
        for customer in self.customers:
            if customer["name"] == name:
                self.customers.remove(customer)
                print(f"Customer '{name}' deleted successfully.")
                return
        print(f"Customer '{name}' not found.")
    
    def display(self):
        if not self.customers:
            print("No customers to display.")
        else:
            print("List of customers:")
            for customer in self.customers:
                print(f"Name: {customer['name']}, Email: {customer['email']}, Address: {customer['address']}")


customer_manager = Customer(name="John Doe", email="john@example.com", address="123 Main St")


customer_manager.add()


customer_manager.display()


customer_manager.update(name="John Doe", new_email="john.doe@example.com")
customer_manager.display()
customer_manager.delete(name="John Doe")
