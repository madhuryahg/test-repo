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
        self.custom = Customisation('bowl')
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

# restaurant1 = RestaurantInfo('Mads', 'Asian')
# restaurant2 = RestaurantInfo('Nis', 'Italian')
# restaurant3 = RestaurantInfo('Anu', 'Indian')
#
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type)
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
#
# restaurant1.open_restaurant()
#
# print(restaurant1.number_served)
# restaurant1.set_number_served(50)
# print(restaurant1.number_served)
# restaurant1.increment_number_served(50)
# print(restaurant1.number_served)


buy_ice = IceCreamStand('Mads Ice', 'Icecreams')
print(buy_ice.restaurant_name)
buy_ice.flavours_available()
print(buy_ice.number_served)
print(buy_ice.custom.container_type())
print(buy_ice.custom.container_type())
