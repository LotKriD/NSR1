import random
from units import *
from objects import *
from colors import *

terrainTypes = {-1: 'EndMap', 0: 'Water', 1: 'Mountain', 2:'Field'}

class Terrain:
    terrainType = None
    _view = ''
    _availability = 0

    def getView(self):
        return self._view

    def getAvailability(self):
        return self._availability

class EndMap(Terrain):
    _view = Red('X')
    _availability = -1

class Water(Terrain):
    _view = Blue('~')
    _availability = 2

class Mountain(Terrain):
    _view = Yellow('^')
    _availability = 0

class Field(Terrain):
    _view = Green('*')
    _availability = 1

class Map:    
    __mapTerrain = []
    __objects = []
    __x = 12
    __y = 12

    def __init__(self, x, y):
        self.__x = x + 2
        self.__y = y + 2
        self.__generateMaps()

    def createMap(self, x, y):
        self.__x = x + 2
        self.__y = y + 2
        self.__generateMaps()

    def __generateMaps(self):
        self.__generateTerrain()
        self.__generateObjects()
        #self.__generateMapUnits()

    def getTerrain(self):
        return self.__mapTerrain

    def getObjects(self):
        return self.__objects
    
    def __generateMapUnits(self):
        for i in range(0, self.__x):
            row = []
            for j in range(0, self.__y):
                row.append(' ')
            self.__mapUnits.append(row)

    def __generateObjects(self):
        self.__objects.append(Healh(random.randint(1, self.__x - 2), random.randint(1, self.__y - 2)))
        self.__objects.append(Gold(random.randint(1, self.__x - 2), random.randint(1, self.__y - 2)))
        self.__objects.append(Castle(random.randint(1, self.__x - 2), random.randint(1, self.__y - 2)))
        self.__objects.append(Altar(random.randint(1, self.__x - 2), random.randint(1, self.__y - 2)))

    def __generateTerrain(self):
        for i in range(0, self.__x):
            row = []
            for j in range(0, self.__y):
                if i == 0 or i == self.__x - 1 or j == 0 or j == self.__y - 1:
                    row.append(EndMap())
                else:
                    n = random.randint(0, 2)
                    if terrainTypes[n] == 'Water':
                        row.append(Water())
                    elif terrainTypes[n] == 'Mountain':
                        row.append(Mountain())
                    elif terrainTypes[n] == 'Field':
                        row.append(Field())
            self.__mapTerrain.append(row)
        

    def show(self, bases, units):
        map = self.__mergeMaps(bases, units)

        for i in range(0, self.__x):
            row = ""
            for j in range(0, self.__y):
                row = row + map[i][j] + " "
            print(row)

    def __mergeMaps(self, bases, units):        
        map = []
        for i in range(0, self.__x):
            row = [] 
            for j in range(0, self.__y):
                row.append(self.__mapTerrain[i][j].getView())
            map.append(row)

        for o in self.__objects:
            map[int(o.LocX())][int(o.LocY())] = o.getView()

        for b in bases:
            map[int(b.LocX())][int(b.LocY())] = b.getView()
        
        for u in units:
            map[int(u.LocX())][int(u.LocY())] = u.getView()
        
        return map

    