def createBase(self, x, y):
        self.__bases.append(Base(x, y))
        self._baseLocX = x
        self._baseLocY = y

    def baseStatus(self):
        self.__bases[0].showBaseStatus()

    def createUnit(self):
        unit = self.__bases[0].createUnit()
        if unit != False:
            self.__units.append(unit)

    def unitProgress(self):
        for u in self.__units:
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
                    up = self.__checkUp(u.getRange(), u.LocX(), u.LocY())
                    down = self.__checkDown(u.getRange(), u.LocX(), u.LocY())
                    right = self.__checkRight(u.getRange(), u.LocX(), u.LocY())
                    left = self.__checkLeft(u.getRange(), u.LocX(), u.LocY())
                    temp = u.attack(up, down, right, left)
                    if temp != False:
                        atk = temp.split('-')
                        print(atk[0][1])
                        print(atk[1])
                        if atk[0][0] == 'u':
                            self.__checkAttack(u, 'x', -int(atk[0][1]), int(atk[1]))
                        elif atk[0][0] == 'd':
                            self.__checkAttack(u, 'x', int(atk[0][1]), int(atk[1]))
                        elif atk[0][0] == 'r':
                            self.__checkAttack(u, 'y', int(atk[0][1]), int(atk[1]))
                        elif atk[0][0] == 'l':
                            self.__checkAttack(u, 'y', -int(atk[0][1]), int(atk[1]))
                    self.show()
                            
                elif ch == 'w' or ch == 'a' or ch == 's' or ch == 'd':
                    self.__moveUnit(u, ch)
                    self.show()

    def __checkUp(self, r, x, y):
        for i in range(1, r + 1):
            if self.__mapTerrain[int(x) - i][int(y)].getAvailability() <= 0:
                return i - 1
        return i

    def __checkDown(self, r, x, y):
        for i in range(1, r + 1):
            if self.__mapTerrain[int(x) + i][int(y)].getAvailability() <= 0:
                return i - 1
        return i

    def __checkRight(self, r, x, y):
        for i in range(1, r + 1):
            if self.__mapTerrain[int(x)][int(y) + i].getAvailability() <= 0:
                return i - 1
        return i

    def __checkLeft(self, r, x, y):
        for i in range(1, r + 1):
            if self.__mapTerrain[int(x)][int(y) - i].getAvailability() <= 0:
                return i - 1
        return i

    def __checkAttack(self, u, dir, n, dmg):
        if dir == 'x':
            k = -1
            for i in self.__bases:
                k = k + 1
                if i.LocX() == int(u.LocX()) + n and i.LocY() == u.LocY():
                    i.getDmg(dmg)
                    if i.HP() <= 0:                   
                        self.__bases.pop(k)
                        k = k - 1

            k = -1
            for i in self.__units:
                k = k + 1 
                if i.LocX() == int(u.LocX()) + n and i.LocY() == u.LocY():
                    i.getDmgFromEnemy(dmg)
                    if i.HP() <= 0:
                        self.__bases[0].unitKilled(i.getCost(), i.getView())
                        self.__units.pop(k)
                        k = k - 1
        else:
            k = -1
            for i in self.__bases:
                k = k + 1
                if int(i.LocX()) == int(u.LocX()) and int(i.LocY()) == int(u.LocY()) + n:
                    i.getDmg(dmg)
                    if i.HP() <= 0:
                        self.__bases.pop(k)
                        k = k - 1

            k = -1
            for i in self.__units:
                k = k + 1
                if i.LocX() == u.LocX() and i.LocY() == int(u.LocY()) + n:
                    i.getDmgFromEnemy(dmg)
                    if i.HP() <= 0:
                        self.__bases[0].unitKilled(i.getCost(), i.getView())
                        self.__units.pop(k)
                        k = k - 1

    def __moveUnit(self, unit, direction):
        print(direction)
        if unit.getView() != Violet('D'):
            if direction == 'w' and self.__mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability() > 0:
                unit.move(int(unit.LocX()) - 1, unit.LocY(), self.__mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability())
            elif direction == 's' and self.__mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability() > 0:
                unit.move(int(unit.LocX()) + 1, unit.LocY(), self.__mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability())
            elif direction == 'a' and self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability() > 0:
                unit.move(unit.LocX(), int(unit.LocY()) - 1, self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability())
            elif direction == 'd' and self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability() > 0:
                unit.move(unit.LocX(), int(unit.LocY()) + 1, self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability())
        else:
            if direction == 'w' and self.__mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability() >= 0:
                unit.move(int(unit.LocX()) - 1, unit.LocY(), self.__mapTerrain[int(unit.LocX()) - 1][int(unit.LocY())].getAvailability())
            elif direction == 's' and self.__mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability() >= 0:
                unit.move(int(unit.LocX()) + 1, unit.LocY(), self.__mapTerrain[int(unit.LocX()) + 1][int(unit.LocY())].getAvailability())
            elif direction == 'a' and self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability() >= 0:
                unit.move(unit.LocX(), int(unit.LocY()) - 1, self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) - 1].getAvailability())
            elif direction == 'd' and self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability() >= 0:
                unit.move(unit.LocX(), int(unit.LocY()) + 1, self.__mapTerrain[int(unit.LocX())][int(unit.LocY()) + 1].getAvailability())
            
