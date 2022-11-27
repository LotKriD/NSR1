from map import *
import ctypes
from colors import *
            
def createBase(x, y):
    __bases.append(Base(x, y))

def baseStatus():
    __bases[0].showBaseStatus()

def createUnit():
    objs = map.getObjects()
    unit = __bases[0].createUnit(objs)
    if unit != False:
        __units.append(unit)

def unitProgress():
    for u in __units:
        print("Ход юнита {} ({} , {})".format(u.getView(), u.LocX(), u.LocY()))
        print(White("Перемещение [w,a,s,d]"))
        print("k - атака")
        ch = ''
        while(ch != 'n'):
            print(White("i. Статус юнита."))
            print("n. Следующий юнит.")
            ch = input("Введите действие: ")

            if ch == 'i':
                u.showUnitStatus()

            elif ch == 'k':
                up = __checkUp(u.getRange(), u.LocX(), u.LocY())
                down = __checkDown(u.getRange(), u.LocX(), u.LocY())
                right = __checkRight(u.getRange(), u.LocX(), u.LocY())
                left = __checkLeft(u.getRange(), u.LocX(), u.LocY())

                temp = u.attack(up, down, right, left)
                if temp != False:
                    atk = temp.split('-')
                    if atk[0][0] == 'u':
                        __checkAttack(u, 'x', -int(atk[0][1]), int(atk[1]))
                    elif atk[0][0] == 'd':
                        __checkAttack(u, 'x', int(atk[0][1]), int(atk[1]))
                    elif atk[0][0] == 'r':
                        __checkAttack(u, 'y', int(atk[0][1]), int(atk[1]))
                    elif atk[0][0] == 'l':
                        __checkAttack(u, 'y', -int(atk[0][1]), int(atk[1]))
                    ShowMap()
                            
            elif ch == 'w' or ch == 'a' or ch == 's' or ch == 'd':
                __moveUnit(u, ch)
                ShowMap()

def __checkUp(r, x, y):
    mapTerrain = map.getTerrain()
    for i in range(1, r + 1):
        if mapTerrain[int(x) - i][int(y)].getAvailability() <= 0:
            return i - 1
    return i

def __checkDown( r, x, y):
    mapTerrain = map.getTerrain()
    for i in range(1, r + 1):
        if mapTerrain[int(x) + i][int(y)].getAvailability() <= 0:
            return i - 1
    return i

def __checkRight(r, x, y):
    mapTerrain = map.getTerrain()
    for i in range(1, r + 1):
        if mapTerrain[int(x)][int(y) + i].getAvailability() <= 0:
            return i - 1
    return i

def __checkLeft(r, x, y):
    mapTerrain = map.getTerrain()
    for i in range(1, r + 1):
        if mapTerrain[int(x)][int(y) - i].getAvailability() <= 0:
            return i - 1
    return i

def __checkAttack(u, dir, n, dmg):
    if dir == 'x':
        k = -1
        for i in __bases:
            k = k + 1
            if i.LocX() == int(u.LocX()) + n and i.LocY() == u.LocY():
                i.getDmg(dmg)
                if i.HP() <= 0:                   
                    __bases.pop(k)
                    k = k - 1

        k = -1
        for i in __units:
            k = k + 1 
            if i.LocX() == int(u.LocX()) + n and i.LocY() == u.LocY():
                i.getDmgFromEnemy(dmg)
                if i.HP() <= 0:
                    __bases[0].unitKilled(i.getCost(), i.getView())
                    __units.pop(k)
                    k = k - 1
    else:
        k = -1
        for i in __bases:
            k = k + 1
            if int(i.LocX()) == int(u.LocX()) and int(i.LocY()) == int(u.LocY()) + n:
                i.getDmg(dmg)
                if i.HP() <= 0:
                    __bases.pop(k)
                    k = k - 1

        k = -1
        for i in __units:
            k = k + 1
            if i.LocX() == u.LocX() and i.LocY() == int(u.LocY()) + n:
                i.getDmgFromEnemy(dmg)
                if i.HP() <= 0:
                    __bases[0].unitKilled(i.getCost(), i.getView())
                    __units.pop(k)
                    k = k - 1

def __moveUnit(unit, direction):
    mapTerrain = map.getTerrain()
    if unit.getView() != Violet('D'):
        if direction == 'w' and mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability() > 0:
            unit.move(int(unit.LocX()) - 1, unit.LocY(), mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability())
        elif direction == 's' and mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability() > 0:
            unit.move(int(unit.LocX()) + 1, unit.LocY(), mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability())
        elif direction == 'a' and mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability() > 0:
            unit.move(unit.LocX(), int(unit.LocY()) - 1, mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability())
        elif direction == 'd' and mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability() > 0:
            unit.move(unit.LocX(), int(unit.LocY()) + 1, mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability())
    else:
        if direction == 'w' and mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability() >= 0:
            unit.move(int(unit.LocX()) - 1, unit.LocY(), mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability())
        elif direction == 's' and mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability() >= 0:
            unit.move(int(unit.LocX()) + 1, unit.LocY(), mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability())
        elif direction == 'a' and mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability() >= 0:
            unit.move(unit.LocX(), int(unit.LocY()) - 1, mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability())
        elif direction == 'd' and mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability() >= 0:
            unit.move(unit.LocX(), int(unit.LocY()) + 1, mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability())
    
    objs = map.getObjects()
    for o in objs:
        if o.LocX() == unit.LocX() and o.LocY() == unit.LocY():
            if o.getType() == 'H':
                o.heal(unit)
            elif o.getType() == 'G':
                o.increaseBudget(__bases[0])
            elif o.getType() == 'C':
                o.setOwner()
            elif o.getType() == 'Altar':
                o.setOwner()
        
def reset():
    for b in __bases:
        b.reset()

    for u in __units:
        u.reset()

def ShowMap():
    map.show(__bases, __units)

__bases = []
__units =  []

if __name__ == "__main__":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    print(White("Генерация карты"))
    l = input("Введите размер карты:")

    if l == 'd':
        map = Map(10, 10)
    else:
        map = Map(int(l), int(l))
    ShowMap()
    print(White("Создание базы"))
    y = input("Введите координату y: ")
    x = input("Введите координату x: ")
    createBase(x, y)
    while(True):
        try:
            print("<==========================>")
            ShowMap()

            print(White("<==========================>"))
            print("1. Статус базы.")
            print("2. Создать юнита.")
            print("3. Следующий юнит.")
            print("0. Закончить ход.")
            n = int(input("Выберите действие: "))
        
            if n == 1:
                baseStatus()
            elif n == 2:
                createUnit()
            elif n == 3:
                unitProgress()
            elif n == 0:
                print("Конец хода.")
                reset()
        except:
            print("<!>")
            print("Ошибка. Неверный ввод.")
            print("<!>")