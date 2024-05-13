class Zoo:

    def __init__(self, name: str, address: str) -> None:

        self.name = name
        self.address = address



class Animal:

    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: str) -> None:

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: list[str] = preferred_habitat

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
        
        elif fence.habitat in animal.preferred_habitat:
            raise RuntimeError(f"Wrong fence habitat ({fence.habitat}) for animal {animal.name} (habitats: {animal.preferred_habitat})")
        
        else:
            return bool


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