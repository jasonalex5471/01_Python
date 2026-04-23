from port_functions import register_ship as rs
from port_functions import buld_ship_profile as bsp
from port_functions import process_verification as pv
from port_functions import collect_cargo as cc

#part 1
rs('ship1')
rs('ship2','medical_ship')
rs(ship_type='military_ship',name='ship3')

#part 2
all_information = bsp('Cargo',10000,origin='Shanghai',captain='Li')
print(all_information)

#part 3
unverified_ships = ['oil_cargo','medical_ship','unknown_ship']
verified_ships = []
pv(unverified_ships,verified_ships)

#part 4
cc('oil','fish','metal')