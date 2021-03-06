from .biome import Biome

class Grassland(Biome):

    def __init__(self):
        Biome.__init__(self, "Grassland", 22, 15, {"little Rainfall", "No Shade"})
        

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.species_type == "bird":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-bird animals to a grassland")

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == "full" and plant.insecticide_resistance.lower() == "high" or plant.sunlight.lower() == "partial" and plant.insecticide_resitance.lower() == "medium":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add this plant/tree to this forest")