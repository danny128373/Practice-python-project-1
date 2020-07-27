from animals import RiverDolphin
from environments import River
from animals import HappyFacedSpider
from animals import GoldDustDayGecko
from animals import Kikakapu
from animals import NeneGoose
from animals import Opeapea
from animals import Pueo
from animals import Ulae


def release_animal(arboretum):

    biome_list = arboretum.rivers + arboretum.swamps + arboretum.grasslands + \
        arboretum.forests + arboretum.coastlines + arboretum.mountains

    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("+ C H O O S E  A N I M A L  F O R  R E L E A S E +")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")

    print('1. Gold Dust Day Gecko')
    print('2. Happy Faced Spider')
    print('3. Kikakapu')
    print('4. Nene Goose')
    print('5. Opeapea')
    print('6. Pueo')
    print('7. River Dolphin')
    print('8. Ulae')

    choice = input("Choose animal to release > ")

    if choice == "1":
        gold_dust_day_gecko = GoldDustDayGecko()
        arboretum.gold_dust_day_geckos.append(gold_dust_day_gecko)
        animal = river_dolphin
    if choice == "2":
        happy_faced_spider = HappyFacedSpider()
    if choice == "3":
        kikakapu = Kikakapu()
    if choice == "4":
        nene_goose = NeneGoose()
    if choice == "5":
        opeapea = Opeapea()
    if choice == "6":
        pueo = Pueo()
    if choice == "7":
        river_dolphin = RiverDolphin()
        arboretum.river_dolphins.append(river_dolphin)
        animal = river_dolphin
    if choice == "8":
        ulae = Ulae()

    print("Release the animal into which biome?")

    counter = 0
    for river in arboretum.rivers:
        print(f'{counter + 1}. River [{river.id}]')
        counter += 1
    for swamp in arboretum.swamps:
        print(f'{counter + 1}. Swamp [{swamp.id}]')
        counter += 1
    for grassland in arboretum.grasslands:
        print(f'{counter + 1}. Grassland [{grassland.id}]')
        counter += 1
    for forest in arboretum.forests:
        print(f'{counter + 1}. Forest [{forest.id}]')
        counter += 1
    for coastline in arboretum.coastlines:
        print(f'{counter + 1}. Coastline [{coastline.id}]')
        counter += 1
    for mountain in arboretum.mountains:
        print(f'{counter + 1}. Mountain [{mountain.id}]')
        counter += 1

    choice = int(input("> "))

    biome_list[choice - 1].add_animal(animal)

    print(
        f"{animal.species} [{animal.id}] was added to {biome_list[choice - 1].name} [{biome_list[choice - 1].id}]")

    input('Press enter to continue...')
