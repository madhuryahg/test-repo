'''Class used for Restaurant info'''


class RestaurantInfo():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"We are {self.restaurant_name} . Our cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, customer):
        self.number_served = customer

    def increment_number_served(self, total):
        self.number_served += total


class IceCreamStand(RestaurantInfo):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = ['Strawberry', 'apple', 'mango', 'pista']
        self.custom = Customisation(input('What container do you want?'))

    def flavours_available(self):
        print("The available flavours are")
        for item in self.flavour:
            print(item)


class Customisation():
    def __init__(self, container='cone'):
        self.container = container

    def container_type(self):
        if self.container == 'bowl':
            return print(f'{self.container} icecream')
        elif self.container == 'cone':
            return print(f'{self.container} icecream')
