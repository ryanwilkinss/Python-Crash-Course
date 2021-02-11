# Use a dictionary to store people’s favorite numbers. Think of five names, 
# and use them as keys in your dictionary. Think of a favorite number for each 
# person, and store each as a value in your dictionary. Print each person’s 
# name and their favorite number. For even more fun, poll a few friends and get 
# some actual data for your program.
favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000_000,
    'maggie': 0,
    }

num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")
