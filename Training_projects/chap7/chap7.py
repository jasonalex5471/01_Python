#part 1

msg = "please input the name of ship"
msg += "\nenter 'q' to quit"

current_ships = []
flag = True
while flag:
    current_ship = input(msg).strip()
    if current_ship != 'q':
        current_ships.append(current_ship.title())
    else:
        flag = False    
for current_ship in current_ships:
    print(f"- {current_ship}")

#part 2

while True:
    current_ship = input(msg)
    if current_ship == 'pirate' or current_ship == 'unknown':
        continue
    elif current_ship == 'q':
        break
    elif current_ship == 'EMERGENCY_STOP':
        print("the system has detected error,closing...")
        break
    else:
        current_ships.append(current_ship.title())

#part 3

unverified_ships = ['oil_cargo','medical_ship','unknown_ship']
verified_ships = []

while unverified_ships:
    verified_ship = unverified_ships.pop()
    verified_ships.append(verified_ship)
    print("verifiying...")
    print(f"the {verified_ship} passed!")

