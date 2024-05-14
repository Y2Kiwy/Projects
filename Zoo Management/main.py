from lib2 import * 

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
    f1: Fence = Fence(area=1550, temperature=24, habitat="Savana")                                               # It works
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

try:
    zoo1: Zoo = Zoo(name="Bioparco di Roma", address="Piazzale del, V.le del Giardino Zoologico, 1, 00197 Roma RM", zookeepers=[z1], fences=[f1, f2])
    zoo1.describe_zoo()                                                                                          # It seems to works
except Exception as e:
    print("Error cleaning fence f2:", e)