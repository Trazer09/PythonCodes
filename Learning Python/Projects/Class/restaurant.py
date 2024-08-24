class Restaurant: 
    """"A simple Restaurant Class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
       
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Retaurant is open!")

    def set_number_served(self, update_served):
        self.numberserved = update_served

    def increment_number_served(self, increment_serve):
        self.number_served += increment_serve
    
restaurant = Restaurant("Indian Taste"," Indian")
restaurant.set_number_served(25)
restaurant.increment_number_served(8)
print(f"Total number of serving in a day: {restaurant.number_served}")