ships = ['Maersk','MSC','CMA CGM','Hapag-Lloyd']
print(f"welcome {ships[0]} enter the port")
print(f"\nthe last one is {ships[-1]}")

ships[-1] = 'spaceship'
ships.append('new_ship')
ships.insert(0,'medical_ship')

del ships[2]
leaving_ship = ships.pop()
print(f"\nthe {leaving_ship} was leaving")

ships.remove('spaceship')

print("-" * 15)
print("the original list is")
print("-" * 15)
print("\n")
print(ships)
print("\n")

print("-" * 15)
print("the sorted list is")
print("-" * 15)
print("\n")
print(sorted(ships))
print("\n")

print("-" * 15)
print("the original list is")
print("-" * 15)
print("\n")
print(ships)
print("\n")

ships.reverse()
print(ships)
print("\n")

ships.sort()
print(ships)
print("\n")

print(len(ships))