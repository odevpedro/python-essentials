# If-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Nested if-else statement
y = 7
if y > 10:
    print("y is greater than 10")
elif y > 5:
    print("y is greater than 5 but not greater than 10")
else:
    print("y is not greater than 5")

# For loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1


# Break statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Exit the loop if num is 3
    print(num)

# Continue statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue  # Skip the rest of the loop and continue with the next iteration if num is 3
    print(num)

# While loop with break statement
count = 0
while count < 5:
    if count == 3:
        break  # Exit the loop if count is 3
    print("Count:", count)
    count += 1

# While loop with continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop and continue with the next iteration if count is 3
    print("Count:", count)
