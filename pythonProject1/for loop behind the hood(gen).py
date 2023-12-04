def my_for_generator(iteratable):
    iterator = iter(iteratable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_for_generator(my_list)
