class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:

        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100 * (1 / age), 3)


    def get_area(self) -> float:
        return float(self.width * self.height)



class Fence:

    def __init__(self, area: float, temperature: float, habitat: str) -> None:

        self.area: float = area
        self.temperature: int = temperature
        self.habitat: str = habitat

        self.animals: list[Animal] = []


    def get_areas(self) -> tuple[float, float]:

        occupied_area: float = 0

        for animal in self.animals:
            occupied_area += animal.get_area()

        free_area: float = self.area - occupied_area

        return (float(occupied_area), float(free_area))



class ZooKeeper:

    def __init__(self, name: str, surname: str, id: int) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: int = id


    def add_animal(self, animal: Animal, fence: Fence) -> None:

        if animal.preferred_habitat != fence.habitat:
            raise RuntimeError(f"'{animal.name}' cannot live in fence habitat: '{fence.habitat}'")
        
        elif animal.get_area() > fence.get_areas()[1]:
            raise RuntimeError(f"'{animal.name}' with area of '{animal.get_area():,.2f}' do not fit in fence free area: '{fence.get_areas()[1]:,.2f}'")
        
        else:
            try:
                fence.animals.append(animal)

            except Exception as e:
                print(f"Something went wrong while adding '{animal.name}' to fence -> {e}")


    def remove_animal(self, animal: Animal, fence: Fence) -> None:

        if not animal in fence.animals:
            raise RuntimeError(f"'{animal.name}' do not found in fence")
        
        else:
            try:
                fence.animals.remove(animal)

            except Exception as e:
                print(f"Something went wrong while deleting '{animal.name}' from fence -> {e}")

    
    def feed(self, animal: Animal, fence: Fence) -> None:
        
        base_anima_area: float = animal.get_area()
        feeded_animal_area: float = (animal.width + (animal.width * 0.02)) * (animal.height + (animal.height * 0.02))
        area_incremment: float = feeded_animal_area - base_anima_area

        if area_incremment > fence.get_areas()[1]:
            raise RuntimeError(f"Cannot feed {animal.name} (feeded area increment: {area_incremment:,.2f}) it would exceed the remaining available area (free area: {fence.get_areas()[1]:,.2f})")
        
        else:
            try:
                animal.width *= animal.width * 0.02
                animal.height *= animal.height * 0.02

            except Exception as e:
                print(f"Something went wrong while feeding '{animal.name}' -> {e}")


    def clean(self, fence: Fence) -> float:

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
        print("\nGuardians:\n")
        for guardian in self.guardians:
            print(f"ZooKeeper(name={guardian.name}, surname={guardian.surname}, id={guardian.id})")
        print("\nFences:\n")
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("\nwith animals:\n")
            if fence.animals:
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            else:
                print("No animals in this fence.")
            print("\n" + "#" * 30 + "\n")
