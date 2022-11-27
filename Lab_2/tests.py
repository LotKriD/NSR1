import unittest
from objects import Base, Gold
from units import *

class baseTest(unittest.TestCase):
    
    def setUp(self):
        self.base = Base(5, 7)
        self.gold = Gold(3, 3)
    
    def test_locX(self):
        self.assertEquals(self.base.LocX(), 5)

    def test_locY(self):
        self.assertEquals(self.base.LocY(), 7)

    def test_HP(self):
        self.assertEquals(self.base.HP(), 50)

    def test_getDmg(self):
        self.base.getDmg(40)
        self.assertEquals(self.base.HP(), 10)

    def test_budget(self):
        self.gold.increaseBudget(self.base)
        self.assertEquals(self.base.Budget(), 120)

class unitsTest(unittest.TestCase):

    def setUp(self):
        self.a = Archer(3, 3)

    def test_move(self):
        self.a.move(3, 4, 2)
        self.assertEquals(self.a.LocX(), 3)
        self.assertEquals(self.a.LocY(), 4)
        self.assertEquals(self.a.getAp(), 6)

    def test_getDmg(self):
        self.a.getDmgFromEnemy(4)
        self.assertEquals(self.a.Arm(), 3)
        self.assertEquals(self.a.HP(), 8)

    def test_reset(self):
        self.a.reset()
        self.assertEquals(self.a.getAp(), 10)


if __name__ == "__main__":
    unittest.main()