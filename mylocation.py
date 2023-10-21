# Define a class with variables for **name** and **country**.
# Then define a method that belongs to the class. The method’s
# purpose is to print a sentence that uses the variables.
class location:
    def __init__(self, name, country):
        self.name = name
        self.country = country 
    
    def myLocation(self):
        print(f"ola meu nome é {self.name} e eu moro em {self.country}")

# First instantiation of the Location class
loc1 = location("Michael Sergio", "Itaquaquecetuba")
# Call a method from the instantiated class

# Three more instantiations and method calls for the Location class
loc2 = location("Rafael Silva", "Portugual")
loc3 = location("Locas", "Bahia")
yourloc = location("Cleia", "Itaim paulista")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
yourloc.myLocation()