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

# Tests ----------------------------------------------------------------------

try:
    a1: Animal = Animal(name="Leone", species="Felino", age=7, height=30, width=50, preferred_habitat="Savana")  # It works
except Exception as e:
    print("Error creating animal a1:", e)

try:
    a2: Animal = Animal(name="Squalo", species="Pesce", age=35, height=30, width=100, preferred_habitat="Water") # It works
except Exception as e:
    print("Error creating animal a2:", e)

try:
    f1: Fence = Fence(area=2000, temperature=24, habitat="Savana")                                               # It works
except Exception as e:
    print("Error creating fence f1:", e)

try:
    f2: Fence = Fence(area=5890, temperature=18, habitat="Water")                                                # It works
except Exception as e:
    print("Error creating fence f2:", e)

try:
    z1: ZooKeeper = ZooKeeper(name="Simone", surname="Antonelli", id=8113)                                       # It works
except Exception as e:
    print("Error creating ZooKeeper z1:", e)

try:
    z1.add_animal(a1, f1)                                                                                        # It works
    print(f"Added {a1.name} to fence f1")
except Exception as e:
    print("Error adding animal a1 to fence f1:", e)

try:
    z1.feed(a1, f1)                                                                                              # It works
    print(f"Feeded {a1.name}") 
except Exception as e:
    print("Error feeding animal a1:", e)

try:
    f1_clean_time: float = z1.clean(f1)                                                                          # It works
    print(f"Cleaned fence f1 with time of: {f1_clean_time:,.2f}")
except Exception as e:
    print("Error cleaning fence f1:", e)

try:
    z1.remove_animal(a1, f1)                                                                                     # It works
    print(f"Removed {a1.name} to fence f1")
except Exception as e:
    print("Error removing animal a1 from fence f1:", e)

try:
    z1.add_animal(a2, f2)                                                                                        # It works
    print(f"Added {a2.name} to fence f2")
except Exception as e:
    print("Error adding animal a2 to fence f2:", e)

try:
    f2_clean_time: float = z1.clean(f2)                                                                          # It works
    print(f"Cleaned fence f2 with time of: {f2_clean_time:,.2f}")
except Exception as e:
    print("Error cleaning fence f2:", e)

