"""
File: filename.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""


from datetime import date
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from zoo import Zoo

# =============================================================================
#                   SIMONE'S ZOO -  SYSTEM DEMO by ByteWise Consulting
# =============================================================================

print("=" * 70)
print("       WELCOME TO SIMONE'S ZOO MANAGEMENT SYSTEM")
print("=" * 70)
print()

# Create the zoo
zoo = Zoo()


# Create Enclosures

exhibit_enclosure = Enclosure("EXH-01", 1500, "exhibit", 10)
aviary_enclosure   = Enclosure("AVI-01", 500, "aviary", 30)
reptile_house      = Enclosure("REP-01", 300, "temperate", 15)

zoo.add_enclosure(exhibit_enclosure)
zoo.add_enclosure(aviary_enclosure)
zoo.add_enclosure(reptile_house)

print("3 enclosures created and registered.\n")


# Add Animals

leo     = Mammal("Leo", "Lion", 7, "carnivore", "exhibit")
simba     = Mammal("Simba", "Lion", 5, "carnivore", "exhibit")
coco    = Bird("Coco", "Cockatoo", 9, "seeds and fruit", "aviary")
python = Reptile("Python", "Snake", 10, "carnivore", "temperate")

zoo.add_animal(leo)
zoo.add_animal(simba)
zoo.add_animal(coco)
zoo.add_animal(python)

print("4 animals added to zoo records.\n")

# House Animals — Compatibility & Rules

print("Housing animals...")
print(exhibit_enclosure.add_animal(leo))
print(exhibit_enclosure.add_animal(simba))
print(aviary_enclosure.add_animal(coco))
print(reptile_house.add_animal(python))

# Try to put bird in exhibit_enclosure — should fail

try:
    exhibit_enclosure.add_animal(coco)
except ValueError as e:
    print(f"Blocked: {e}")

print("\nAll compatible animals successfully housed!\n")

# Hire Staff

saisy = Zookeeper("Saisy S", "ZK001")
nidhi  = Veterinarian("Dr. Yog Nidhi", "VET001")

# Assign responsibilities (role-restricted)

saisy.assign_to_enclosure(exhibit_enclosure)
saisy.assign_to_enclosure(reptile_house)
nidhi.assign_to_animal(leo)
nidhi.assign_to_animal(python)

# This would fail - just showing the protection works

try:
    saisy.assign_to_animal(leo)        # Zookeepers can't do this
except ValueError as e:
    print(f"Role protection working: {e}")

try:
    nidhi.assign_to_enclosure(aviary_enclosure)  # Vets can't do this
except ValueError as e:
    print(f"Role protection working: {e}")

zoo.add_staff(saisy)
zoo.add_staff(nidhi)

print(f"\nStaff assigned: {saisy.get_name()} (Zookeeper) & {nidhi.get_name()} (Vet)\n")


# Daily Operations

print("MORNING ROUTINE")
print(saisy.feed_animal(leo))
print(saisy.feed_animal(simba))
print(saisy.clean_enclosure(exhibit_enclosure))
print(saisy.clean_enclosure(reptile_house))
print(nidhi.perform_health_check(leo))
print()

# Health Issue Reported

print("HEALTH ALERT")
print(nidhi.record_health_issue(
    animal=leo,
    description="Limping on front left leg - possible ligament strain",
    severity=8,
    treatment="Cage rest, anti-biotics, daily monitoring"
))

print(f" Leo is now status: {leo.get_health_status()}")
print(" Leo cannot be moved while under treatment\n")

# Try to move a sick animal - should be blocked
try:
    exhibit_enclosure.remove_animal(leo)
    print("ERROR: Sick animal was moved!")
except ValueError as e:
    print(f"Correctly prevented: {e}\n")


#  End-of-Day Reports

print("=" * 70)
print("END OF DAY REPORTS")
print("=" * 70)

zoo.generate_enclosure_report()

print("\n" + "-" * 70)

zoo.generate_animal_report()

print("\n" + "-" * 70)
print("ANIMALS REQUIRING URGENT MEDICAL ATTENTION")
attention = zoo.get_animals_needing_attention()
if attention:
    for animal in attention:
        print(f"{animal.get_name()} ({animal.get_species()}) - Under Treatment")
else:
    print("All animals healthy!")

print("\n" + "=" * 70)
print("ZOO OPERATION COMPLETED!")
print("=" * 70)

