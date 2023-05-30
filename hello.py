# Prompt the user for input
user_input = input("Enter something: ")

# Display the user input
print("You entered:", user_input)
# Prompt the user for input
user_input = input("Enter something: ")

# Display the user input
print("You entered:", user_input)


# Print a welcome message
print("*********************************")
print("Welcome to the Guessing Game!")
print("*********************************")

# Set the secret number
secret_number = 42

# Get the user's guess
guess_str = input("Enter your guess: ")
print("You entered: ", guess_str)
guess = int(guess_str)

# Check if the guess is correct
if guess == secret_number:
    print("Congratulations! You guessed correctly!")
else:
    print("Sorry, that's incorrect.")

# Print the end of the game message
print("End of the game")