class Zoo:

    def __init__(self, name: str, address: str) -> None:
        self._name = name
        self._address = address

class Animal:

    def __init__(self, name: str, species: str, age: float, height: float, width: float, preferred_habitat: list[str]) -> None:

        self._name = name
        self._species = species
        self._age = age
        self._height = height
        self.width = width
        self._preferred_habitat = preferred_habitat

        self._health = round(100 * (1 / age), 3)

class Fence:

    def __init__(self, area: float, temperature: float, habitat: str) -> None:

        self._area = area
        self._temperature = temperature
        self._habitat = habitat

        self._amials = []

class ZooKeeper:

    def __init__(self, name: str, surname: str, id: int) -> None:

        self._name = name
        self._surname = surname
        self._hid = id

    def add_animal(self, animal: Animal, fence: Fence) -> None:
        '''Add specific animal to specific fence
        
        Args:
        
            - animal (Animal): Animal instance to add into the fence
            - fence (Fence): Fence instance where to add the animal instance

        Return

            - None'''
        fence._animals.append(animal)

