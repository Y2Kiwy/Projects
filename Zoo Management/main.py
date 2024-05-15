from lib import * 

# Tests ----------------------------------------------------------------------

try:
    a1: Animal = Animal(name="Leone", species="Felino", age=7, height=30, width=50, preferred_habitat="Savana")
except Exception as e:
    print("Error creating animal a1:", e)

try:
    a2: Animal = Animal(name="Squalo", species="Pesce", age=35, height=30, width=100, preferred_habitat="Water")
except Exception as e:
    print("Error creating animal a2:", e)

try:
    f1: Fence = Fence(area=1560, temperature=24, habitat="Savana")
except Exception as e:
    print("Error creating fence f1:", e)

try:
    f2: Fence = Fence(area=5890, temperature=18, habitat="Water")
except Exception as e:
    print("Error creating fence f2:", e)

try:
    z1: ZooKeeper = ZooKeeper(name="Simone", surname="Antonelli", id=8113)
except Exception as e:
    print("Error creating ZooKeeper z1:", e)

try:
    z1.add_animal(a1, f1)
    print(f"Added {a1.name} to fence f1")
except Exception as e:
    print("Error adding animal a1 to fence f1:", e)

try:
    z1.feed(a1)
    print(f"Feeded {a1.name}") 
except Exception as e:
    print("Error feeding animal a1:", e)

try:
    f1_clean_time: float = z1.clean(f1)
    print(f"Cleaned fence f1 with time of: {f1_clean_time:,.2f}")
except Exception as e:
    print("Error cleaning fence f1:", e)

try:
    z1.remove_animal(a1, f1)
    print(f"Removed {a1.name} to fence f1")
except Exception as e:
    print("Error removing animal a1 from fence f1:", e)

try:
    z1.add_animal(a2, f2)
    print(f"Added {a2.name} to fence f2")
except Exception as e:
    print("Error adding animal a2 to fence f2:", e)

try:
    z1.feed(a2)
    print(f"Feeded {a2.name}") 
except Exception as e:
    print("Error feeding animal a1:", e)

try:
    f2_clean_time: float = z1.clean(f2)
    print(f"Cleaned fence f2 with time of: {f2_clean_time:,.2f}")
except Exception as e:
    print("Error cleaning fence f2:", e)

try:
    zoo1: Zoo = Zoo(name="Bioparco di Roma", address="V.le del Giardino Zoologico", zookeepers=[z1], fences=[f1, f2])
    zoo1.describe_zoo()
except Exception as e:
    print("Error cleaning fence f2:", e)