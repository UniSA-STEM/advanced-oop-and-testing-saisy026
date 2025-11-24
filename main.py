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

