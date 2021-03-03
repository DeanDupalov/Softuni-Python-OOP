class Customer:
    ID: int = 1
    name: str
    address: str
    email: str

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.ID
        Customer.ID += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


    @staticmethod
    def get_next_id():
        return Customer.ID
