requested_ships = ['cargo_1', 'medical_ship', 'cargo_2', 'oil_tanker', 'illegal_ship']

for requested_ship in requested_ships:
    if requested_ship == 'medical_ship':
        print("Priority Access: Medical ship detected! Clear the way.")
    elif requested_ship == 'illegal_ship':
        print("ALERT: Illegal ship blocked! Security dispatched!")
    else:
        print(f"welcome {requested_ship}!")

tonnages = [2500, 3000, 5800, 21000, 2000]

for value in range(len(tonnages)):
    if tonnages[value] < 5000:
        print(f"{requested_ships[value]} charge for $100")
    elif (tonnages[value] >= 5000) and (tonnages[value] <20000):
        print(f"{requested_ships[value]} charge for $500") 
    elif tonnages[value] >= 20000:
        print(f"{requested_ships[value]} charge for $1200")

for value in range(len(requested_ships)):
    if (requested_ships[value] == 'oil_tanker') and (tonnages[value] >= 15000):
        print("Oil tanker over 15k tons: Extra tugboats required for safety.")

incoming_queue = []
if not incoming_queue:
    print("Port is empty, no ships to process.")