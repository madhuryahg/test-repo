from functools import reduce


def capital(item):
    return item.upper()


def check_percentage(marks):
    return marks > 50


def total(initial, score):
    return initial + score


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capital, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
# my_numbers.sort()
# new_list = list(map(ascend, my_numbers))
print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(check_percentage, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(total, (scores + my_numbers)))
print(scores + my_numbers)