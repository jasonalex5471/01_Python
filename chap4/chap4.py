cargos = list(range(1,21))
costs = list((cargo**2)+10 for cargo in cargos) 

cargo_types = ['Grain', 'Oil', 'Iron', 'Cars', 'Coal']
for cargo_type in cargo_types:
    print(f"Checking storage for {cargo_type} done!")
    
print("all the cargos are set")

ships = ['Maersk','MSC','CMA CGM','Hapag-Lloyd','madical ship','new_ship']
print("the first three ships are priority")
print("\n")
print(ships[:3])
print("\n")
print(ships[2:3])
print("\n")

emergence_queue = ships[:]
ships.append('atlantic')
emergence_queue.append('boat')
print(ships)
print("\n")
print(emergence_queue)

PORT_COORDINATES = (11.2,113.21)

PORT_COORDINATES = (11.3,113.21)