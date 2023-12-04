from restaurant import RestaurantInfo
from restaurant import IceCreamStand

my_new_restaurant = RestaurantInfo('Nis', 'German')
print(my_new_restaurant.restaurant_name)
my_new_restaurant.describe_restaurant()
ice = IceCreamStand('jack','gelato')
ice.restaurant_name = 'Mikos'
print(ice.restaurant_name)
ice.custom.container_type()