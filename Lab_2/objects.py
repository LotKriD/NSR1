from pytest import Class
from colors import *
from units import *

class Object:
    _x = 0
    _y = 0
    _view = ""
    _type = ""

    def LocX(self):
        return self._x

    def LocY(self):
        return self._y

    def getView(self):
        return self._view

    def getType(self):
        return self._type

class Healh(Object):
    _view = White("+")
    _type = 'H'

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def heal(self, u):
        u.heal(10)

class Gold(Object):
    _view = White("$")
    _type = 'G'

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def increaseBudget(self, b):
        b.budget(20)

class Castle(Object):
    _view = White("№")
    __owner = False
    _type = 'C'

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getOwner(self):
        return self.__owner

    def setOwner(self):
        self.__owner = True
        self._view = Violet("№")

class Altar(Object):
    _view = White("!")
    __owner = False
    _type = 'Altar'

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getOwner(self):
        return self.__owner

    def setOwner(self):
        self.__owner = True
        self._view = Violet("!")

class Base:

    __hp = 50
    __budget = 100
    __ap = 1
    __view = Violet('#')
    __knights = 0
    __paladins = 0
    __archers = 0
    __mages = 0
    __dragonborns = 0
    __lords = 0
    __x = 1
    __y = 1

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getView(self):
        return self.__view

    def LocX(self):
        return self.__x

    def LocY(self):
        return self.__y

    def HP(self):
        return self.__hp

    def Budget(self):
        return self.__budget

    def budget(self, gold):
        self.__budget = self.__budget + gold

    def showBaseStatus(self):
        print("<============Статус базы============>")
        print("HP: {}".format(self.__hp))
        print("Бюджет: {}".format(self.__budget))
        print("Юниты: ")
        print("Рыцари (K): {}".format(self.__knights))
        print("Паладины (P): {}".format(self.__paladins))
        print("Лучники (A): {}".format(self.__archers))       
        print("Маги (M): {}".format(self.__mages))
        print("Драконорожденые (D): {}".format(self.__dragonborns))
        print("Лорды (L): {}".format(self.__lords))
        print("<===================================>")
    
    def createUnit(self, objs):
        if self.__ap <= 0:
            print("<!>")
            print("Недостаточно очков действий.")
            print("<!")
            return False
        else:
            print("k. Рыцарь")
            print("p. Паладин")
            print("a. Лучник")
            print("m. Маг")
            if objs[3].getOwner() == True:
                print("d. Драконорожденный")
            if objs[2].getOwner() == True:
                print("l. Лорд")
            i = input("Выберите юнита: ")
            if i == 'k':
                unit = Knight(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__knights = self.__knights + 1
                    self.__ap = self.__ap - 1
                    return unit
            elif i == 'p':
                unit = Paladin(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__paladins = self.__paladins + 1
                    self.__ap = self.__ap - 1
                    return unit
            elif i == 'a':
                unit = Archer(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__archers = self.__archers + 1
                    self.__ap = self.__ap - 1
                    return unit        
            elif i == 'm':
                unit = Mage(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__mages = self.__mages + 1
                    self.__ap = self.__ap - 1
                    return unit
            elif i == 'd':
                unit = Dragonborn(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__dragonborns = self.__dragonborns + 1
                    self.__ap = self.__ap - 1
                    return unit
            elif i == 'l':
                unit = Lord(self.__x, self.__y)
                if self.__checkUnit(unit) == True:
                    self.__budget = self.__budget - unit.getCost()
                    self.__lords = self.__lords + 1
                    self.__ap = self.__ap - 1
                    return unit
            return False

    def __checkUnit(self, unit):
        if unit.getCost() > self.__budget:
                print("<!>")
                print("Невозможно создать: ")
                print("Бюджет - {}; Цена юнита - {}".format(self.__budget, unit.getCost()))
                print("<!>")
                return False
        else:
            return True

    def getDmg(self, dmg):
        self.__hp = self.__hp - dmg

    def unitKilled(self, cost, view):
        self.__budget = self.__budget + cost
        if view == Violet('K'):
            self.__knight= self.__knight - 1
        elif view == Violet('P'):
            self.__paladins = self.__paladins - 1
        elif view == Violet('A'):
            self.__archers = self.__archers - 1
        elif view == Violet('M'):
            self.__mages = self.__mages - 1
        elif view == Violet('D'):
            self.__dragonborns = self.__dragonborns- 1
        elif view == Violet('L'):
            self.__lords = self.__lords - 1

    def reset(self):
        self.__ap = 1

