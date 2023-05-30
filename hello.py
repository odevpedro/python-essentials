import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print("Random integer:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float (0-1):", random_float)

# Generate a random floating-point number between 2.5 and 5.5
random_float_range = random.uniform(2.5, 5.5)
print("Random float (range):", random_float_range)

# Generate a random element from a list
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random element from list:", random_element)
