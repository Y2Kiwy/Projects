class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:

        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100 * (1 / age), 3)

        self.fence: str = None


    def get_area(self) -> float:
        '''
        Calculate the area of the animal.

        Returns:
            - animal_area (float): The area of the animal.
        '''
        return float(self.width * self.height)



class Fence:

    def __init__(self, area: float, temperature: float, habitat: str) -> None:

        self.area: float = area
        self.temperature: int = temperature
        self.habitat: str = habitat

        self.animals: list[Animal] = []


    def get_areas(self) -> tuple[float, float]:
        '''
        Calculate the occupied and free areas in the fence.

        Returns:
            - tuple[float, float]: A tuple containing the occupied area and the free area in the fence.
        '''
        occupied_area: float = 0

        # Calculate the total occupied area by summing up the areas of all animals in the fence
        for animal in self.animals:
            occupied_area += animal.get_area()

        # Calculate the free area by subtracting the occupied area from the total area of the fence
        free_area: float = self.area - occupied_area

        return (float(occupied_area), float(free_area))



class ZooKeeper:

    def __init__(self, name: str, surname: str, id: int) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: int = id


    
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        Add a specific animal to a specific fence.

        Args:
            - animal (Animal): The Animal instance to add into the fence.
            - fence (Fence): The Fence instance where to add the animal instance.

        Returns:
            - None
        '''

        if animal.preferred_habitat != fence.habitat:
            raise RuntimeError(f"'{animal.name}' cannot live in fence habitat: '{fence.habitat}'")
        
        elif animal.get_area() > fence.get_areas()[1]:
            raise RuntimeError(f"'{animal.name}' with area of '{animal.get_area():,.2f}' does not fit in fence free area: '{fence.get_areas()[1]:,.2f}'")
        
        else:
            try:
                fence.animals.append(animal)
                animal.fence = fence

            except Exception as e:
                print(f"Something went wrong while adding '{animal.name}' to fence -> {e}")


    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        Remove a specific animal from the animals list in the fence.

        Args:
            - animal (Animal): The Animal instance to remove from the animals list.
            - fence (Fence): The Fence instance where to remove the animal instance.

        Returns:
            - None
        '''

        if not animal in fence.animals:
            raise RuntimeError(f"'{animal.name}' not found in fence")
        
        else:
            try:
                fence.animals.remove(animal)
                animal.fence = None

            except Exception as e:
                print(f"Something went wrong while deleting '{animal.name}' from fence -> {e}")

    
    def feed(self, animal: Animal) -> None:
        '''
        Feed an animal if possible.

        Args:
            - animal (Animal): The Animal instance to feed.

        Returns:
            - None
        '''
        
        base_animal_area: float = animal.get_area()
        feeded_animal_area: float = (animal.width + (animal.width * 0.02)) * (animal.height + (animal.height * 0.02))
        area_increment: float = feeded_animal_area - base_animal_area

        if area_increment > animal.fence.get_areas()[1]:
            raise RuntimeError(f"Cannot feed {animal.name} (feeded area increment: {area_increment:,.2f}), it would exceed the remaining available area (free area: {animal.fence.get_areas()[1]:,.2f})")
        
        else:
            try:
                animal.width += animal.width * 0.02
                animal.height += animal.height * 0.02
                animal.health += round(animal.health * 0.01, 3)

            except Exception as e:
                print(f"Something went wrong while feeding '{animal.name}' -> {e}")


    def clean(self, fence: Fence) -> float:
        '''
        Calculate the cleanliness level of the fence.

        Args:
            - fence (Fence): The Fence instance to clean.

        Returns:
            - float: The cleanliness level of the fence.
        '''

        if fence.get_areas()[1] == 0:
            return 0
        else:
            try:
                return float(fence.get_areas()[0] / fence.get_areas()[1])
            
            except Exception as e:
                print(f"Something went wrong while cleaning fence -> {e}")



class Zoo:
    def __init__(self, name: str, address: str, zookeepers: list[ZooKeeper], fences: list[Fence]) -> None:
        self.name: str = name
        self.address: str = address
        self.guardians = zookeepers
        self.fences = fences

    def describe_zoo(self):
        '''
        Print the description of the zoo, including guardians and fences with animals.

        Returns:
            - None
        '''
        print("\nGuardians:\n")
        for guardian in self.guardians:
            print(f"ZooKeeper(name={guardian.name}, surname={guardian.surname}, id={guardian.id})\n")
        print("Fences:\n")
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("\nwith animals:\n")
            if fence.animals:
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            else:
                print("No animals in this fence.")
            print("\n" + "#" * 30 + "\n")
