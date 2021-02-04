# 3-9. len()

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

print(f'There is only ', len(guests), ' people left on the list.')
print(guests)
