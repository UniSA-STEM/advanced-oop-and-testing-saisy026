"""
File: test.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird
from zookeeper import Zookeeper

def test_enclosure_compatibility():
    enc = Enclosure("SAV1", 100, "savannah", 3)
    lion = Mammal("Leo", "Lion", 4, "meat", "savannah")
    parrot = Bird("Tweety", "Canary", 2, "seeds", "aviary")

    assert enc.can_add_animal(lion) is True
    assert enc.can_add_animal(parrot) is False

def test_zookeeper_role_restriction():
    zk = Zookeeper("Alice", "ZK1")
    lion = Mammal("Leo", "Lion", 3, "meat", "savannah")

    with pytest.raises(ValueError):
        zk.assign_to_animal(lion)

