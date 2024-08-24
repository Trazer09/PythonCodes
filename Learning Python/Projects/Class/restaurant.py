class Restaurant:
    """A simple Restaurant Class"""
    
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Shows the name and cuisine"""
        return f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}"

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("Restaurant is open!")

    def set_number_served(self, update_served: int):
        """Sets the number of people served."""
        self.number_served = update_served

    def increment_number_served(self, increment_serve: int):
        """Increments the number of people served."""
        self.number_served += increment_serve

# Create an instance of Restaurant
restaurant = Restaurant("Indian Taste", "Indian")

# Call methods to update and display information
restaurant.set_number_served(25)
restaurant.increment_number_served(8)
print(restaurant.describe_restaurant())
print(f"Total number of servings in a day: {restaurant.number_served}")

# Call the method to indicate that the restaurant is open
restaurant.open_restaurant()
