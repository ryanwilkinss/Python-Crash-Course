# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

guests = ['elliott', 'andreas', 'scotty']

guests.insert(0, 'jimmie')
guests.insert(2, 'lukas')
guests.append('dan')

print(f"I'm sorry {guests[0].title()}, we only have room for two for tonight")
print(f"I'm sorry {guests[1].title()}, we only have room for two for tonight")
print(f"I'm sorry {guests[2].title()}, we only have room for two for tonight")
print(f"I'm sorry {guests[3].title()}, we only have room for two for tonight")
print(f"I'm sorry {guests[4].title()}, we only have room for two for tonight")
print(f"I'm sorry {guests[5].title()}, we only have room for two for tonight")

print(f"I'm sorry {guests[2].title()}, I can't invite you to dinner tonight")
guests.pop(2)

print(f"I'm sorry {guests[2].title()}, I can't invite you to dinner tonight")
guests.pop(2)

print(f"I'm sorry {guests[2].title()}, I can't invite you to dinner tonight")
guests.pop(2)

print(f"I'm sorry {guests[2].title()}, I can't invite you to dinner tonight")
guests.pop(2)

print(f'{guests[0].title()} you are still invited.')
print(f'{guests[1].title()} you are still invited.')

del guests[1]
del guests[0]

print(guests)
