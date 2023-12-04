#creating a generator

def my_generator(num):
    print('in gen')
    for i in range(num):
        print('in for')
        yield i*2


def gen_list(num):
      print('in list')
      for it in my_generator(num):
          print('in calling fun')
          print(it)

gen_list(10)

# g=my_generator(10)
# next(g)
# print(next(g))
# print(next(g))
# print(next(g))
