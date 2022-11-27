from colors import *

class Unit:
    _hp = 0
    _arm = 0
    _dmg = 0
    _rng = 0
    _ap = 0
    _locX = 0
    _locY = 0
    _cost = 0
    _view = ''

    def __init__(self, x, y):
        self._locX = x
        self._locY = y

    def getView(self):
        return self._view

    def LocX(self):
        return self._locX
    
    def LocY(self):
        return self._locY

    def getCost(self):
        return self._cost

    def getDmg(self):
        return self._dmg

    def getAp(self):
        return self._ap

    def HP(self):
        return self._hp

    def Arm(self):
        return self._arm

    def getRange(self):
        return self._rng

    def heal(self, n):
        self._hp = self._hp + n

    def showUnitStatus(self):
        print("<============Статус юнита============>")
        print("HP: {}".format(self._hp))
        print("Броня: {}".format(self._arm))
        print("Урон: {}".format(self._dmg))
        print("Радиус атаки: {}".format(self._rng))
        print("Очки действия: {}".format(self._ap))
        print("<====================================>")

    def move(self, x, y, av):
        if (self._ap >= 2 * av):
            self._ap = self._ap - (2 * av)
            self._locX = x
            self._locY = y
        else:
            print("Недостаточно очков действия.")

    def attack(self, u, d, r, l):
        if self._ap >= 6:
            for i in range(1, u + 1):
                print("u{} - Вверх {}".format(i, i))
            for i in range(1, d + 1):
                print("d{} - Вниз {}".format(i, i))
            for i in range(1, r + 1):
                print("r{} - Вправо {}".format(i, i))
            for i in range(1, l + 1):
                print("l{} - Влево {}".format(i, i))
            direction = input("Выберите направление атаки: ")
            self._ap = self._ap - 6
            return "{}-{}".format(direction, self._dmg)
        else:
            print("<!>")
            print("Недостаточно очков действия.")
            print("<!>")
            return False

    def getDmgFromEnemy(self, dmg):
        if self._arm >= dmg / 2:
            self._arm = self._arm - dmg / 2
            self._hp = self._hp - dmg / 2
        elif self._arm < dmg / 2 and self._arm > 0:
            self._hp = self._hp - (dmg - self._arm)
            self._arm = 0
        else:
            self._hp = self._hp - dmg

    def reset(self):
        self._ap = 10
        
class MeleeWaririor(Unit):
    _rng = 1

class Knight(MeleeWaririor):
    _hp = 10
    _arm = 10
    _dmg = 10
    _ap = 10
    _cost = 10
    _view = Violet('K')

class Paladin(MeleeWaririor):
    _hp = 20
    _arm = 15
    _dmg = 15
    _ap = 10
    _cost = 20
    _view = Violet('P')

class RangedWarrior(Unit):
    _rng = 3

class Archer(RangedWarrior):
    _hp = 10
    _arm = 5
    _dmg = 5
    _ap = 10
    _cost = 10
    _view = Violet('A')

class Mage(RangedWarrior):
    _hp = 10
    _arm = 0
    _dmg = 10
    _ap = 10
    _cost = 20
    _view = Violet('M')

class SpecialWarrior(Unit):
    _rng = 2

class Dragonborn(SpecialWarrior):
    _hp = 30
    _arm = 20
    _dmg = 20
    _ap = 10
    _cost = 30
    _view = Violet('D')

    def move(self, x, y, av):
        if self._ap >= 2:
            self._ap = self._ap - 2
            self._locX = x
            self._locY = y
        else:
            print("Недостаточно очков действия.")

class Lord(SpecialWarrior):
    _hp = 50
    _arm = 30
    _dmg = 30
    _ap = 10
    _cost = 50
    _view = Violet('L')