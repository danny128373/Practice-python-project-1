import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Forest
from environments import Mountain

from arboretum import Arboretum


def annex_habitat(Arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++")
    print("+ C H O O S E  A  H A B I T A T +")
    print("+-++-++-++-++-++-++-++-++-++-++-++")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        Arboretum.rivers.append(river)
        print('New river habitat was created!')
        input('Please press any key to continue...')
    if choice == "2":
        swamp = Swamp()
        Arboretum.swamps.append(swamp)
        print('New swamp habitat was created!')
        input('Please press any key to continue...')

    if choice == "3":
        coastline = Coastline()
        Arboretum.coastlines.append(coastline)
        print('New coastline habitat was created!')
        input('Please press any key to continue...')

    if choice == "4":
        grassland = Grassland()
        Arboretum.grasslands.append(grassland)
        print('New grassland habitat was created!')
        input('Please press any key to continue...')

    if choice == "5":
        forest = Forest()
        Arboretum.forests.append(forest)
        print('New forest habitat was created!')
        input('Please press any key to continue...')

    if choice == "6":
        mountain = Mountain()
        Arboretum.mountains.append(mountain)
        print('New mountain habitat was created!')
        input('Please press any key to continue...')
