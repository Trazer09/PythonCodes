class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"Retaurant is open!")


res1 = Restaurant("Shark Clam", "Italian")
print(res1.restaurant_name)
print(res1.cuisine_type)
res1.describe_restaurant()
res1.open_restaurant()
