class Animal:

    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: str) -> None:

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat

        self.health: int = round(100 * (1 / age), 3)

    def get_area(self, feed: bool = False) -> float:
        '''
        Calculate the are aof the animal.
        Args:
            - None
        Return:
            - animal_area (float): The area of the animal.
        
        '''
        if not feed:
            return (self.width * self.height)
        else:
            return(self.width + (self.width * 0.02)) * (self.height + (self.height * 0.02))



class Fence:

    def __init__(self, area: float, temperature: float, habitat: str) -> None:

        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat

        self.animals: list[Animal] = []

    def get_free_area(self) -> float:
        '''
        Calculate the remaining free area in the fence.

        Args:
            - None
        
        Return:
            - free_area (float): The remaining free area in the fence.
        '''
        
        occupied_area: float = 0

        for animal in self.animals:
            occupied_area += animal.get_area()

        free_area: float = self.area - occupied_area

        return free_area
    
    def get_occupied_area(self) -> float:
        '''
        Calculate the occupied area in the fence.

        Args:
            - None
        
        Return:
            - occupied_area (float): The occupied area in the fence.
        '''
        
        occupied_area: float = 0

        for animal in self.animals:
            occupied_area += animal.get_area()

        return occupied_area



class ZooKeeper:

    def __init__(self, name: str, surname: str, id: int) -> None:

        self.name: str = name
        self.surname: str = surname
        self.id: int = id

    def add_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        Add specific animal to specific fence
        
        Args:
            - animal (Animal): Animal instance to add into the fence
            - fence (Fence): Fence instance where to add the animal instance

        Return
            - None
        '''

        valid_trasnfer: bool = self.validate_add(animal, fence)

        if valid_trasnfer:
            fence.animals.append(animal)
    def validate_add(self, animal: Animal, fence: Fence) -> bool:
        '''
        Compare the available area in the fence and its habitat to the given animal.

        Args:
            - animal (Animal): Animal instance to add into the fence.
            - fence (Fence): Fence instance where to add the animal.

        Return:
            - None
        '''

        animal_area: float = animal.width * animal.height

        if animal_area > fence.get_free_area():
            raise RuntimeError(f"Insufficent area ({fence.get_free_area()}) in the fence to add animal {animal.name} (area: {animal.width * animal.height})")
        
        elif fence.habitat.lower() == animal.preferred_habitat.lower():
            raise RuntimeError(f"Wrong fence habitat ({fence.habitat}) for animal {animal.name} (habitat: {animal.preferred_habitat})")
        
        else:
            return True


    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        Remove specific animal from animals list in the fence.

        Args:
            - animal (Animal): the animal instance to remove from the animals list
            - fence (Fenec): The fence instance where to remove the animal instance
        '''
        fence.animals.remove(animal)


    def feed(self, animal: Animal, fence: Fence) -> None:
        '''
        Feed animal if possible.

        Args:
            - animal (Animal): The animal to feed.
            - fence (Fence): The fence where the animal is located.

        Return:
            - None
        '''

        valid_feed: bool = self.validate_feed(animal, fence)

        if not valid_feed:
            raise RuntimeError(f"Cannot feed animal {animal.name} (area increment: {animal.get_area(feed = True)}), no more space left in the fence ({fence.get_free_area()})")
        
        else:
            animal.width += animal.width * 0.02
            animal.height += animal.height * 0.02
            animal.health += 1
    def validate_feed(self, animal: Animal, fence: Fence) -> bool:
        '''
        Check if it is possible to feed animal due to area increment.

        Args: 
            - animal (Animal): Animal instance to feed.
            - fence (Fence): Fence instance where the animal is located.

        Return:
            - valid (bool): True if feed is valid, False if feed is not valid.
        '''

        free_fence_area: float = fence.get_free_area()

        base_animal_area: float = animal.get_area()

        feeded_animal_area: float = animal.get_area(feed = True)

        if feeded_animal_area - base_animal_area > free_fence_area:
            return False
        
        else:
            return True
        
    
    def  clean(self, fence: Fence) -> float:
        '''
        Cleans the fence and returns the cleanliness ratio.

        Args:
            - fence (Fence): The fence to be cleaned.

        Returns:
            - cleanliness_ratio (float): The ratio of occupied area to free area in the fence.
        '''
        if fence.area - fence.get_free_area() == 0:
            return float(fence.area)
        else:
            return float(fence.get_occupied_area() / fence.get_free_area())



class Zoo:

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.zookeepers = []
        self.fences = []

    def describe_zoo(self) -> None:
        print("Guardians:\n")
        for keeper in self.zookeepers:
            print(f"\tZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})\n")

        print("Fences:\n")
        for fence in self.fences:
            print(f"\tFence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            if fence.animals:
                print("\nwith animals:\n")
                for animal in fence.animals:
                    print(f"\tAnimal(name={animal.name}, species={animal.species}, age={animal.age})\n")
            else:
                print("No animals in this fence.\n")
            print("\t##############################\n")



# Creazione degli animali
scoiattolo = Animal("Scoiattolo", "Blabla", 25, 10, 5, "Bosco")
lupo = Animal("Lupo", "Lupus", 14, 15, 8, "Forestale")

# Creazione dei recinti
recinto1 = Fence(100, 25, "Continentale")
recinto2 = Fence(150, 20, "Bosco")

# Creazione del guardiano dello zoo
guardiano = ZooKeeper("Lorenzo", "Maggi", 1234)

# Aggiunta degli animali ai recinti
guardiano.add_animal(scoiattolo, recinto1)
guardiano.add_animal(lupo, recinto2)

# Creazione dello zoo
zoo = Zoo("Zoo", "Indirizzo")
zoo.zookeepers.append(guardiano)
zoo.fences.extend([recinto1, recinto2])

# Tentativo di nutrire un animale in un recinto senza spazio
try:
    guardiano.feed(scoiattolo, recinto1)
except RuntimeError as e:
    print(f"Errore: {e}")

# Test della funzione describe_zoo dopo l'errore
zoo.describe_zoo()