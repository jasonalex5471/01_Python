def register_ship(name,ship_type='Cargo'):
    """print the registration information"""
    print(f"the {name} {ship_type} has"
          "already registered")
    
def buld_ship_profile(name, tonnage, **additional_info):
    all_information = {
        'name' : name,
        'tonnage' : tonnage,
        **additional_info
    }
    return all_information

def process_verification(unverified_ships, verified_ships):
    while unverified_ships:
        verified_ship = unverified_ships.pop()
        verified_ships.append(verified_ship)
        print("verifiying...")
        print(f"the {verified_ship} passed!")
    show_verified_ships(verified_ships)

def show_verified_ships(verified_ships):
    print(verified_ships)
    
def collect_cargo(*cargo_items):
    print(cargo_items)